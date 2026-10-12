from rest_framework import serializers

from modules.leave_elm.models import (
    DutyResumption,
    HalfDaySlot,
    HolidayCalendarEntry,
    LeaveActionLog,
    LeaveApplication,
    LeaveBalance,
    LeaveCategory,
    LeavePolicyConfig,
    StationLeaveDetail,
    SubstituteAssignment,
)


class LeavePolicyConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeavePolicyConfig
        fields = (
            "id",
            "leave_category",
            "annual_quota",
            "allows_half_day",
            "continuous_counting",
            "carries_forward",
            "max_carry_forward",
            "requires_substitute",
            "requires_medical_proof",
            "is_faculty_only",
            "is_non_faculty_only",
        )
        read_only_fields = fields


class LeaveBalanceSerializer(serializers.ModelSerializer):
    available_balance = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = LeaveBalance
        fields = (
            "id",
            "user_id",
            "year",
            "leave_category",
            "credited_days",
            "used_days",
            "pending_days",
            "carried_forward_days",
            "available_balance",
        )
        read_only_fields = fields


class StationLeaveDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationLeaveDetail
        fields = (
            "id",
            "leaving_station_at",
            "returning_to_station_at",
            "station_address",
            "emergency_contact",
        )


class SubstituteAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubstituteAssignment
        fields = (
            "id",
            "substitute_user_id",
            "responsibilities",
            "status",
            "responded_at",
            "remarks",
        )
        read_only_fields = ("id", "status", "responded_at")


class LeaveActionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveActionLog
        fields = (
            "id",
            "actor_user_id",
            "stage",
            "decision",
            "remarks",
            "created_at",
        )
        read_only_fields = fields


class DutyResumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyResumption
        fields = (
            "id",
            "resumption_date",
            "resumption_type",
            "variance_reason",
            "fitness_certificate_url",
            "status",
            "reviewer_user_id",
            "review_remarks",
            "created_at",
        )
        read_only_fields = ("id", "status", "reviewer_user_id", "review_remarks", "created_at")


class LeaveApplicationReadSerializer(serializers.ModelSerializer):
    station_leave = StationLeaveDetailSerializer(read_only=True)
    substitutes = SubstituteAssignmentSerializer(many=True, read_only=True)
    action_logs = LeaveActionLogSerializer(many=True, read_only=True)
    resumption = DutyResumptionSerializer(read_only=True)

    class Meta:
        model = LeaveApplication
        fields = (
            "id",
            "application_number",
            "user_id",
            "leave_category",
            "start_date",
            "end_date",
            "is_half_day",
            "half_day_slot",
            "chargeable_days",
            "purpose",
            "status",
            "current_assignee_user_id",
            "medical_certificate_url",
            "station_leave",
            "substitutes",
            "action_logs",
            "resumption",
            "created_at",
            "updated_at",
        )
        read_only_fields = fields


class LeaveApplicationCreateSerializer(serializers.Serializer):
    leave_category = serializers.ChoiceField(choices=LeaveCategory.choices)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    is_half_day = serializers.BooleanField(default=False)
    half_day_slot = serializers.ChoiceField(choices=HalfDaySlot.choices, default=HalfDaySlot.NONE)
    purpose = serializers.CharField()
    substitute_user_id = serializers.IntegerField(required=False, allow_null=True)
    substitute_responsibilities = serializers.CharField(required=False, allow_blank=True)
    medical_certificate_url = serializers.CharField(required=False, allow_blank=True)

    # Embedded Station Leave (BR-EL-013)
    is_station_leave = serializers.BooleanField(default=False)
    leaving_station_at = serializers.DateTimeField(required=False, allow_null=True)
    returning_to_station_at = serializers.DateTimeField(required=False, allow_null=True)
    station_address = serializers.CharField(required=False, allow_blank=True)
    emergency_contact = serializers.CharField(required=False, allow_blank=True)


class SubstituteResponseSerializer(serializers.Serializer):
    decision = serializers.ChoiceField(choices=["ACCEPTED", "DECLINED"])
    remarks = serializers.CharField(required=False, allow_blank=True)


class LeaveReviewActionSerializer(serializers.Serializer):
    decision = serializers.ChoiceField(
        choices=["RECOMMENDED", "NOT_RECOMMENDED", "APPROVED", "REJECTED"]
    )
    remarks = serializers.CharField(required=False, allow_blank=True)


class HolidayCalendarEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayCalendarEntry
        fields = ("id", "calendar_year", "date", "name", "is_restricted_holiday", "is_published")
        read_only_fields = fields
