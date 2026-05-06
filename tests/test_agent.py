import pytest
from agent.fitness_agent import FitnessAgent


@pytest.fixture
def agent():
    return FitnessAgent()


@pytest.fixture
def valid_user():
    return {
        "name":             "Bob",
        "age":              28,
        "weight_kg":        80.0,
        "height_cm":        180.0,
        "gender":           "male",
        "activity_level":   "active",
        "goal":             "muscle_gain",
        "experience_level": "intermediate",
    }


def test_success_flag_on_valid_input(agent, valid_user):
    result = agent.run(valid_user)
    assert result["success"] is True


def test_result_contains_user_name(agent, valid_user):
    result = agent.run(valid_user)
    assert result["name"] == "Bob"


def test_result_contains_nutrition(agent, valid_user):
    result = agent.run(valid_user)
    assert "nutrition" in result
    assert "calories" in result["nutrition"]
    assert "macros" in result["nutrition"]


def test_result_contains_workout_schedule(agent, valid_user):
    result = agent.run(valid_user)
    assert "workout" in result
    assert "schedule" in result["workout"]


def test_invalid_input_returns_failure(agent, valid_user):
    valid_user["age"] = 999
    result = agent.run(valid_user)
    assert result["success"] is False
    assert "errors" in result
    assert len(result["errors"]) > 0


def test_target_calories_positive(agent, valid_user):
    result = agent.run(valid_user)
    assert result["nutrition"]["calories"]["target_calories"] > 0


def test_macro_grams_all_positive(agent, valid_user):
    macros = agent.run(valid_user)["nutrition"]["macros"]
    assert macros["protein_g"] > 0
    assert macros["carbs_g"] > 0
    assert macros["fat_g"] > 0


def test_weight_loss_produces_calorie_deficit(agent, valid_user):
    valid_user["goal"] = "weight_loss"
    cal = agent.run(valid_user)["nutrition"]["calories"]
    assert cal["target_calories"] < cal["tdee"]


def test_muscle_gain_produces_calorie_surplus(agent, valid_user):
    cal = agent.run(valid_user)["nutrition"]["calories"]  # goal = muscle_gain
    assert cal["target_calories"] > cal["tdee"]


def test_maintenance_calories_equal_tdee(agent, valid_user):
    valid_user["goal"] = "maintenance"
    cal = agent.run(valid_user)["nutrition"]["calories"]
    assert cal["target_calories"] == cal["tdee"]


@pytest.mark.parametrize("goal", ["weight_loss", "muscle_gain", "maintenance"])
def test_all_goals_return_success(agent, valid_user, goal):
    valid_user["goal"] = goal
    result = agent.run(valid_user)
    assert result["success"] is True
    assert "workout" in result


@pytest.mark.parametrize("experience", ["beginner", "intermediate", "advanced"])
def test_all_experience_levels_return_success(agent, valid_user, experience):
    valid_user["experience_level"] = experience
    result = agent.run(valid_user)
    assert result["success"] is True
