import uuid
from decimal import Decimal

from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from modules.leave_elm.models import (
    DutyResumption,
    HalfDaySlot,
    LeaveActionLog,
    LeaveApplication,
    LeaveApplicationStatus,
    ResumptionStatus,
    ResumptionType,
    ReviewDecision,
    ReviewStage,
    StationLeaveDetail,
    SubstituteAssignment,
    SubstituteStatus,
)


@transaction.atomic
def apply_for_leave(
    user_id: int,
    data: dict,
) -> LeaveApplication:
    """Submit a new leave application (CFR-EL-002, AFR-EL-002..005, EL-UC-001)."""
    start_date = data["start_date"]
    end_date = data["end_date"]
    category = data["leave_category"]

    if end_date < start_date:
        raise ValidationError("End date cannot precede start date.")

    # Calculate days
    if data.get("is_half_day"):
        chargeable_days = Decimal("0.50")
    else:
        total_days = (end_date - start_date).days + 1
        chargeable_days = Decimal(str(total_days))

    app_number = f"ELM-{timezone.now().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"

    sub_pending = LeaveApplicationStatus.SUBSTITUTE_PENDING
    unit_pending = LeaveApplicationStatus.PENDING_UNIT_HEAD
    initial_status = sub_pending if data.get("substitute_user_id") else unit_pending

    application = LeaveApplication.objects.create(
        application_number=app_number,
        user_id=user_id,
        leave_category=category,
        start_date=start_date,
        end_date=end_date,
        is_half_day=data.get("is_half_day", False),
        half_day_slot=data.get("half_day_slot", HalfDaySlot.NONE),
        chargeable_days=chargeable_days,
        purpose=data["purpose"],
        status=initial_status,
        medical_certificate_url=data.get("medical_certificate_url", ""),
    )

    # Couple Station Leave if outside Jabalpur (BR-EL-013)
    if data.get("is_station_leave"):
        StationLeaveDetail.objects.create(
            application=application,
            leaving_station_at=data["leaving_station_at"],
            returning_to_station_at=data["returning_to_station_at"],
            station_address=data.get("station_address", ""),
            emergency_contact=data.get("emergency_contact", ""),
        )

    # Nominate substitute if required (BR-EL-014, BR-EL-015)
    sub_user_id = data.get("substitute_user_id")
    if sub_user_id:
        if sub_user_id == user_id:
            raise ValidationError("Applicant cannot nominate themselves as substitute.")
        SubstituteAssignment.objects.create(
            application=application,
            substitute_user_id=sub_user_id,
            responsibilities=data.get(
                "substitute_responsibilities", "General duties handover"
            ),
            status=SubstituteStatus.PENDING,
        )

    return application


@transaction.atomic
def respond_substitute_request(
    substitute_user_id: int,
    assignment_id: int,
    decision: str,
    remarks: str = "",
) -> SubstituteAssignment:
    """Respond to substitute nomination request (BR-EL-015, EL-UC-002)."""
    assignment = SubstituteAssignment.objects.select_for_update().get(
        id=assignment_id,
        substitute_user_id=substitute_user_id,
    )
    if assignment.status != SubstituteStatus.PENDING:
        raise ValidationError("Substitute request has already been processed.")

    assignment.status = (
        SubstituteStatus.ACCEPTED if decision == "ACCEPTED" else SubstituteStatus.DECLINED
    )
    assignment.responded_at = timezone.now()
    assignment.remarks = remarks
    assignment.save()

    app = assignment.application
    if decision == "ACCEPTED":
        app.status = LeaveApplicationStatus.PENDING_UNIT_HEAD
        app.save(update_fields=["status", "updated_at"])

    return assignment


@transaction.atomic
def withdraw_application(
    user_id: int,
    application_id: int,
) -> LeaveApplication:
    """Immediate withdrawal of pending request (BR-EL-022, EL-UC-007)."""
    app = LeaveApplication.objects.select_for_update().get(id=application_id, user_id=user_id)
    if app.status in [
        LeaveApplicationStatus.APPROVED,
        LeaveApplicationStatus.REJECTED,
        LeaveApplicationStatus.WITHDRAWN,
        LeaveApplicationStatus.CANCELLED,
    ]:
        raise ValidationError(f"Cannot withdraw application in status {app.status}.")

    app.status = LeaveApplicationStatus.WITHDRAWN
    app.save(update_fields=["status", "updated_at"])

    LeaveActionLog.objects.create(
        application=app,
        actor_user_id=user_id,
        stage=ReviewStage.UNIT_HEAD,
        decision=ReviewDecision.RECOMMENDED,
        remarks="Withdrawn by applicant.",
    )
    return app


@transaction.atomic
def cancel_approved_leave(
    user_id: int,
    application_id: int,
    reason: str = "",
) -> LeaveApplication:
    """Cancellation of approved leave before availing (BR-EL-023, EL-UC-008)."""
    app = LeaveApplication.objects.select_for_update().get(id=application_id, user_id=user_id)
    if app.status != LeaveApplicationStatus.APPROVED:
        raise ValidationError("Only approved leave can be cancelled.")
    if timezone.localdate() >= app.start_date:
        raise ValidationError("Cannot cancel leave once start date has passed.")

    app.status = LeaveApplicationStatus.CANCELLED
    app.save(update_fields=["status", "updated_at"])

    LeaveActionLog.objects.create(
        application=app,
        actor_user_id=user_id,
        stage=ReviewStage.UNIT_HEAD,
        decision=ReviewDecision.APPROVED,
        remarks=f"Cancellation requested: {reason}",
    )
    return app


@transaction.atomic
def review_leave_application(
    actor_user_id: int,
    application_id: int,
    stage: str,
    decision: str,
    remarks: str = "",
) -> LeaveApplication:
    """Unit Head review / Higher Sanction decision (BR-EL-016..020, EL-UC-003..005)."""
    app = LeaveApplication.objects.select_for_update().get(id=application_id)

    if decision == ReviewDecision.APPROVED:
        app.status = LeaveApplicationStatus.APPROVED
    elif decision == ReviewDecision.REJECTED:
        app.status = LeaveApplicationStatus.REJECTED
    elif decision in [ReviewDecision.RECOMMENDED, ReviewDecision.NOT_RECOMMENDED]:
        app.status = LeaveApplicationStatus.PENDING_SANCTION

    app.save(update_fields=["status", "updated_at"])

    LeaveActionLog.objects.create(
        application=app,
        actor_user_id=actor_user_id,
        stage=stage,
        decision=decision,
        remarks=remarks,
    )
    return app


@transaction.atomic
def submit_resumption(
    user_id: int,
    application_id: int,
    resumption_date,
    resumption_type: str = ResumptionType.NORMAL,
    variance_reason: str = "",
    fitness_certificate_url: str = "",
) -> DutyResumption:
    """Submit resumption of duty (BR-EL-027, BR-EL-028, EL-UC-010)."""
    app = LeaveApplication.objects.get(id=application_id, user_id=user_id)
    if app.status != LeaveApplicationStatus.APPROVED:
        raise ValidationError("Resumption can only be submitted for approved leaves.")

    resumption, _ = DutyResumption.objects.update_or_create(
        application=app,
        defaults={
            "resumption_date": resumption_date,
            "resumption_type": resumption_type,
            "variance_reason": variance_reason,
            "fitness_certificate_url": fitness_certificate_url,
            "status": ResumptionStatus.PENDING,
        },
    )
    return resumption
