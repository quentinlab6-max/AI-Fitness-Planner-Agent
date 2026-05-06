import pytest
from validation.input_validator import InputValidator


@pytest.fixture
def validator():
    return InputValidator()


@pytest.fixture
def valid_data():
    return {
        "name":             "Alice",
        "age":              25,
        "weight_kg":        65.0,
        "height_cm":        170.0,
        "gender":           "female",
        "activity_level":   "moderate",
        "goal":             "weight_loss",
        "experience_level": "beginner",
    }


def test_valid_input_passes(validator, valid_data):
    ok, errors = validator.validate(valid_data)
    assert ok is True
    assert errors == []


def test_age_too_young(validator, valid_data):
    valid_data["age"] = 5
    ok, errors = validator.validate(valid_data)
    assert ok is False
    assert any("Age" in e for e in errors)


def test_age_too_old(validator, valid_data):
    valid_data["age"] = 150
    ok, errors = validator.validate(valid_data)
    assert ok is False


def test_age_string_fails(validator, valid_data):
    valid_data["age"] = "twenty"
    ok, errors = validator.validate(valid_data)
    assert ok is False


def test_weight_too_low(validator, valid_data):
    valid_data["weight_kg"] = 5
    ok, errors = validator.validate(valid_data)
    assert ok is False
    assert any("Weight" in e for e in errors)


def test_weight_too_high(validator, valid_data):
    valid_data["weight_kg"] = 400
    ok, errors = validator.validate(valid_data)
    assert ok is False


def test_height_too_low(validator, valid_data):
    valid_data["height_cm"] = 50
    ok, errors = validator.validate(valid_data)
    assert ok is False
    assert any("Height" in e for e in errors)


def test_invalid_gender(validator, valid_data):
    valid_data["gender"] = "other"
    ok, errors = validator.validate(valid_data)
    assert ok is False
    assert any("Gender" in e for e in errors)


def test_invalid_activity_level(validator, valid_data):
    valid_data["activity_level"] = "super_active"
    ok, errors = validator.validate(valid_data)
    assert ok is False


def test_invalid_goal(validator, valid_data):
    valid_data["goal"] = "bulk"
    ok, errors = validator.validate(valid_data)
    assert ok is False


def test_invalid_experience_level(validator, valid_data):
    valid_data["experience_level"] = "expert"
    ok, errors = validator.validate(valid_data)
    assert ok is False


def test_multiple_errors_accumulated(validator, valid_data):
    valid_data["age"] = -1
    valid_data["weight_kg"] = 5
    valid_data["gender"] = "alien"
    ok, errors = validator.validate(valid_data)
    assert ok is False
    assert len(errors) >= 3


def test_boundary_age_accepted(validator, valid_data):
    for age in [10, 100]:
        valid_data["age"] = age
        ok, _ = validator.validate(valid_data)
        assert ok is True
