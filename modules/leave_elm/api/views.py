from django.utils import timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from fusion_auth.permissions import HasModuleGrant, HasPermission
from modules.leave_elm import selectors, services
from modules.leave_elm.api import serializers as s
from modules.leave_elm.models import (
    LeaveApplication,
    LeavePolicyConfig,
)

MODULE = HasModuleGrant("leave_elm")

P_VIEW_SELF = "leave_elm.application.view_self"
P_APPLY = "leave_elm.application.apply"
P_WITHDRAW = "leave_elm.application.withdraw"
P_CANCEL = "leave_elm.application.cancel"
P_SUB_RESPOND = "leave_elm.substitute.respond"
P_REVIEW = "leave_elm.application.review"
P_RESUMPTION_SUBMIT = "leave_elm.resumption.submit"
P_RESUMPTION_REVIEW = "leave_elm.resumption.review"
P_POLICY_MANAGE = "leave_elm.policy.manage"
P_RECORD_MANAGE = "leave_elm.record.manage"


def _actor(request):
    return getattr(request, "principal", None)


class LeavePolicyListView(generics.ListAPIView):
    serializer_class = s.LeavePolicyConfigSerializer
    permission_classes = [MODULE]
    queryset = LeavePolicyConfig.objects.all()


class LeaveBalanceListView(generics.ListAPIView):
    serializer_class = s.LeaveBalanceSerializer
    permission_classes = [MODULE, HasPermission(P_VIEW_SELF)]

    def get_queryset(self):
        actor = _actor(self.request)
        year = self.request.query_params.get("year", timezone.now().year)
        try:
            year = int(year)
        except ValueError:
            year = timezone.now().year
        return selectors.get_my_balances(actor.user_id, year)


class LeaveApplicationListCreateView(generics.ListCreateAPIView):
    permission_classes = [MODULE, HasPermission(P_VIEW_SELF)]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return s.LeaveApplicationCreateSerializer
        return s.LeaveApplicationReadSerializer

    def get_queryset(self):
        actor = _actor(self.request)
        return selectors.get_my_applications(actor.user_id)

    def create(self, request, *args, **kwargs):
        actor = _actor(request)
        serializer = s.LeaveApplicationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        app = services.apply_for_leave(actor.user_id, serializer.validated_data)
        return Response(s.LeaveApplicationReadSerializer(app).data, status=status.HTTP_201_CREATED)


class LeaveApplicationDetailView(generics.RetrieveAPIView):
    serializer_class = s.LeaveApplicationReadSerializer
    permission_classes = [MODULE]
    lookup_field = "pk"
    queryset = LeaveApplication.objects.all()


class LeaveWithdrawView(APIView):
    permission_classes = [MODULE, HasPermission(P_WITHDRAW)]

    def post(self, request, pk: int):
        actor = _actor(request)
        app = services.withdraw_application(actor.user_id, pk)
        return Response(s.LeaveApplicationReadSerializer(app).data)


class LeaveCancelView(APIView):
    permission_classes = [MODULE, HasPermission(P_CANCEL)]

    def post(self, request, pk: int):
        actor = _actor(request)
        reason = request.data.get("reason", "")
        app = services.cancel_approved_leave(actor.user_id, pk, reason)
        return Response(s.LeaveApplicationReadSerializer(app).data)


class SubstituteRequestListView(generics.ListAPIView):
    serializer_class = s.SubstituteAssignmentSerializer
    permission_classes = [MODULE, HasPermission(P_SUB_RESPOND)]

    def get_queryset(self):
        actor = _actor(self.request)
        return selectors.get_pending_substitute_requests(actor.user_id)


class SubstituteRespondView(APIView):
    permission_classes = [MODULE, HasPermission(P_SUB_RESPOND)]

    def post(self, request, pk: int):
        actor = _actor(request)
        serializer = s.SubstituteResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        assignment = services.respond_substitute_request(
            actor.user_id,
            pk,
            serializer.validated_data["decision"],
            serializer.validated_data.get("remarks", ""),
        )
        return Response(s.SubstituteAssignmentSerializer(assignment).data)


class PendingApprovalsListView(generics.ListAPIView):
    serializer_class = s.LeaveApplicationReadSerializer
    permission_classes = [MODULE, HasPermission(P_REVIEW)]

    def get_queryset(self):
        actor = _actor(self.request)
        return selectors.get_pending_approvals_for_actor(actor.user_id)


class LeaveReviewActionView(APIView):
    permission_classes = [MODULE, HasPermission(P_REVIEW)]

    def post(self, request, pk: int):
        actor = _actor(request)
        stage = request.data.get("stage", "UNIT_HEAD")
        serializer = s.LeaveReviewActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        app = services.review_leave_application(
            actor.user_id,
            pk,
            stage=stage,
            decision=serializer.validated_data["decision"],
            remarks=serializer.validated_data.get("remarks", ""),
        )
        return Response(s.LeaveApplicationReadSerializer(app).data)


class DutyResumptionView(APIView):
    permission_classes = [MODULE, HasPermission(P_RESUMPTION_SUBMIT)]

    def post(self, request, pk: int):
        actor = _actor(request)
        resumption_date = request.data.get("resumption_date")
        resumption_type = request.data.get("resumption_type", "NORMAL")
        variance_reason = request.data.get("variance_reason", "")
        fitness_cert = request.data.get("fitness_certificate_url", "")
        resumption = services.submit_resumption(
            actor.user_id,
            pk,
            resumption_date=resumption_date,
            resumption_type=resumption_type,
            variance_reason=variance_reason,
            fitness_certificate_url=fitness_cert,
        )
        return Response(
            s.DutyResumptionSerializer(resumption).data,
            status=status.HTTP_201_CREATED,
        )


class DutyResumptionReviewView(APIView):
    permission_classes = [MODULE, HasPermission(P_RESUMPTION_REVIEW)]

    def post(self, request, pk: int):
        actor = _actor(request)
        decision = request.data.get("decision", "ACCEPTED")
        remarks = request.data.get("remarks", "")
        resumption = services.applications.DutyResumption.objects.get(pk=pk)
        resumption.status = decision
        resumption.reviewer_user_id = actor.user_id
        resumption.review_remarks = remarks
        resumption.save()
        return Response(s.DutyResumptionSerializer(resumption).data)


class LeavePolicyManageView(generics.CreateAPIView):
    serializer_class = s.LeavePolicyConfigSerializer
    permission_classes = [MODULE, HasPermission(P_POLICY_MANAGE)]
    queryset = LeavePolicyConfig.objects.all()


class OfflineLeaveRecordView(APIView):
    permission_classes = [MODULE, HasPermission(P_RECORD_MANAGE)]

    def post(self, request):
        target_user_id = request.data.get("user_id")
        serializer = s.LeaveApplicationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        app = services.apply_for_leave(target_user_id, serializer.validated_data)
        app.status = services.applications.LeaveApplicationStatus.APPROVED
        app.save(update_fields=["status", "updated_at"])
        return Response(s.LeaveApplicationReadSerializer(app).data, status=status.HTTP_201_CREATED)


class HolidayCalendarListView(generics.ListAPIView):
    serializer_class = s.HolidayCalendarEntrySerializer
    permission_classes = [MODULE]

    def get_queryset(self):
        year = self.request.query_params.get("year", timezone.now().year)
        try:
            year = int(year)
        except ValueError:
            year = timezone.now().year
        return selectors.get_active_holidays(year)
