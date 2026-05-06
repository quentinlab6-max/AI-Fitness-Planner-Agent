from models.user_profile import UserProfile
from tools.calorie_calculator import CalorieCalculator
from tools.macro_calculator import MacroCalculator
from tools.workout_generator import WorkoutGenerator
from tools.meal_plan_generator import MealPlanGenerator
from validation.input_validator import InputValidator


class FitnessAgent:
    """
    Orchestrates the fitness-planning pipeline.

    Tool call sequence
    ------------------
    1. InputValidator      — rejects invalid data before any computation
    2. CalorieCalculator   — BMR → TDEE → goal-adjusted target
    3. MacroCalculator     — requires target_calories from step 2
    4. WorkoutGenerator    — independent of nutrition results
    5. MealPlanGenerator   — local LLM generates a 7-day meal calendar
                             using target_calories and macros from steps 2–3
    """

    def __init__(self, ollama_model: str = "llama3.2") -> None:
        self.validator = InputValidator()
        self.tools = {
            "calorie_calculator":  CalorieCalculator(),
            "macro_calculator":    MacroCalculator(),
            "workout_generator":   WorkoutGenerator(),
            "meal_plan_generator": MealPlanGenerator(model=ollama_model),
        }

    def run(self, user_data: dict) -> dict:
        valid, errors = self.validator.validate(user_data)
        if not valid:
            return {"success": False, "errors": errors}

        profile = UserProfile(**user_data)

        calorie_result = self.tools["calorie_calculator"].calculate(profile)
        macro_result   = self.tools["macro_calculator"].calculate(
            profile, calorie_result["target_calories"]
        )
        workout_result = self.tools["workout_generator"].generate(profile)

        print("Generating your personalised meal plan with AI (this may take ~30 s)...")
        meal_plan_result = self.tools["meal_plan_generator"].generate(
            profile,
            calorie_result["target_calories"],
            macro_result,
        )

        return {
            "success":   True,
            "name":      profile.name,
            "goal":      profile.goal,
            "nutrition": {
                "calories": calorie_result,
                "macros":   macro_result,
            },
            "workout":   workout_result,
            "meal_plan": meal_plan_result,
        }
