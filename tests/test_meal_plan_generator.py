"""
Tests for MealPlanGenerator.

The LLM call is mocked so tests run offline and deterministically.
"""
from unittest.mock import MagicMock, patch
import pytest
from models.user_profile import UserProfile
from tools.meal_plan_generator import MealPlanGenerator, _parse_response, _build_prompt


@pytest.fixture
def profile():
    return UserProfile(
        name="Test", age=25, weight_kg=70, height_cm=175,
        gender="male", activity_level="moderate",
        goal="muscle_gain", experience_level="intermediate",
    )


@pytest.fixture
def macros():
    return {"protein_g": 180, "carbs_g": 270, "fat_g": 67,
            "protein_pct": 30, "carbs_pct": 45, "fat_pct": 25}


# ---------------------------------------------------------------------------
# Unit tests for helper functions (no LLM needed)
# ---------------------------------------------------------------------------

def test_build_prompt_contains_calories(profile, macros):
    prompt = _build_prompt(profile, 2400, macros)
    assert "2400" in prompt


def test_build_prompt_contains_macros(profile, macros):
    prompt = _build_prompt(profile, 2400, macros)
    assert "180" in prompt  # protein_g
    assert "270" in prompt  # carbs_g


def test_build_prompt_contains_goal(profile, macros):
    prompt = _build_prompt(profile, 2400, macros)
    assert "muscle gain" in prompt.lower()


SAMPLE_LLM_OUTPUT = """
Monday:
  Breakfast (450cal): Oatmeal with banana and peanut butter
  Lunch (650cal): Grilled chicken breast, brown rice, broccoli
  Dinner (700cal): Salmon, sweet potato, green beans
  Snack (200cal): Greek yogurt with honey
  Daily total: 2000cal | P: 150g | C: 220g | F: 55g

Tuesday:
  Breakfast (420cal): Scrambled eggs, whole wheat toast, orange juice
  Lunch (680cal): Turkey wrap, mixed salad, apple
  Dinner (720cal): Beef stir fry with vegetables and noodles
  Snack (180cal): Protein shake with milk
  Daily total: 2000cal | P: 155g | C: 215g | F: 58g
"""


def test_parse_response_finds_monday():
    result = _parse_response(SAMPLE_LLM_OUTPUT)
    assert "Monday" in result


def test_parse_response_finds_tuesday():
    result = _parse_response(SAMPLE_LLM_OUTPUT)
    assert "Tuesday" in result


def test_parse_response_extracts_breakfast():
    result = _parse_response(SAMPLE_LLM_OUTPUT)
    assert "breakfast" in result["Monday"]


def test_parse_response_extracts_all_meals():
    result = _parse_response(SAMPLE_LLM_OUTPUT)
    for meal in ("breakfast", "lunch", "dinner", "snack"):
        assert meal in result["Monday"]


def test_parse_response_extracts_daily_total():
    result = _parse_response(SAMPLE_LLM_OUTPUT)
    assert "daily_total" in result["Monday"]


# ---------------------------------------------------------------------------
# Integration test with mocked Ollama call
# ---------------------------------------------------------------------------

def test_generate_calls_ollama_and_returns_structure(profile, macros):
    mock_response = {
        "message": {"content": SAMPLE_LLM_OUTPUT}
    }

    with patch("tools.meal_plan_generator.ollama.chat", return_value=mock_response):
        gen = MealPlanGenerator(model="llama3.2")
        result = gen.generate(profile, 2400, macros)

    assert result["model_used"] == "llama3.2"
    assert result["target_calories"] == 2400
    assert "days" in result
    assert "Monday" in result["days"]


def test_generate_passes_correct_model(profile, macros):
    mock_response = {"message": {"content": SAMPLE_LLM_OUTPUT}}

    with patch("tools.meal_plan_generator.ollama.chat", return_value=mock_response) as mock_chat:
        MealPlanGenerator(model="mistral").generate(profile, 2000, macros)

    called_model = mock_chat.call_args[1]["model"]
    assert called_model == "mistral"


# ---------------------------------------------------------------------------
# Error handling tests
# ---------------------------------------------------------------------------

def test_ollama_connection_error_returns_error_key(profile, macros):
    with patch("tools.meal_plan_generator.ollama.chat", side_effect=Exception("Connection refused")):
        gen = MealPlanGenerator(model="llama3.2")
        result = gen.generate(profile, 2000, macros)

    assert "error" in result
    assert "Ollama" in result["error"]


def test_ollama_connection_error_returns_empty_days(profile, macros):
    with patch("tools.meal_plan_generator.ollama.chat", side_effect=Exception("Connection refused")):
        result = MealPlanGenerator().generate(profile, 2000, macros)

    assert result["days"] == {}


def test_ollama_connection_error_still_returns_metadata(profile, macros):
    with patch("tools.meal_plan_generator.ollama.chat", side_effect=Exception("timeout")):
        result = MealPlanGenerator(model="llama3.2").generate(profile, 1800, macros)

    assert result["model_used"] == "llama3.2"
    assert result["target_calories"] == 1800


def test_parse_empty_string_returns_empty_dict():
    assert _parse_response("") == {}


def test_parse_malformed_response_returns_partial_result():
    malformed = "Monday:\n  Breakfast (400cal): Oats\n  some random line\n"
    result = _parse_response(malformed)
    assert "Monday" in result
    assert "breakfast" in result["Monday"]
