from typing import List, Tuple


VALID_GENDERS = {"male", "female"}
VALID_ACTIVITY_LEVELS = {"sedentary", "light", "moderate", "active", "very_active"}
VALID_GOALS = {"weight_loss", "muscle_gain", "maintenance"}
VALID_EXPERIENCE_LEVELS = {"beginner", "intermediate", "advanced"}


class InputValidator:
    """Validates raw user input before it is passed to the agent."""

    def validate(self, data: dict) -> Tuple[bool, List[str]]:
        errors: List[str] = []

        age = data.get("age")
        if not isinstance(age, (int, float)) or not (10 <= age <= 100):
            errors.append("Age must be a number between 10 and 100.")

        weight = data.get("weight_kg")
        if not isinstance(weight, (int, float)) or not (30 <= weight <= 300):
            errors.append("Weight must be a number between 30 and 300 kg.")

        height = data.get("height_cm")
        if not isinstance(height, (int, float)) or not (100 <= height <= 250):
            errors.append("Height must be a number between 100 and 250 cm.")

        if data.get("gender") not in VALID_GENDERS:
            errors.append(f"Gender must be one of: {', '.join(sorted(VALID_GENDERS))}.")

        if data.get("activity_level") not in VALID_ACTIVITY_LEVELS:
            errors.append(
                f"Activity level must be one of: {', '.join(sorted(VALID_ACTIVITY_LEVELS))}."
            )

        if data.get("goal") not in VALID_GOALS:
            errors.append(f"Goal must be one of: {', '.join(sorted(VALID_GOALS))}.")

        if data.get("experience_level") not in VALID_EXPERIENCE_LEVELS:
            errors.append(
                f"Experience level must be one of: {', '.join(sorted(VALID_EXPERIENCE_LEVELS))}."
            )

        return len(errors) == 0, errors
