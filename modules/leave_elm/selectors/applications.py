from django.db.models import QuerySet

from modules.leave_elm.models import (
    HolidayCalendarEntry,
    LeaveApplication,
    LeaveApplicationStatus,
    LeaveBalance,
    SubstituteAssignment,
)


def get_my_applications(user_id: int) -> QuerySet[LeaveApplication]:
    """Retrieve all applications for the authenticated applicant."""
    return LeaveApplication.objects.filter(user_id=user_id).order_by("-created_at")


def get_my_balances(user_id: int, year: int) -> QuerySet[LeaveBalance]:
    """Retrieve annual leave balances for the authenticated applicant."""
    return LeaveBalance.objects.filter(user_id=user_id, year=year)


def get_pending_substitute_requests(user_id: int) -> QuerySet[SubstituteAssignment]:
    """Retrieve pending substitute assignments where user is the nominated substitute."""
    return SubstituteAssignment.objects.filter(
        substitute_user_id=user_id,
        status="PENDING",
    ).select_related("application").order_by("-created_at")


def get_pending_approvals_for_actor(actor_user_id: int) -> QuerySet[LeaveApplication]:
    """Retrieve leave applications awaiting review by this assignee."""
    return LeaveApplication.objects.filter(
        current_assignee_user_id=actor_user_id,
        status__in=[
            LeaveApplicationStatus.PENDING_UNIT_HEAD,
            LeaveApplicationStatus.PENDING_SANCTION,
        ],
    ).order_by("-created_at")


def get_active_holidays(year: int) -> QuerySet[HolidayCalendarEntry]:
    """Retrieve published holidays and RH dates for the year."""
    return HolidayCalendarEntry.objects.filter(
        calendar_year=year,
        is_published=True,
    ).order_by("date")
