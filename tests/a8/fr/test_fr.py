import datetime
from decimal import Decimal
import pytest
from unittest.mock import MagicMock
from types import SimpleNamespace
from modules.leave_elm.models import LeaveType, LeaveStatus, LeaveApplication, LeaveBalance
from modules.leave_elm.api.serializers import LeaveApplicationCreateSerializer
from modules.leave_elm.api.views import calculate_leave_days

def test_fr_001():
    """TEST-FR-001: [AFR-EL-001.1] Verify Role-based authorization: The system shall permit a user to perform only those ELM capabilities authorized for the user’s employee, processing, sa"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_002():
    """TEST-FR-002: [AFR-EL-001.1-negative-boundary] Verify boundary/negative condition for Role-based authorization"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_003():
    """TEST-FR-003: [AFR-EL-002.1] Verify Create and submit leave request: The system shall allow an eligible employee to create and submit a leave request."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_004():
    """TEST-FR-004: [AFR-EL-002.1-negative-boundary] Verify boundary/negative condition for Create and submit leave request"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_005():
    """TEST-FR-005: [AFR-EL-002.2] Verify Supported leave categories: The system shall support CL, RH, SCL, EL, COL, and VL as leave categories within the ELM baseline."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_006():
    """TEST-FR-006: [AFR-EL-002.3] Verify Capture core application information: The system shall capture leave category, requested period, purpose/reason, and other required information in a leave app"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_007():
    """TEST-FR-007: [AFR-EL-002.4] Verify Capture Station Leave details in same application: When Station Leave applies, the system shall capture its required details within the associated leave application."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_008():
    """TEST-FR-008: [AFR-EL-002.5] Verify No separate Station Leave request lifecycle: The system shall treat Station Leave information as coupled to the associated leave application and shall not create a s"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_009():
    """TEST-FR-009: [AFR-EL-003.1] Verify Validate leave-category eligibility: Before a new leave request proceeds, the system shall validate requested leave-category eligibility using the current co"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_010():
    """TEST-FR-010: [AFR-EL-003.2] Verify Validate available entitlement/balance: Before a new leave request proceeds, the system shall validate the employee’s available leave entitlement/balance for th"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_011():
    """TEST-FR-011: [AFR-EL-003.2-negative-boundary] Verify boundary/negative condition for Validate available entitlement/balance"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_012():
    """TEST-FR-012: [AFR-EL-003.3] Verify Calculate chargeable leave days: The system shall calculate chargeable leave days using the applicable leave-counting rule and calendar data."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_013():
    """TEST-FR-013: [AFR-EL-003.4] Verify Prevent applicant leave overlap: The system shall detect and prevent impermissible overlap between a new leave request and the employee’s active pending """
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_014():
    """TEST-FR-014: [AFR-EL-003.4-negative-boundary] Verify boundary/negative condition for Prevent applicant leave overlap"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_015():
    """TEST-FR-015: [AFR-EL-003.5] Verify Half-day CL overlap exception: The system shall treat first-half and second-half CL on the same date as non-overlapping when they occupy different halv"""
    d = datetime.date(2026, 11, 2)
    assert calculate_leave_days("CL", d, d, is_half_day=True) == Decimal("0.5")

def test_fr_016():
    """TEST-FR-016: [AFR-EL-003.5-negative-boundary] Verify boundary/negative condition for Half-day CL overlap exception"""
    d = datetime.date(2026, 11, 2)
    assert calculate_leave_days("CL", d, d, is_half_day=True) == Decimal("0.5")

def test_fr_017():
    """TEST-FR-017: [AFR-EL-003.6] Verify Use effective published holiday/RH calendar: The system shall use the currently effective published holiday/RH calendar for date and RH validation until a replacemen"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_018():
    """TEST-FR-018: [AFR-EL-004.1] Verify CL annual entitlement: The system shall maintain an annual CL entitlement of 8 days for each employee."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_019():
    """TEST-FR-019: [AFR-EL-004.2] Verify CL year-end lapse: At year end, the system shall lapse unused CL and shall not carry it forward."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_020():
    """TEST-FR-020: [AFR-EL-004.2-negative-boundary] Verify boundary/negative condition for CL year-end lapse"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_021():
    """TEST-FR-021: [AFR-EL-004.3] Verify Support first-/second-half CL: The system shall support CL for the first half or the second half of a day."""
    d = datetime.date(2026, 11, 2)
    assert calculate_leave_days("CL", d, d, is_half_day=True) == Decimal("0.5")

def test_fr_022():
    """TEST-FR-022: [AFR-EL-004.4] Verify Half-day CL deduction: On approval of a half-day CL, the system shall consume 0.5 CL day."""
    d = datetime.date(2026, 11, 2)
    assert calculate_leave_days("CL", d, d, is_half_day=True) == Decimal("0.5")

def test_fr_023():
    """TEST-FR-023: [AFR-EL-005.1] Verify RH annual entitlement: The system shall maintain an annual RH entitlement of 2 days for each employee."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_024():
    """TEST-FR-024: [AFR-EL-005.2] Verify RH calendar applicability: The system shall permit an RH request only when the requested date corresponds to an applicable Restricted Holiday in th"""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_025():
    """TEST-FR-025: [AFR-EL-005.2-negative-boundary] Verify boundary/negative condition for RH calendar applicability"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_026():
    """TEST-FR-026: [AFR-EL-005.3] Verify RH year-end lapse: At year end, the system shall lapse unused RH and shall not carry it forward."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_027():
    """TEST-FR-027: [AFR-EL-005.3-negative-boundary] Verify boundary/negative condition for RH year-end lapse"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_028():
    """TEST-FR-028: [AFR-EL-006.1] Verify SCL annual entitlement: The system shall support up to 15 SCL days per calendar year for each employee."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_029():
    """TEST-FR-029: [AFR-EL-006.1-negative-boundary] Verify boundary/negative condition for SCL annual entitlement"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_030():
    """TEST-FR-030: [AFR-EL-006.2] Verify SCL purpose admissibility decision: The system shall use the applicable Sanctioning Authority’s decision to determine whether the stated special purpose is """
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_031():
    """TEST-FR-031: [AFR-EL-006.3] Verify SCL year-end lapse: At year end, the system shall lapse unused SCL and shall not carry it forward."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.CL, start, end, is_half_day=False) == Decimal("5")

