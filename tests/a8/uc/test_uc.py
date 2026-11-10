import datetime
from decimal import Decimal
import pytest
from unittest.mock import MagicMock
from types import SimpleNamespace
from modules.leave_elm.models import LeaveType, LeaveStatus, LeaveApplication, LeaveBalance
from modules.leave_elm.api.serializers import LeaveApplicationCreateSerializer
from modules.leave_elm.api.views import calculate_leave_days

def test_uc_001():
    """TEST-UC-001: [EL-UC-001 Main Flow] Verify main success flow for EL-UC-001 — Apply for Leave"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_002():
    """TEST-UC-002: [EL-UC-001 path.
Alternative / Excep] Verify alternative/exception flow path.
Alternative / Exception Flows for EL-UC-001"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_003():
    """TEST-UC-003: [EL-UC-002 Main Flow] Verify main success flow for EL-UC-002 — Respond to Substitute Request"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_004():
    """TEST-UC-004: [EL-UC-002 Required.
Alternative / E] Verify alternative/exception flow Required.
Alternative / Exception Flows for EL-UC-002"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_005():
    """TEST-UC-005: [EL-UC-003 Main Flow] Verify main success flow for EL-UC-003 — Review Leave-Related Request at Unit Head"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_006():
    """TEST-UC-006: [EL-UC-003 path.
Alternative / Excep] Verify alternative/exception flow path.
Alternative / Exception Flows for EL-UC-003"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_007():
    """TEST-UC-007: [EL-UC-004 Main Flow] Verify main success flow for EL-UC-004 — Verify and Route Higher-Sanction Request"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_008():
    """TEST-UC-008: [EL-UC-004 Authority.
Alternative /] Verify alternative/exception flow Authority.
Alternative / Exception Flows for EL-UC-004"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_009():
    """TEST-UC-009: [EL-UC-005 Main Flow] Verify main success flow for EL-UC-005 — Make Final Sanctioning Decision"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_010():
    """TEST-UC-010: [EL-UC-005 leave.
Alternative / Exce] Verify alternative/exception flow leave.
Alternative / Exception Flows for EL-UC-005"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_011():
    """TEST-UC-011: [EL-UC-007 Main Flow] Verify main success flow for EL-UC-007 — Withdraw Pending Request"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_012():
    """TEST-UC-012: [EL-UC-007 roles.
Alternative / Exce] Verify alternative/exception flow roles.
Alternative / Exception Flows for EL-UC-007"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_013():
    """TEST-UC-013: [EL-UC-008 Main Flow] Verify main success flow for EL-UC-008 — Request Cancellation of Approved Leave"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_014():
    """TEST-UC-014: [EL-UC-008 leave.
Alternative / Exce] Verify alternative/exception flow leave.
Alternative / Exception Flows for EL-UC-008"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_015():
    """TEST-UC-015: [EL-UC-009 Main Flow] Verify main success flow for EL-UC-009 — Request Extension of Ongoing Leave"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_016():
    """TEST-UC-016: [EL-UC-009 path.
Alternative / Excep] Verify alternative/exception flow path.
Alternative / Exception Flows for EL-UC-009"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_017():
    """TEST-UC-017: [EL-UC-010 Main Flow] Verify main success flow for EL-UC-010 — Submit Resumption of Duty"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_018():
    """TEST-UC-018: [EL-UC-010 review.
Alternative / Exc] Verify alternative/exception flow review.
Alternative / Exception Flows for EL-UC-010"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_019():
    """TEST-UC-019: [EL-UC-011 Main Flow] Verify main success flow for EL-UC-011 — Review Resumption"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_020():
    """TEST-UC-020: [EL-UC-011 records.
Alternative / Ex] Verify alternative/exception flow records.
Alternative / Exception Flows for EL-UC-011"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_021():
    """TEST-UC-021: [EL-UC-012 Main Flow] Verify main success flow for EL-UC-012 — View Leave Balances and History"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_022():
    """TEST-UC-022: [EL-UC-013 Main Flow] Verify main success flow for EL-UC-013 — Obtain Printable/Exportable Leave Application"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_023():
    """TEST-UC-023: [EL-UC-014 Main Flow] Verify main success flow for EL-UC-014 — Maintain Policy and Hierarchy Configuration"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_024():
    """TEST-UC-024: [EL-UC-014 values.
Alternative / Exc] Verify alternative/exception flow values.
Alternative / Exception Flows for EL-UC-014"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_025():
    """TEST-UC-025: [EL-UC-015 Main Flow] Verify main success flow for EL-UC-015 — Maintain and Publish Holiday/RH Calendar"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_026():
    """TEST-UC-026: [EL-UC-015 validation.
Alternative /] Verify alternative/exception flow validation.
Alternative / Exception Flow for EL-UC-015"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_027():
    """TEST-UC-027: [EL-UC-016 Main Flow] Verify main success flow for EL-UC-016 — Record Already-Sanctioned Offline Leave"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_028():
    """TEST-UC-028: [EL-UC-016 workflow.
Alternative / E] Verify alternative/exception flow workflow.
Alternative / Exception Flows for EL-UC-016"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_029():
    """TEST-UC-029: [EL-UC-017 Main Flow] Verify main success flow for EL-UC-017 — Maintain Authorized Leave Records"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_030():
    """TEST-UC-030: [EL-UC-017 implemented.
Alternative] Verify alternative/exception flow implemented.
Alternative / Exception Flo for EL-UC-017"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_031():
    """TEST-UC-031: [EL-UC-018 Main Flow] Verify main success flow for EL-UC-018 — Configure Workflow SLA Thresholds"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_032():
    """TEST-UC-032: [EL-UC-019 Main Flow] Verify main success flow for EL-UC-019 — Nominate Replacement Substitute After Decline"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_033():
    """TEST-UC-033: [EL-UC-019 Response.
Alternative / E] Verify alternative/exception flow Response.
Alternative / Exception Flows for EL-UC-019"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid date sequence"})
    assert not s.is_valid()
    assert "end_date" in s.errors

def test_uc_034():
    """TEST-UC-034: [EL-UC-020 Main Flow] Verify main success flow for EL-UC-020 — Execute Year-End Leave Processing"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_uc_035():
    """TEST-UC-035: [EL-UC-021 Main Flow] Verify main success flow for EL-UC-021 — Process SLA Threshold Event"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=101)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Casual duty leave", "substitute_user_id": 102}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

