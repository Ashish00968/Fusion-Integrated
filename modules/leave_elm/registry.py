"""What the server tells the shell about this module (ADR-0010).

Nav items carry `required_permission` and the server filters before sending —
the client does zero filtering, so a link a role cannot use never reaches the
browser at all.
"""

MODULE = {
    "code": "leave_elm",
    "label": "Leave Management",
    "icon": "CalendarBlank",
    "base_path": "/leave",
    "nav_section": "Leaves",
    "sort_order": 25,
    "status": "active",
}

NAV_ITEMS = []


#: Every permission this module recognises; ROLE_GRANTS below says who holds each.
PERMISSIONS = [
    ("leave_elm.application.view_self", "View own leave applications and balances"),
    ("leave_elm.application.apply", "Submit a new leave application"),
    ("leave_elm.application.withdraw", "Withdraw own pending leave request"),
    ("leave_elm.application.cancel", "Request cancellation of approved leave"),
    ("leave_elm.substitute.respond", "Accept or decline nominated substitute request"),
    ("leave_elm.resumption.submit", "Submit resumption of duty after leave"),
    ("leave_elm.application.review", "Review, recommend or sanction leave requests"),
    ("leave_elm.resumption.review", "Review and accept resumption of duty"),
    ("leave_elm.policy.manage", "Maintain leave policy, holidays and configurations"),
    ("leave_elm.record.manage", "Record offline-sanctioned leaves and adjustments"),
    ("leave_elm.system.year_end_convert", "System year-end leave conversion"),
    ("leave_elm.system.sla_escalate", "System automated SLA escalation"),
]

#: Performed by a service or a scheduled task, so no designation holds them.
SYSTEM_PERMISSIONS = [
    "leave_elm.system.year_end_convert",
    "leave_elm.system.sla_escalate",
]

_EMPLOYEE = [
    "leave_elm.application.view_self",
    "leave_elm.application.apply",
    "leave_elm.application.withdraw",
    "leave_elm.application.cancel",
    "leave_elm.substitute.respond",
    "leave_elm.resumption.submit",
]

_APPROVER = [
    *_EMPLOYEE,
    "leave_elm.application.review",
    "leave_elm.resumption.review",
]

_ADMIN = [
    *_APPROVER,
    "leave_elm.policy.manage",
    "leave_elm.record.manage",
]

#: Keyed by the designation name as it exists in globals_designation or IAM.
ROLE_GRANTS = {
    "student": [],
    "faculty": _EMPLOYEE,
    "staff": _EMPLOYEE,
    "Unit Head": _APPROVER,
    "Dean": _APPROVER,
    "Registrar": _APPROVER,
    "Director": _APPROVER,
    "Leave Approver": _APPROVER,
    "Establishment Admin": _ADMIN,
}