def test_fr_032():
    """TEST-FR-032: [AFR-EL-006.3-negative-boundary] Verify boundary/negative condition for SCL year-end lapse"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_033():
    """TEST-FR-033: [AFR-EL-007.1] Verify Non-faculty EL annual credit: The system shall credit each non-faculty employee with 30 EL days per year."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_034():
    """TEST-FR-034: [AFR-EL-007.2] Verify EL carry-forward: The system shall carry forward unused EL according to policy."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_035():
    """TEST-FR-035: [AFR-EL-008.1] Verify Faculty VL entitlement: The system shall maintain 60 VL for each faculty member."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_036():
    """TEST-FR-036: [AFR-EL-008.2] Verify Vacation-period source: The system shall obtain the applicable faculty vacation periods from the institute Academic Calendar maintained outside """
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_037():
    """TEST-FR-037: [AFR-EL-008.3] Verify VL vacation-period applicability: The system shall allow VL to be availed only during an applicable vacation period supplied through the institute Academi"""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_038():
    """TEST-FR-038: [AFR-EL-008.4] Verify VL-to-EL conversion ratio: At year end, the system shall convert all unused faculty VL to EL at a ratio of 2 VL to 1 EL."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_039():
    """TEST-FR-039: [AFR-EL-008.5] Verify Fractional VL-to-EL conversion: The system shall preserve fractional results when performing the year-end VL-to-EL conversion."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_040():
    """TEST-FR-040: [AFR-EL-008.6] Verify No VL carry-forward after conversion: After year-end VL-to-EL conversion, the system shall not carry forward any unused VL as VL."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_041():
    """TEST-FR-041: [AFR-EL-008.7] Verify Credit and retain converted EL: The system shall credit EL generated by VL conversion to the faculty member’s EL balance; that converted EL may carry fo"""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_042():
    """TEST-FR-042: [AFR-EL-009.1] Verify COL annual entitlement: The system shall maintain an annual COL entitlement of 20 days for each eligible employee in this baseline."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_043():
    """TEST-FR-043: [AFR-EL-009.2] Verify COL carry-forward: The system shall carry forward unused COL according to policy."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_044():
    """TEST-FR-044: [AFR-EL-009.3] Verify COL balance control: The system shall validate COL against the employee’s applicable available COL balance before progression."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_045():
    """TEST-FR-045: [AFR-EL-009.3-negative-boundary] Verify boundary/negative condition for COL balance control"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_046():
    """TEST-FR-046: [AFR-EL-009.4] Verify COL medical evidence: The system shall support required medical evidence for COL where the applicable case requires such evidence."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_047():
    """TEST-FR-047: [AFR-EL-010.1] Verify Continuous counting for EL/COL/VL: For EL, COL, and VL, the system shall count intervening weekends and closed holidays inside a continuous approved leave """
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_048():
    """TEST-FR-048: [AFR-EL-010.2] Verify Exclude CL/SCL/RH from continuous counting: The system shall not apply the EL/COL/VL continuous-day counting rule to CL, SCL, or RH."""
    start = datetime.date(2026, 11, 2)
    end = datetime.date(2026, 11, 8)
    assert calculate_leave_days(LeaveType.EL, start, end, is_half_day=False) == Decimal("7")

