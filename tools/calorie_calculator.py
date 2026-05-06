from models.user_profile import UserProfile


class CalorieCalculator:
    """Tool: Calculates daily calorie needs using the Mifflin-St Jeor BMR formula."""

    ACTIVITY_MULTIPLIERS = {
        "sedentary":  1.2,
        "light":      1.375,
        "moderate":   1.55,
        "active":     1.725,
        "very_active": 1.9,
    }

    GOAL_ADJUSTMENTS = {
        "weight_loss": -500,
        "muscle_gain":  300,
        "maintenance":    0,
    }

    def calculate(self, profile: UserProfile) -> dict:
        if profile.gender == "male":
            bmr = 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age + 5
        else:
            bmr = 10 * profile.weight_kg + 6.25 * profile.height_cm - 5 * profile.age - 161

        multiplier = self.ACTIVITY_MULTIPLIERS[profile.activity_level]
        tdee = bmr * multiplier
        adjustment = self.GOAL_ADJUSTMENTS[profile.goal]
        target_calories = tdee + adjustment

        return {
            "bmr": round(bmr),
            "tdee": round(tdee),
            "target_calories": round(target_calories),
            "adjustment_kcal": adjustment,
        }
