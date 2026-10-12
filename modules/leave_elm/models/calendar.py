from django.db import models

from core.db.mixins import TimeStampedModel


class HolidayCalendarEntry(TimeStampedModel):
    """Institute Holiday and Restricted Holiday (RH) calendar (BR-EL-031, EL-UC-015)."""

    calendar_year = models.PositiveSmallIntegerField(db_index=True)
    date = models.DateField(db_index=True)
    name = models.CharField(max_length=150)
    is_restricted_holiday = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    class Meta:
        db_table = "elm_holiday_calendar"
        unique_together = ("calendar_year", "date")
        ordering = ["date"]

    def __str__(self) -> str:
        tag = "RH" if self.is_restricted_holiday else "Holiday"
        return f"{self.date} [{tag}]: {self.name}"


class WorkflowSLAConfig(TimeStampedModel):
    """Workflow SLA thresholds for reminders and escalation (BR-EL-032, BR-EL-033, BR-EL-038)."""

    stage = models.CharField(max_length=30, unique=True)
    reminder_hours = models.PositiveIntegerField(default=48)
    escalation_hours = models.PositiveIntegerField(default=96)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "elm_sla_config"

    def __str__(self) -> str:
        return f"SLA: {self.stage} (Rem:{self.reminder_hours}h, Esc:{self.escalation_hours}h)"