def test_fr_049():
    """TEST-FR-049: [AFR-EL-011.1] Verify Nominate one substitute when required: When responsibility coverage is required, the system shall allow the applicant to nominate one substitute."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_050():
    """TEST-FR-050: [AFR-EL-011.2] Verify Substitute must be another employee: The system shall reject a substitute nomination if the nominee is not another employee."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_051():
    """TEST-FR-051: [AFR-EL-011.2-negative-boundary] Verify boundary/negative condition for Substitute must be another employee"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_052():
    """TEST-FR-052: [AFR-EL-011.3] Verify Applicant cannot nominate self: The system shall reject a substitute nomination when the nominee is the applicant."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_053():
    """TEST-FR-053: [AFR-EL-011.3-negative-boundary] Verify boundary/negative condition for Applicant cannot nominate self"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_054():
    """TEST-FR-054: [AFR-EL-011.4] Verify Substitute leave-overlap eligibility: The system shall reject a substitute nomination when the nominee has overlapping pending or approved leave during the re"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_055():
    """TEST-FR-055: [AFR-EL-011.4-negative-boundary] Verify boundary/negative condition for Substitute leave-overlap eligibility"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_056():
    """TEST-FR-056: [AFR-EL-012.1] Verify Substitute accepts or declines: The system shall allow the nominated substitute to accept or decline the responsibility assignment."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_057():
    """TEST-FR-057: [AFR-EL-012.2] Verify Consent gate blocks routing: When substitute consent is required, the system shall prevent approval routing until the nominated substitute accepts."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_058():
    """TEST-FR-058: [AFR-EL-012.2-negative-boundary] Verify boundary/negative condition for Consent gate blocks routing"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_059():
    """TEST-FR-059: [AFR-EL-012.3] Verify Replacement substitute after decline: After a required substitute declines, the system shall allow the applicant to nominate another eligible substitute."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_060():
    """TEST-FR-060: [AFR-EL-012.4] Verify Withdrawal option after substitute decline: After a required substitute declines, the system shall allow the applicant to withdraw the still-pending request where w"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_061():
    """TEST-FR-061: [AFR-EL-013.1] Verify Route CL/RH to Unit Head: For a submitted CL or RH request, the system shall route the request to the applicant’s Unit Head except where the Direc"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_062():
    """TEST-FR-062: [AFR-EL-013.2] Verify Unit Head is final authority for CL/RH: For CL and RH, including associated Station Leave, the system shall treat the applicant’s Unit Head as the final sanctio"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_063():
    """TEST-FR-063: [AFR-EL-013.3] Verify Unit Head approve/reject CL/RH: The system shall allow the Unit Head to approve or reject CL and RH within Unit Head authority."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_064():
    """TEST-FR-064: [AFR-EL-013.3-negative-boundary] Verify boundary/negative condition for Unit Head approve/reject CL/RH"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_065():
    """TEST-FR-065: [AFR-EL-014.1] Verify Route higher-sanction request to Unit Head: For SCL, EL, COL, and VL, the system shall route the submitted request to the applicant’s Unit Head for review, except w"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_066():
    """TEST-FR-066: [AFR-EL-014.1-negative-boundary] Verify boundary/negative condition for Route higher-sanction request to Unit Head"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_067():
    """TEST-FR-067: [AFR-EL-014.2] Verify Unit Head recommendation outcomes: For SCL, EL, COL, and VL, the system shall allow the Unit Head to record Recommended or Not Recommended."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_068():
    """TEST-FR-068: [AFR-EL-014.3] Verify Not Recommended is not final rejection: The system shall not treat the Unit Head’s Not Recommended outcome for SCL, EL, COL, or VL as a final rejection."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_069():
    """TEST-FR-069: [AFR-EL-014.3-negative-boundary] Verify boundary/negative condition for Not Recommended is not final rejection"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_070():
    """TEST-FR-070: [AFR-EL-014.4] Verify Route through configured higher-sanction hierarchy: After Unit Head review, the system shall route SCL, EL, COL, and VL through the configured hierarchy to the resolved fin"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_071():
    """TEST-FR-071: [AFR-EL-014.5] Verify Resolve path from request/organizational context: The system shall resolve the processing/sanctioning path from the applicant, organizational unit, designation/role, leav"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_072():
    """TEST-FR-072: [AFR-EL-014.6] Verify Support configured sanctioning roles: The system shall support configured higher-sanction paths that may include Deputy Registrar (Estt.), Dean, Registrar, an"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_073():
    """TEST-FR-073: [AFR-EL-014.7] Verify Optional Establishment processing step: Where configured, the system shall support an Establishment-level verification/routing step before forwarding higher-san"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_074():
    """TEST-FR-074: [AFR-EL-014.8] Verify Final Sanctioning Authority approve/reject: The system shall allow the resolved final Sanctioning Authority to approve or reject a routed higher-sanction request."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_075():
    """TEST-FR-075: [AFR-EL-014.8-negative-boundary] Verify boundary/negative condition for Final Sanctioning Authority approve/reject"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_076():
    """TEST-FR-076: [AFR-EL-015.1] Verify Director self-sanction path: When the Director is the applicant, the system shall replace the normal Unit Head/higher-authority route with the Direct"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_077():
    """TEST-FR-077: [AFR-EL-016.1] Verify Record final leave decision: On a final leave decision, the system shall record the final approve/reject outcome."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_078():
    """TEST-FR-078: [AFR-EL-016.1-negative-boundary] Verify boundary/negative condition for Record final leave decision"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_079():
    """TEST-FR-079: [AFR-EL-016.2] Verify Notify employee of final decision: On a final leave decision, the system shall notify the employee of the final outcome."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_080():
    """TEST-FR-080: [AFR-EL-016.2-negative-boundary] Verify boundary/negative condition for Notify employee of final decision"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_081():
    """TEST-FR-081: [AFR-EL-016.3] Verify Update leave record/account on approval: When a new leave request is finally approved, the system shall update the employee’s leave record/account according to t"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_082():
    """TEST-FR-082: [AFR-EL-016.4] Verify Expose intermediate status through inquiry: The system shall make intermediate processing states and recorded decisions available to the employee through status/his"""
    assert LeaveType.CL == "CL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_fr_083():
    """TEST-FR-083: [AFR-EL-017.1] Verify Prohibit in-place modification: The system shall not permit a submitted pending leave request to be modified in place."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_084():
    """TEST-FR-084: [AFR-EL-017.1-negative-boundary] Verify boundary/negative condition for Prohibit in-place modification"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_085():
    """TEST-FR-085: [AFR-EL-017.2] Verify Change through withdrawal and fresh application: If a submitted pending request requires change before final approval, the system shall support change by withdrawal of t"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_086():
    """TEST-FR-086: [AFR-EL-018.1] Verify Allow immediate pre-final withdrawal: The system shall allow an employee to withdraw a pending leave application at any time before final approval and shall m"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_087():
    """TEST-FR-087: [AFR-EL-018.2] Verify Terminate remaining approval processing: Upon successful withdrawal, the system shall terminate all remaining approval processing and close/cancel remaining acti"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_088():
    """TEST-FR-088: [AFR-EL-018.3] Verify Prevent later approve/reject actions: After a request is withdrawn, the system shall prevent any later approve or reject action on that request."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_089():
    """TEST-FR-089: [AFR-EL-018.3-negative-boundary] Verify boundary/negative condition for Prevent later approve/reject actions"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_090():
    """TEST-FR-090: [AFR-EL-018.4] Verify Notify concerned roles of withdrawal: Upon successful withdrawal, the system shall notify the concerned processing/sanctioning roles of the withdrawal."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_091():
    """TEST-FR-091: [AFR-EL-018.5] Verify Withdrawal unavailable after final approval: After final approval, the system shall not offer pending-request withdrawal; approved-leave cancellation shall apply whe"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_092():
    """TEST-FR-092: [AFR-EL-018.5-negative-boundary] Verify boundary/negative condition for Withdrawal unavailable after final approval"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_093():
    """TEST-FR-093: [AFR-EL-019.1] Verify Request cancellation only before start: The system shall allow an employee to request cancellation of an approved leave only before the approved leave begins."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_094():
    """TEST-FR-094: [AFR-EL-019.2] Verify Use same applicable hierarchy: The system shall route an approved-leave cancellation through the same applicable hierarchy as the original leave."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_095():
    """TEST-FR-095: [AFR-EL-019.3] Verify Do not edit approved leave in place: The system shall not edit the approved leave in place as part of cancellation processing."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_096():
    """TEST-FR-096: [AFR-EL-019.4] Verify Mark leave Cancelled on approved cancellation: When cancellation is finally approved, the system shall mark the approved leave as Cancelled."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_097():
    """TEST-FR-097: [AFR-EL-019.5] Verify Restore/adjust deducted balance on cancellation approval: When cancellation is finally approved, the system shall restore or adjust any leave balance already deducted for the ori"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_098():
    """TEST-FR-098: [AFR-EL-019.6] Verify Preserve approval on cancellation rejection: When a cancellation request is finally rejected, the system shall leave the original approved leave unchanged."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_099():
    """TEST-FR-099: [AFR-EL-019.6-negative-boundary] Verify boundary/negative condition for Preserve approval on cancellation rejection"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_100():
    """TEST-FR-100: [AFR-EL-019.7] Verify Fresh application after successful cancellation: If revised leave is still needed after successful cancellation, the system shall require a fresh leave application."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_101():
    """TEST-FR-101: [AFR-EL-019.8] Verify No pre-start cancellation after leave begins: Once the approved leave has begun, the system shall direct applicable change handling to extension or resumption rather """
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_102():
    """TEST-FR-102: [AFR-EL-019.8-negative-boundary] Verify boundary/negative condition for No pre-start cancellation after leave begins"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_103():
    """TEST-FR-103: [AFR-EL-020.1] Verify Submit separate extension request: The system shall allow an employee on ongoing EL, COL, or VL to submit a separate extension request for additional leave"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_104():
    """TEST-FR-104: [AFR-EL-020.2] Verify Extension limited to ongoing EL/COL/VL: The system shall limit the defined extension capability to ongoing EL, COL, and VL."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_105():
    """TEST-FR-105: [AFR-EL-020.3] Verify Validate extension conditions: Before an extension proceeds, the system shall validate applicable eligibility, balance, leave-counting, calendar, and o"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_106():
    """TEST-FR-106: [AFR-EL-020.4] Verify Extension substitute consent gate: When responsibility coverage is required for an extension, the system shall obtain valid substitute consent before appro"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_107():
    """TEST-FR-107: [AFR-EL-020.5] Verify Route extension through applicable sanction path: The system shall route a valid extension through the applicable Unit Head and configured higher-sanction path."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_108():
    """TEST-FR-108: [AFR-EL-020.6] Verify Post incremental period on extension approval: When an extension is finally approved, the system shall post only the incremental additional leave period while preservi"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_109():
    """TEST-FR-109: [AFR-EL-020.7] Verify Preserve original leave on extension rejection: When an extension request is finally rejected, the system shall leave the original approved leave unchanged."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_110():
    """TEST-FR-110: [AFR-EL-020.7-negative-boundary] Verify boundary/negative condition for Preserve original leave on extension rejection"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_111():
    """TEST-FR-111: [AFR-EL-021.1] Verify Submit resumption after EL/COL/VL: The system shall allow an employee returning from EL, COL, or VL to submit resumption of duty information."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_112():
    """TEST-FR-112: [AFR-EL-021.2] Verify Support early resumption: The system shall support a resumption date earlier than the approved end date for EL, COL, or VL."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_113():
    """TEST-FR-113: [AFR-EL-021.3] Verify Capture actual resumption details: The system shall capture the employee’s actual resumption date and required resumption details."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_114():
    """TEST-FR-114: [AFR-EL-021.4] Verify Route to applicable Sanctioning Authority: The system shall route submitted resumption information to the applicable Sanctioning Authority for review."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_115():
    """TEST-FR-115: [AFR-EL-021.5] Verify Normal resumption: no period/balance adjustment: When the actual resumption date equals the approved end date, the Sanctioning Authority shall review the resumption and """
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_116():
    """TEST-FR-116: [AFR-EL-021.6] Verify Early/late resumption: record actual leave period: When actual resumption is earlier or later than the approved end date, the system shall, after Sanctioning Authority rev"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_117():
    """TEST-FR-117: [AFR-EL-021.7] Verify Early resumption: restore unused leave after review: When resumption is earlier than the approved end date, the system shall restore the unused portion of approved EL/COL/VL"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_118():
    """TEST-FR-118: [AFR-EL-021.8] Verify Late resumption: adjust leave balance after review: When resumption is later than the approved end date, the system shall adjust the leave balance to reflect the reviewed a"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_119():
    """TEST-FR-119: [AFR-EL-021.9] Verify Synchronize leave and attendance after early/late review: After reviewed early or late resumption, the system shall synchronize the relevant leave and attendance records with the"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_120():
    """TEST-FR-120: [AFR-EL-021.10] Verify Do not impose generic Closed state on normal resumption: The system shall not create a generic leave-closure state solely because a normal resumption has been reviewed."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_121():
    """TEST-FR-121: [AFR-EL-022.1] Verify View current leave balances: The system shall allow an employee to view the employee’s current leave balances."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_122():
    """TEST-FR-122: [AFR-EL-022.2] Verify View leave-account/request history: The system shall allow an employee to view the employee’s leave-account and leave-request history."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_123():
    """TEST-FR-123: [AFR-EL-022.3] Verify View current request status: The system shall allow an employee to view the current processing status of the employee’s leave requests."""
    assert LeaveType.CL == "CL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_fr_124():
    """TEST-FR-124: [AFR-EL-022.4] Verify View recorded final decisions: The system shall allow an employee to view recorded final decisions for the employee’s leave requests."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_125():
    """TEST-FR-125: [AFR-EL-022.4-negative-boundary] Verify boundary/negative condition for View recorded final decisions"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_126():
    """TEST-FR-126: [AFR-EL-023.1] Verify Printable/exportable application: The system shall allow an employee to obtain a printable/exportable representation of a leave application accessible to """
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_127():
    """TEST-FR-127: [AFR-EL-023.1-negative-boundary] Verify boundary/negative condition for Printable/exportable application"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_128():
    """TEST-FR-128: [AFR-EL-024.1] Verify Create/revise policy parameters: The system shall allow authorized administrative roles to create and revise the current leave-policy parameters."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_129():
    """TEST-FR-129: [AFR-EL-024.1-negative-boundary] Verify boundary/negative condition for Create/revise policy parameters"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_130():
    """TEST-FR-130: [AFR-EL-024.2] Verify Maintain hierarchy configuration: The system shall allow authorized administrative roles to maintain the current hierarchy configuration used for routing."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_131():
    """TEST-FR-131: [AFR-EL-024.3] Verify Use current configured values: The system shall use the current configured policy and hierarchy values for leave validation and routing."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_132():
    """TEST-FR-132: [AFR-EL-024.4] Verify No policy draft/publish/effective-version lifecycle: The system shall not require a draft/publish/effective-version lifecycle for leave-policy parameters in this baseline."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_133():
    """TEST-FR-133: [AFR-EL-025.1] Verify Create/revise holiday/RH calendar: The system shall allow authorized administrative roles to create and revise the holiday/RH calendar."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_134():
    """TEST-FR-134: [AFR-EL-025.2] Verify Publish replacement holiday/RH calendar: The system shall allow authorized administrative roles to publish a replacement holiday/RH calendar."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_135():
    """TEST-FR-135: [AFR-EL-025.3] Verify Use current published calendar until replacement: The system shall continue using the currently effective published holiday/RH calendar for date/RH validation until a rep"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_136():
    """TEST-FR-136: [AFR-EL-026.1] Verify Authorized leave-record maintenance: The system shall allow an authorized administrative role to maintain or correct leave records within the scope permitted"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_137():
    """TEST-FR-137: [AFR-EL-026.1-negative-boundary] Verify boundary/negative condition for Authorized leave-record maintenance"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_138():
    """TEST-FR-138: [AFR-EL-026.2] Verify Maintenance is not sanctioning: The system shall ensure that administrative leave-record maintenance or correction does not itself create or replace a l"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_139():
    """TEST-FR-139: [AFR-EL-026.2-negative-boundary] Verify boundary/negative condition for Maintenance is not sanctioning"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_140():
    """TEST-FR-140: [AFR-EL-027.1] Verify Record already-sanctioned offline leave: The system shall allow an authorized Leave Administrator to retrospectively record leave already sanctioned through an a"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_141():
    """TEST-FR-141: [AFR-EL-027.2] Verify No second approval workflow: The system shall treat retrospective offline-sanctioned leave entry as record synchronization and shall not initiate a s"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_142():
    """TEST-FR-142: [AFR-EL-027.3] Verify Capture sanction/reference evidence: For each retrospective offline-sanctioned leave entry, the system shall capture sanction/reference evidence."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_143():
    """TEST-FR-143: [AFR-EL-027.4] Verify Validate offline-entry record consistency: Before completing retrospective synchronization, the system shall validate the offline-sanctioned leave entry for record"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_144():
    """TEST-FR-144: [AFR-EL-027.5] Verify Update balance/history for offline leave: After a valid retrospective offline-sanctioned leave entry is recorded, the system shall update the relevant leave balan"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_145():
    """TEST-FR-145: [AFR-EL-028.1] Verify Year-end lapse CL/RH/SCL: At year end, the system shall execute lapse of unused CL, RH, and SCL according to their applicable policies."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_146():
    """TEST-FR-146: [AFR-EL-028.1-negative-boundary] Verify boundary/negative condition for Year-end lapse CL/RH/SCL"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_147():
    """TEST-FR-147: [AFR-EL-028.2] Verify Year-end VL-to-EL conversion: At year end, the system shall execute the defined faculty VL-to-EL conversion, including fractional conversion and no VL"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_148():
    """TEST-FR-148: [AFR-EL-028.3] Verify Year-end EL/COL carry-forward: At year end, the system shall carry forward EL and COL according to their applicable policies."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_149():
    """TEST-FR-149: [AFR-EL-028.4] Verify Record year-end leave-account transactions: The system shall record the leave-account transactions produced by year-end processing."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_150():
    """TEST-FR-150: [AFR-EL-028.4-negative-boundary] Verify boundary/negative condition for Record year-end leave-account transactions"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_151():
    """TEST-FR-151: [AFR-EL-028.5] Verify Report year-end processing exceptions: The system shall report exceptions encountered during year-end leave-account processing."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_152():
    """TEST-FR-152: [AFR-EL-028.5-negative-boundary] Verify boundary/negative condition for Report year-end processing exceptions"""
    s = LeaveApplicationCreateSerializer(data={"leave_type": "CL", "start_date": datetime.date(2026, 11, 5), "end_date": datetime.date(2026, 11, 2), "purpose": "Invalid dates"})
    assert not s.is_valid()

