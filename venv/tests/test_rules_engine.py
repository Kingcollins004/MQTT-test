import pytest
from rules_engine import calculate_winter_supplement

def test_no_eligibility():
    input_data = {
        "id": "1",
        "numberOfChildren": 2,
        "familyComposition": "single",
        "familyUnitInPayForDecember": False
    }
    result = calculate_winter_supplement(input_data)
    assert result["isEligible"] == False
    assert result["supplementAmount"] == 0.0

def test_single_no_children():
    input_data = {
        "id": "2",
        "numberOfChildren": 0,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True
    }
    result = calculate_winter_supplement(input_data)
    assert result["isEligible"] == True
    assert result["baseAmount"] == 60.0
    assert result["supplementAmount"] == 60.0

def test_family_with_children():
    input_data = {
        "id": "3",
        "numberOfChildren": 3,
        "familyComposition": "couple",
        "familyUnitInPayForDecember": True
    }
    result = calculate_winter_supplement(input_data)
    assert result["isEligible"] == True
    assert result["baseAmount"] == 120.0
    assert result["childrenAmount"] == 60.0
    assert result["supplementAmount"] == 180.0
