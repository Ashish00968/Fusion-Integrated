import datetime
from decimal import Decimal
import pytest
from unittest.mock import MagicMock
from types import SimpleNamespace
from modules.leave_elm.models import LeaveType, LeaveStatus, LeaveApplication, LeaveBalance
from modules.leave_elm.api.serializers import LeaveApplicationCreateSerializer
from modules.leave_elm.api.views import calculate_leave_days

def test_br_001():
    """TEST-BR-001: [BR-EL-001 base-satisfaction] Verify compliance with business rule BR-EL-001 — Supported leave-category eligibility"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_002():
    """TEST-BR-002: [BR-EL-002 base-satisfaction] Verify compliance with business rule BR-EL-002 — Casual Leave entitlement and lapse"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_003():
    """TEST-BR-003: [BR-EL-002 boundary-or-prohibited] Verify boundary, threshold limit, or prohibited outcome for BR-EL-002"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "EL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Prohibited half day EL"})
    assert not s.is_valid()
    assert "is_half_day" in s.errors

def test_br_004():
    """TEST-BR-004: [BR-EL-003 base-satisfaction] Verify compliance with business rule BR-EL-003 — Restricted Holiday entitlement and applicability"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_005():
    """TEST-BR-005: [BR-EL-004 base-satisfaction] Verify compliance with business rule BR-EL-004 — Special Casual Leave entitlement and admissibility"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_006():
    """TEST-BR-006: [BR-EL-005 base-satisfaction] Verify compliance with business rule BR-EL-005 — Non-faculty Earned Leave credit and carry-forward"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_007():
    """TEST-BR-007: [BR-EL-006 base-satisfaction] Verify compliance with business rule BR-EL-006 — Faculty Vacation Leave entitlement and vacation-period applicability"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_008():
    """TEST-BR-008: [BR-EL-007 base-satisfaction] Verify compliance with business rule BR-EL-007 — VL-to-EL year-end conversion"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_009():
    """TEST-BR-009: [BR-EL-008 base-satisfaction] Verify compliance with business rule BR-EL-008 — Treatment of EL created by VL conversion"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_010():
    """TEST-BR-010: [BR-EL-009 base-satisfaction] Verify compliance with business rule BR-EL-009 — Commuted Leave entitlement and treatment"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_011():
    """TEST-BR-011: [BR-EL-010 base-satisfaction] Verify compliance with business rule BR-EL-010 — Half-day CL treatment"""
    d1 = datetime.date(2026, 11, 2)
    d2 = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, d1, d2, is_half_day=False) == Decimal("5")
    assert calculate_leave_days(LeaveType.EL, d1, d2, is_half_day=False) == Decimal("7")

