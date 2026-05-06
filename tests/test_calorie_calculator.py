import pytest
from models.user_profile import UserProfile
from tools.calorie_calculator import CalorieCalculator


@pytest.fixture
def calc():
    return CalorieCalculator()


@pytest.fixture
def male_profile():
    return UserProfile(
        name="Test", age=25, weight_kg=70.0, height_cm=175.0,
        gender="male", activity_level="sedentary",
        goal="maintenance", experience_level="beginner",
    )


@pytest.fixture
def female_profile():
    return UserProfile(
        name="Test", age=30, weight_kg=60.0, height_cm=165.0,
        gender="female", activity_level="moderate",
        goal="weight_loss", experience_level="intermediate",
    )


def test_male_bmr(calc, male_profile):
    # 10*70 + 6.25*175 - 5*25 + 5 = 1673.75 → 1674
    assert calc.calculate(male_profile)["bmr"] == 1674


def test_female_bmr(calc, female_profile):
    # 10*60 + 6.25*165 - 5*30 - 161 = 1320.25 → 1320
    assert calc.calculate(female_profile)["bmr"] == 1320


def test_sedentary_tdee(calc, male_profile):
    # bmr=1673.75 (unrounded) * 1.2 = 2008.5 → banker's rounding → 2008
    assert calc.calculate(male_profile)["tdee"] == 2008


def test_weight_loss_adjustment_is_minus_500(calc, male_profile):
    male_profile.goal = "weight_loss"
    result = calc.calculate(male_profile)
    assert result["adjustment_kcal"] == -500
    assert result["target_calories"] == result["tdee"] - 500


def test_muscle_gain_adjustment_is_plus_300(calc, male_profile):
    male_profile.goal = "muscle_gain"
    result = calc.calculate(male_profile)
    assert result["adjustment_kcal"] == 300
    assert result["target_calories"] == result["tdee"] + 300


def test_maintenance_no_adjustment(calc, male_profile):
    result = calc.calculate(male_profile)
    assert result["adjustment_kcal"] == 0
    assert result["target_calories"] == result["tdee"]


def test_higher_activity_means_higher_tdee(calc, male_profile):
    activities = ["sedentary", "light", "moderate", "active", "very_active"]
    tdees = []
    for level in activities:
        male_profile.activity_level = level
        tdees.append(calc.calculate(male_profile)["tdee"])
    assert tdees == sorted(tdees), "TDEE should increase with each activity level"


def test_target_calories_is_positive(calc, male_profile):
    male_profile.goal = "weight_loss"
    assert calc.calculate(male_profile)["target_calories"] > 0
