from decimal import Decimal

from django.db import models

from core.db.mixins import TimeStampedModel, UserScopedModel
from modules.leave_elm.models.policy import LeaveCategory


class LeaveApplicationStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    SUBSTITUTE_PENDING = "SUBSTITUTE_PENDING", "Pending Substitute Consent"
    PENDING_UNIT_HEAD = "PENDING_UNIT_HEAD", "Pending Unit Head Recommendation/Sanction"
    PENDING_SANCTION = "PENDING_SANCTION", "Pending Higher Sanction"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    WITHDRAWN = "WITHDRAWN", "Withdrawn"
    CANCELLED = "CANCELLED", "Cancelled"


class HalfDaySlot(models.TextChoices):
    NONE = "NONE", "Full Day"
    FIRST_HALF = "FIRST_HALF", "First Half"
    SECOND_HALF = "SECOND_HALF", "Second Half"


class LeaveApplication(TimeStampedModel, UserScopedModel):
    """Leave Application (CFR-EL-002, AFR-EL-002..005, EL-UC-001)."""

    application_number = models.CharField(max_length=32, unique=True, db_index=True)
    leave_category = models.CharField(max_length=10, choices=LeaveCategory.choices, db_index=True)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(db_index=True)
    is_half_day = models.BooleanField(default=False)
    half_day_slot = models.CharField(
        max_length=15,
        choices=HalfDaySlot.choices,
        default=HalfDaySlot.NONE,
    )
    chargeable_days = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("1.00"))
    purpose = models.TextField()
    status = models.CharField(
        max_length=25,
        choices=LeaveApplicationStatus.choices,
        default=LeaveApplicationStatus.SUBSTITUTE_PENDING,
        db_index=True,
    )
    current_assignee_user_id = models.IntegerField(null=True, blank=True, db_index=True)
    medical_certificate_url = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "elm_leave_application"
        indexes = [
            models.Index(fields=["user_id", "status"], name="elm_app_user_status_idx"),
            models.Index(fields=["start_date", "end_date"], name="elm_app_dates_idx"),
        ]

    def __str__(self) -> str:
        return f"[{self.application_number}] {self.leave_category} ({self.status})"


class StationLeaveDetail(TimeStampedModel):
    """Coupled station leave details for out-of-station travels (BR-EL-013)."""

    application = models.OneToOneField(
        LeaveApplication,
        on_delete=models.CASCADE,
        related_name="station_leave",
    )
    leaving_station_at = models.DateTimeField()
    returning_to_station_at = models.DateTimeField()
    station_address = models.TextField()
    emergency_contact = models.CharField(max_length=20)

    class Meta:
        db_table = "elm_station_leave_detail"

    def __str__(self) -> str:
        return f"Station Leave for {self.application.application_number}"


class SubstituteStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    DECLINED = "DECLINED", "Declined"


class SubstituteAssignment(TimeStampedModel):
    """Substitute coverage nomination & consent gate (BR-EL-014, BR-EL-015, EL-UC-002)."""

    application = models.ForeignKey(
        LeaveApplication,
        on_delete=models.CASCADE,
        related_name="substitutes",
    )
    substitute_user_id = models.IntegerField(db_index=True)
    responsibilities = models.TextField()
    status = models.CharField(
        max_length=15,
        choices=SubstituteStatus.choices,
        default=SubstituteStatus.PENDING,
    )
    responded_at = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True)

    class Meta:
        db_table = "elm_substitute_assignment"
        indexes = [
            models.Index(fields=["substitute_user_id", "status"], name="elm_sub_user_status_idx"),
        ]

    def __str__(self) -> str:
        return f"Sub {self.substitute_user_id} ({self.status})"
