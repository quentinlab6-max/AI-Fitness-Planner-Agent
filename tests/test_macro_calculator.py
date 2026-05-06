import pytest
from models.user_profile import UserProfile
from tools.macro_calculator import MacroCalculator


@pytest.fixture
def calc():
    return MacroCalculator()


def _profile(goal: str) -> UserProfile:
    return UserProfile(
        name="Test", age=25, weight_kg=70, height_cm=175,
        gender="male", activity_level="moderate",
        goal=goal, experience_level="beginner",
    )


@pytest.mark.parametrize("goal,calories", [
    ("weight_loss", 2000),
    ("muscle_gain", 2500),
    ("maintenance", 2200),
])
def test_percentages_sum_to_100(calc, goal, calories):
    result = calc.calculate(_profile(goal), calories)
    total = result["protein_pct"] + result["carbs_pct"] + result["fat_pct"]
    assert total == 100


def test_weight_loss_protein_grams(calc):
    # weight_loss: protein=35%, 2000 kcal → 2000*0.35/4 = 175 g
    result = calc.calculate(_profile("weight_loss"), 2000)
    assert result["protein_g"] == 175


def test_muscle_gain_carb_grams(calc):
    # muscle_gain: carbs=45%, 2000 kcal → 2000*0.45/4 = 225 g
    result = calc.calculate(_profile("muscle_gain"), 2000)
    assert result["carbs_g"] == 225


def test_macros_cover_calories_within_5_percent(calc):
    target = 2400
    result = calc.calculate(_profile("muscle_gain"), target)
    total_kcal = result["protein_g"] * 4 + result["carbs_g"] * 4 + result["fat_g"] * 9
    assert abs(total_kcal - target) / target < 0.05


def test_all_macro_grams_are_positive(calc):
    result = calc.calculate(_profile("maintenance"), 2000)
    assert result["protein_g"] > 0
    assert result["carbs_g"] > 0
    assert result["fat_g"] > 0


def test_weight_loss_highest_protein_ratio(calc):
    wl = calc.calculate(_profile("weight_loss"), 2000)
    mg = calc.calculate(_profile("muscle_gain"), 2000)
    mn = calc.calculate(_profile("maintenance"), 2000)
    assert wl["protein_pct"] >= mg["protein_pct"]
    assert wl["protein_pct"] >= mn["protein_pct"]
