from django.db import models

from core.db.mixins import TimeStampedModel
from modules.leave_elm.models.applications import LeaveApplication


class ResumptionType(models.TextChoices):
    NORMAL = "NORMAL", "Normal (As Scheduled)"
    EARLY = "EARLY", "Early Resumption"
    LATE = "LATE", "Late Resumption (Overstay)"


class ResumptionStatus(models.TextChoices):
    PENDING = "PENDING", "Pending Review"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"


class DutyResumption(TimeStampedModel):
    """Resumption of duty submission and verification (BR-EL-027, BR-EL-028, EL-UC-010..011)."""

    application = models.OneToOneField(
        LeaveApplication,
        on_delete=models.CASCADE,
        related_name="resumption",
    )
    resumption_date = models.DateField(db_index=True)
    resumption_type = models.CharField(
        max_length=15,
        choices=ResumptionType.choices,
        default=ResumptionType.NORMAL,
    )
    variance_reason = models.TextField(blank=True)
    fitness_certificate_url = models.CharField(max_length=500, blank=True)
    status = models.CharField(
        max_length=15,
        choices=ResumptionStatus.choices,
        default=ResumptionStatus.PENDING,
    )
    reviewer_user_id = models.IntegerField(null=True, blank=True)
    review_remarks = models.TextField(blank=True)

    class Meta:
        db_table = "elm_duty_resumption"

    def __str__(self) -> str:
        return f"Resumption for {self.application.application_number} ({self.status})"
