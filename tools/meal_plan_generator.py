import ollama
from models.user_profile import UserProfile


DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

SYSTEM_PROMPT = """You are a professional nutritionist. Your job is to create precise,
realistic 7-day meal plans. Always respond with ONLY the meal plan in the exact format
requested — no extra commentary, no explanations before or after."""


def _build_prompt(profile: UserProfile, target_calories: int, macros: dict) -> str:
    goal_label = profile.goal.replace("_", " ")
    return f"""Create a 7-day meal plan for the following person:
- Goal: {goal_label}
- Daily calorie target: {target_calories} kcal
- Daily protein target: {macros['protein_g']} g
- Daily carbs target: {macros['carbs_g']} g
- Daily fat target: {macros['fat_g']} g

Rules:
- Each day must have: Breakfast, Lunch, Dinner, and Snack
- Each meal must show: food items and approximate calories
- The total daily calories must be close to {target_calories} kcal
- Protein-rich foods for muscle gain, lower-carb for weight loss, balanced for maintenance
- Use simple, realistic, everyday foods

Format each day exactly like this:

Monday:
  Breakfast (Xcal): [food items]
  Lunch (Xcal): [food items]
  Dinner (Xcal): [food items]
  Snack (Xcal): [food items]
  Daily total: Xcal | P: Xg | C: Xg | F: Xg

Repeat for all 7 days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday."""


def _parse_response(raw: str) -> dict:
    """Convert LLM text output into a structured dict keyed by day name."""
    plan = {}
    current_day = None
    meals = {}

    for line in raw.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        # Detect day header (e.g. "Monday:" or "**Monday**:")
        cleaned = stripped.replace("**", "").rstrip(":")
        if cleaned in DAYS:
            if current_day and meals:
                plan[current_day] = meals
            current_day = cleaned
            meals = {}
            continue

        if current_day is None:
            continue

        lower = stripped.lower()
        if lower.startswith("breakfast"):
            meals["breakfast"] = stripped
        elif lower.startswith("lunch"):
            meals["lunch"] = stripped
        elif lower.startswith("dinner"):
            meals["dinner"] = stripped
        elif lower.startswith("snack"):
            meals["snack"] = stripped
        elif lower.startswith("daily total"):
            meals["daily_total"] = stripped

    if current_day and meals:
        plan[current_day] = meals

    return plan


class MealPlanGenerator:
    """Tool: Uses a local Ollama LLM to generate a personalised 7-day meal plan."""

    def __init__(self, model: str = "llama3.2") -> None:
        self.model = model

    def generate(self, profile: UserProfile, target_calories: int, macros: dict) -> dict:
        prompt = _build_prompt(profile, target_calories, macros)

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user",   "content": prompt},
            ],
        )

        raw_text = response["message"]["content"]
        structured = _parse_response(raw_text)

        return {
            "model_used": self.model,
            "target_calories": target_calories,
            "target_macros": macros,
            "days": structured,
            "raw": raw_text,
        }