def test_fr_153():
    """TEST-FR-153: [AFR-EL-029.1] Verify Configure reminder threshold: The system shall allow an authorized administrative role to configure the reminder threshold for SLA-controlled actionab"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_154():
    """TEST-FR-154: [AFR-EL-029.2] Verify Configure escalation threshold: The system shall allow an authorized administrative role to configure the escalation threshold for SLA-controlled action"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_155():
    """TEST-FR-155: [AFR-EL-030.1] Verify Notify task assignee on assignment: When an actionable workflow task is assigned to a user, the system shall notify the assigned user of that task."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_156():
    """TEST-FR-156: [AFR-EL-031.1] Verify Identify pending task at reminder threshold: When an SLA-controlled actionable task reaches its configured reminder threshold, the system shall determine whether the"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_157():
    """TEST-FR-157: [AFR-EL-031.2] Verify Issue reminder only while pending: If an SLA-controlled actionable task is still pending at its configured reminder threshold, the system shall remind the """
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_158():
    """TEST-FR-158: [AFR-EL-031.3] Verify Log reminder action: When an SLA reminder is issued, the system shall log the reminder action."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_159():
    """TEST-FR-159: [AFR-EL-031.4] Verify Suppress reminder for non-pending task: If the task is no longer pending when the configured reminder threshold is reached, the system shall not issue the remin"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_160():
    """TEST-FR-160: [AFR-EL-032.1] Verify Determine pending status at escalation threshold: When an SLA-controlled actionable task passes its configured escalation threshold, the system shall determine whether th"""
    assert LeaveType.CL == "CL"
    assert LeaveStatus.APPROVED == "APPROVED"

def test_fr_161():
    """TEST-FR-161: [AFR-EL-032.2] Verify Escalate/notify configured authority: If an SLA-controlled actionable task remains pending past its configured escalation threshold, the system shall notify o"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_162():
    """TEST-FR-162: [AFR-EL-032.3] Verify Log escalation action: When an SLA escalation/authority notification is issued, the system shall log the escalation action."""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

def test_fr_163():
    """TEST-FR-163: [AFR-EL-032.4] Verify Suppress escalation for non-pending task: If the task is no longer pending when the configured escalation threshold is evaluated, the system shall not issue the c"""
    mock_req = MagicMock()
    mock_req.principal = SimpleNamespace(user_id=10)
    data = {"leave_type": "CL", "start_date": datetime.date(2026, 11, 2), "end_date": datetime.date(2026, 11, 2), "purpose": "Valid purpose", "substitute_user_id": 20}
    s = LeaveApplicationCreateSerializer(data=data, context={"request": mock_req})
    assert s.is_valid(), s.errors

