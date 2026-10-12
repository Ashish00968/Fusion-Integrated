from django.urls import path

from modules.leave_elm.api import views

app_name = "leave_elm"

urlpatterns = [
    # Policy and Balances
    path("policies/", views.LeavePolicyListView.as_view(), name="policy-list"),
    path("balances/", views.LeaveBalanceListView.as_view(), name="balance-list"),
    path("holidays/", views.HolidayCalendarListView.as_view(), name="holiday-list"),
    # Applications
    path(
        "applications/",
        views.LeaveApplicationListCreateView.as_view(),
        name="application-list-create",
    ),
    path(
        "applications/<int:pk>/",
        views.LeaveApplicationDetailView.as_view(),
        name="application-detail",
    ),
    path(
        "applications/<int:pk>/withdraw/",
        views.LeaveWithdrawView.as_view(),
        name="application-withdraw",
    ),
    path(
        "applications/<int:pk>/cancel/",
        views.LeaveCancelView.as_view(),
        name="application-cancel",
    ),
    path(
        "applications/<int:pk>/action/",
        views.LeaveReviewActionView.as_view(),
        name="application-review-action",
    ),
    path(
        "applications/<int:pk>/resumption/",
        views.DutyResumptionView.as_view(),
        name="application-resumption",
    ),
    # Substitutes
    path(
        "substitutes/pending/",
        views.SubstituteRequestListView.as_view(),
        name="substitute-pending-list",
    ),
    path(
        "substitutes/<int:pk>/respond/",
        views.SubstituteRespondView.as_view(),
        name="substitute-respond",
    ),
    # Approvals Queue
    path(
        "approvals/pending/",
        views.PendingApprovalsListView.as_view(),
        name="approvals-pending-list",
    ),
    # Administration and Verification
    path(
        "resumptions/<int:pk>/review/",
        views.DutyResumptionReviewView.as_view(),
        name="resumption-review",
    ),
    path("policies/manage/", views.LeavePolicyManageView.as_view(), name="policy-manage"),
    path("offline-records/", views.OfflineLeaveRecordView.as_view(), name="offline-record"),
]
