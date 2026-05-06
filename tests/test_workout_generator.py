import pytest
from models.user_profile import UserProfile
from tools.workout_generator import WorkoutGenerator

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


@pytest.fixture
def gen():
    return WorkoutGenerator()


def _profile(goal: str, experience: str) -> UserProfile:
    return UserProfile(
        name="Test", age=25, weight_kg=70, height_cm=175,
        gender="male", activity_level="moderate",
        goal=goal, experience_level=experience,
    )


@pytest.mark.parametrize("goal,experience", [
    ("weight_loss",  "beginner"),
    ("weight_loss",  "intermediate"),
    ("weight_loss",  "advanced"),
    ("muscle_gain",  "beginner"),
    ("muscle_gain",  "intermediate"),
    ("muscle_gain",  "advanced"),
    ("maintenance",  "beginner"),
    ("maintenance",  "intermediate"),
    ("maintenance",  "advanced"),
])
def test_schedule_has_all_seven_days(gen, goal, experience):
    result = gen.generate(_profile(goal, experience))
    assert set(result["schedule"].keys()) == set(DAYS)


@pytest.mark.parametrize("goal,experience,expected_active", [
    ("weight_loss", "beginner",      3),
    ("weight_loss", "intermediate",  4),
    ("weight_loss", "advanced",      5),
    ("muscle_gain", "beginner",      3),
    ("muscle_gain", "intermediate",  4),
    ("muscle_gain", "advanced",      5),
    ("maintenance", "beginner",      3),
    ("maintenance", "intermediate",  4),
    ("maintenance", "advanced",      5),
])
def test_active_days_count(gen, goal, experience, expected_active):
    result = gen.generate(_profile(goal, experience))
    active = sum(1 for d in result["schedule"].values() if d["type"] != "Rest")
    assert active == expected_active


def test_exercises_have_required_keys(gen):
    result = gen.generate(_profile("muscle_gain", "intermediate"))
    for details in result["schedule"].values():
        for ex in details["exercises"]:
            assert "name" in ex
            assert "sets" in ex
            assert "reps" in ex
            assert "rest" in ex


def test_rest_days_have_no_exercises(gen):
    result = gen.generate(_profile("weight_loss", "beginner"))
    for details in result["schedule"].values():
        if details["type"] == "Rest":
            assert details["exercises"] == []
            assert details["duration_min"] == 0


def test_result_contains_metadata(gen):
    result = gen.generate(_profile("maintenance", "advanced"))
    assert "goal" in result
    assert "experience_level" in result
    assert "days_per_week" in result
    assert "focus" in result
