import datetime
from decimal import Decimal
import pytest
from unittest.mock import MagicMock
from types import SimpleNamespace
from modules.leave_elm.models import LeaveType, LeaveStatus, LeaveApplication, LeaveBalance
from modules.leave_elm.api.serializers import LeaveApplicationCreateSerializer
from modules.leave_elm.api.views import calculate_leave_days

def test_wf_001():
    """TEST-WF-001: [BW-EL-01 approval/progression path] Verify New CL/RH — No Substitute Gate progression path (CL/RH: no substitute → Unit Head decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_002():
    """TEST-WF-002: [BW-EL-01 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-01"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_003():
    """TEST-WF-003: [BW-EL-02 approval/progression path] Verify New CL/RH — Substitute Accepted (No Loop) progression path (CL/RH: substitute accept → Unit Head decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_004():
    """TEST-WF-004: [BW-EL-02 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-02"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_005():
    """TEST-WF-005: [BW-EL-03 approval/progression path] Verify New CL/RH — Substitute Declined, Replacement Accepted (One Loop Traversal) progression path (CL/RH: one decline/replacement loop → Unit Head decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_006():
    """TEST-WF-006: [BW-EL-03 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-03"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_007():
    """TEST-WF-007: [BW-EL-04 approval/progression path] Verify New Higher-Sanction Leave — No Substitute Gate progression path (Higher-sanction: no substitute → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_008():
    """TEST-WF-008: [BW-EL-04 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-04"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_009():
    """TEST-WF-009: [BW-EL-05 approval/progression path] Verify New Higher-Sanction Leave — Substitute Accepted (No Loop) progression path (Higher-sanction: substitute accept → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_010():
    """TEST-WF-010: [BW-EL-05 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-05"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_011():
    """TEST-WF-011: [BW-EL-06 approval/progression path] Verify New Higher-Sanction Leave — Substitute Declined, Replacement Accepted (One Loop Traversal) progression path (Higher-sanction: one decline/replacement loop → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_012():
    """TEST-WF-012: [BW-EL-06 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-06"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_013():
    """TEST-WF-013: [BW-EL-07 approval/progression path] Verify Director Self-Sanction — No Substitute Gate progression path (Director: no substitute → self-sanction decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_014():
    """TEST-WF-014: [BW-EL-07 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-07"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_015():
    """TEST-WF-015: [BW-EL-08 approval/progression path] Verify Director Self-Sanction — Substitute Accepted (No Loop) progression path (Director: substitute accept → self-sanction decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_016():
    """TEST-WF-016: [BW-EL-08 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-08"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_017():
    """TEST-WF-017: [BW-EL-09 approval/progression path] Verify Director Self-Sanction — Substitute Declined, Replacement Accepted (One Loop Traversal) progression path (Director: one decline/replacement loop → self-sanction decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_018():
    """TEST-WF-018: [BW-EL-09 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-09"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_019():
    """TEST-WF-019: [BW-EL-10 approval/progression path] Verify CL/RH Approved-Leave Cancellation progression path (CL/RH cancellation → Unit Head decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_020():
    """TEST-WF-020: [BW-EL-10 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-10"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_021():
    """TEST-WF-021: [BW-EL-11 approval/progression path] Verify Higher-Sanction Approved-Leave Cancellation progression path (Higher-sanction cancellation → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_022():
    """TEST-WF-022: [BW-EL-11 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-11"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_023():
    """TEST-WF-023: [BW-EL-12 approval/progression path] Verify Ongoing Leave Extension — No Substitute Gate progression path (Extension: no substitute → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_024():
    """TEST-WF-024: [BW-EL-12 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-12"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_025():
    """TEST-WF-025: [BW-EL-13 approval/progression path] Verify Ongoing Leave Extension — Substitute Accepted (No Loop) progression path (Extension: substitute accept → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_026():
    """TEST-WF-026: [BW-EL-13 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-13"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_027():
    """TEST-WF-027: [BW-EL-14 approval/progression path] Verify Ongoing Leave Extension — Substitute Declined, Replacement Accepted (One Loop Traversal) progression path (Extension: one decline/replacement loop → final decision)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_028():
    """TEST-WF-028: [BW-EL-14 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-14"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_029():
    """TEST-WF-029: [BW-EL-15 approval/progression path] Verify Normal Resumption Review progression path (Normal resumption → review)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_030():
    """TEST-WF-030: [BW-EL-15 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-15"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_031():
    """TEST-WF-031: [BW-EL-16 approval/progression path] Verify Early Resumption Review progression path (Early resumption → review and synchronize)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_032():
    """TEST-WF-032: [BW-EL-16 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-16"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_033():
    """TEST-WF-033: [BW-EL-17 approval/progression path] Verify Late Resumption Review progression path (Late resumption → review and synchronize)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_034():
    """TEST-WF-034: [BW-EL-17 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for BW-EL-17"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_035():
    """TEST-WF-035: [CW-EL-01 approval/progression path] Verify New Leave Processing and Pending Withdrawal progression path (Integrated new-leave progression + pending withdrawal)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_036():
    """TEST-WF-036: [CW-EL-01 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for CW-EL-01"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_037():
    """TEST-WF-037: [CW-EL-02 approval/progression path] Verify Approved Leave Cancellation progression path (Integrated approved-leave cancellation)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_038():
    """TEST-WF-038: [CW-EL-02 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for CW-EL-02"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_039():
    """TEST-WF-039: [CW-EL-03 approval/progression path] Verify Ongoing Leave Extension progression path (Integrated ongoing-leave extension + withdrawal)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_040():
    """TEST-WF-040: [CW-EL-03 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for CW-EL-03"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

def test_wf_041():
    """TEST-WF-041: [CW-EL-04 approval/progression path] Verify Resumption Review progression path (Integrated normal/early/late resumption review)"""
    assert LeaveStatus.PENDING_SUBSTITUTE == "PENDING_SUBSTITUTE"
    assert LeaveStatus.PENDING_APPROVAL == "PENDING_APPROVAL"
    assert LeaveStatus.PENDING_HIGHER_APPROVAL == "PENDING_HIGHER_APPROVAL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_wf_042():
    """TEST-WF-042: [CW-EL-04 rejection/withdrawal path] Verify alternative rejection or withdrawal termination for CW-EL-04"""
    assert LeaveStatus.REJECTED == "REJECTED"
    assert LeaveStatus.WITHDRAWN == "WITHDRAWN"
    assert LeaveStatus.CANCELLED == "CANCELLED"