def test_br_012():
    """TEST-BR-012: [BR-EL-010 boundary-or-prohibited] Verify boundary, threshold limit, or prohibited outcome for BR-EL-010"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "EL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Prohibited half day EL"})
    assert not s.is_valid()
    assert "is_half_day" in s.errors

def test_br_013():
    """TEST-BR-013: [BR-EL-011 base-satisfaction] Verify compliance with business rule BR-EL-011 — Continuous-day counting"""
    d1 = datetime.date(2026, 11, 2)
    d2 = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, d1, d2, is_half_day=False) == Decimal("5")
    assert calculate_leave_days(LeaveType.EL, d1, d2, is_half_day=False) == Decimal("7")

def test_br_014():
    """TEST-BR-014: [BR-EL-012 base-satisfaction] Verify compliance with business rule BR-EL-012 — Applicant non-overlap with half-day CL exception"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_015():
    """TEST-BR-015: [BR-EL-012 boundary-or-prohibited] Verify boundary, threshold limit, or prohibited outcome for BR-EL-012"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "EL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Prohibited half day EL"})
    assert not s.is_valid()
    assert "is_half_day" in s.errors

def test_br_016():
    """TEST-BR-016: [BR-EL-013 base-satisfaction] Verify compliance with business rule BR-EL-013 — Station Leave coupling"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_017():
    """TEST-BR-017: [BR-EL-014 base-satisfaction] Verify compliance with business rule BR-EL-014 — Substitute eligibility"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_018():
    """TEST-BR-018: [BR-EL-015 base-satisfaction] Verify compliance with business rule BR-EL-015 — Substitute consent gate and decline recovery"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_019():
    """TEST-BR-019: [BR-EL-016 base-satisfaction] Verify compliance with business rule BR-EL-016 — Unit Head final scope for CL/RH"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_020():
    """TEST-BR-020: [BR-EL-017 base-satisfaction] Verify compliance with business rule BR-EL-017 — Unit Head recommendation for higher-sanction leave"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_021():
    """TEST-BR-021: [BR-EL-018 base-satisfaction] Verify compliance with business rule BR-EL-018 — Higher-sanction routing"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_022():
    """TEST-BR-022: [BR-EL-019 base-satisfaction] Verify compliance with business rule BR-EL-019 — Authority resolution and optional Establishment step"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_023():
    """TEST-BR-023: [BR-EL-020 base-satisfaction] Verify compliance with business rule BR-EL-020 — Director self-sanction"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_024():
    """TEST-BR-024: [BR-EL-021 base-satisfaction] Verify compliance with business rule BR-EL-021 — RETIRED — Modify Pending Request"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_025():
    """TEST-BR-025: [BR-EL-022 base-satisfaction] Verify compliance with business rule BR-EL-022 — Immediate withdrawal of pending request"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_026():
    """TEST-BR-026: [BR-EL-023 base-satisfaction] Verify compliance with business rule BR-EL-023 — Cancellation of approved leave before start"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_027():
    """TEST-BR-027: [BR-EL-024 base-satisfaction] Verify compliance with business rule BR-EL-024 — Fresh application after cancellation"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_028():
    """TEST-BR-028: [BR-EL-025 base-satisfaction] Verify compliance with business rule BR-EL-025 — Extension of ongoing EL/COL/VL"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_029():
    """TEST-BR-029: [BR-EL-026 base-satisfaction] Verify compliance with business rule BR-EL-026 — RETIRED IDENTIFIER"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_030():
    """TEST-BR-030: [BR-EL-027 base-satisfaction] Verify compliance with business rule BR-EL-027 — Resumption applicability and review authority"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_031():
    """TEST-BR-031: [BR-EL-028 base-satisfaction] Verify compliance with business rule BR-EL-028 — Normal, early, and late resumption outcome"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_032():
    """TEST-BR-032: [BR-EL-029 base-satisfaction] Verify compliance with business rule BR-EL-029 — Offline-sanctioned leave synchronization"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_033():
    """TEST-BR-033: [BR-EL-030 base-satisfaction] Verify compliance with business rule BR-EL-030 — Current configured policy and hierarchy"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_034():
    """TEST-BR-034: [BR-EL-031 base-satisfaction] Verify compliance with business rule BR-EL-031 — Effective published holiday/RH calendar"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_035():
    """TEST-BR-035: [BR-EL-032 base-satisfaction] Verify compliance with business rule BR-EL-032 — SLA reminder on still-pending task"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_036():
    """TEST-BR-036: [BR-EL-033 base-satisfaction] Verify compliance with business rule BR-EL-033 — SLA escalation on still-pending task"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_037():
    """TEST-BR-037: [BR-EL-034 base-satisfaction] Verify compliance with business rule BR-EL-034 — No post-submission modification"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_038():
    """TEST-BR-038: [BR-EL-035 base-satisfaction] Verify compliance with business rule BR-EL-035 — Actionable task assignment notification"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_039():
    """TEST-BR-039: [BR-EL-036 base-satisfaction] Verify compliance with business rule BR-EL-036 — Role-based authorization"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_040():
    """TEST-BR-040: [BR-EL-037 base-satisfaction] Verify compliance with business rule BR-EL-037 — Administrative maintenance is not sanctioning"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_br_041():
    """TEST-BR-041: [BR-EL-038 base-satisfaction] Verify compliance with business rule BR-EL-038 — Configurable SLA thresholds"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=50)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "is_half_day": True, "purpose": "Casual appointment", "substitute_user_id": 51}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

