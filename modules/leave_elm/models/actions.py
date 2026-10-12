from django.db import models

from core.db.mixins import TimeStampedModel
from modules.leave_elm.models.applications import LeaveApplication


class ReviewStage(models.TextChoices):
    UNIT_HEAD = "UNIT_HEAD", "Unit Head"
    ESTABLISHMENT = "ESTABLISHMENT", "Establishment Section"
    DEAN = "DEAN", "Dean"
    REGISTRAR = "REGISTRAR", "Registrar"
    DIRECTOR = "DIRECTOR", "Director"


class ReviewDecision(models.TextChoices):
    RECOMMENDED = "RECOMMENDED", "Recommended"
    NOT_RECOMMENDED = "NOT_RECOMMENDED", "Not Recommended"
    APPROVED = "APPROVED", "Approved"
    REJECTED = "REJECTED", "Rejected"
    ESCALATED = "ESCALATED", "Escalated"


class LeaveActionLog(TimeStampedModel):
    """Workflow state transitions and authority audit trail (BR-EL-016..020, EL-UC-003..005)."""

    application = models.ForeignKey(
        LeaveApplication,
        on_delete=models.CASCADE,
        related_name="action_logs",
    )
    actor_user_id = models.IntegerField(db_index=True)
    stage = models.CharField(max_length=20, choices=ReviewStage.choices)
    decision = models.CharField(max_length=20, choices=ReviewDecision.choices)
    remarks = models.TextField(blank=True)

    class Meta:
        db_table = "elm_action_log"
        indexes = [
            models.Index(fields=["actor_user_id", "created_at"], name="elm_log_actor_idx"),
        ]

    def __str__(self) -> str:
        app_num = self.application.application_number
        return f"{self.stage} {self.decision} on {app_num} by U:{self.actor_user_id}"
