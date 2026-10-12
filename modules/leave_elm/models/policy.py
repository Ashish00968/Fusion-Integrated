from decimal import Decimal

from django.db import models

from core.db.mixins import TimeStampedModel, UserScopedModel


class LeaveCategory(models.TextChoices):
    CL = "CL", "Casual Leave"
    RH = "RH", "Restricted Holiday"
    SCL = "SCL", "Special Casual Leave"
    EL = "EL", "Earned Leave"
    COL = "COL", "Commuted Leave"
    VL = "VL", "Vacation Leave"


class LeavePolicyConfig(TimeStampedModel):
    """Configured leave parameters (BR-EL-030)."""

    leave_category = models.CharField(max_length=10, choices=LeaveCategory.choices, unique=True)
    annual_quota = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    allows_half_day = models.BooleanField(default=False)
    continuous_counting = models.BooleanField(default=False)
    carries_forward = models.BooleanField(default=False)
    max_carry_forward = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    requires_substitute = models.BooleanField(default=False)
    requires_medical_proof = models.BooleanField(default=False)
    is_faculty_only = models.BooleanField(default=False)
    is_non_faculty_only = models.BooleanField(default=False)

    class Meta:
        db_table = "elm_policy_config"

    def __str__(self) -> str:
        return f"Policy: {self.leave_category}"


class LeaveBalance(TimeStampedModel, UserScopedModel):
    """Annual leave entitlement and balance tracking (BR-EL-002..009)."""

    year = models.PositiveSmallIntegerField(db_index=True)
    leave_category = models.CharField(max_length=10, choices=LeaveCategory.choices, db_index=True)
    credited_days = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    used_days = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    pending_days = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal("0.00"))
    carried_forward_days = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal("0.00")
    )

    class Meta:
        db_table = "elm_leave_balance"
        unique_together = ("user_id", "year", "leave_category")
        indexes = [
            models.Index(fields=["user_id", "year"], name="elm_balance_user_yr_idx"),
        ]

    @property
    def available_balance(self) -> Decimal:
        credited = self.credited_days + self.carried_forward_days
        consumed = self.used_days + self.pending_days
        return credited - consumed

    def __str__(self) -> str:
        return (
            f"User {self.user_id} - {self.leave_category} ({self.year}): "
            f"{self.available_balance} remaining"
        )
