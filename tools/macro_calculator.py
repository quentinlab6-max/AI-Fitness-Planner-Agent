from models.user_profile import UserProfile


class MacroCalculator:
    """Tool: Calculates macronutrient targets (protein, carbs, fat) based on goal."""

    # Ratio of calories from each macro per goal
    MACRO_RATIOS = {
        "weight_loss": {"protein": 0.35, "carbs": 0.40, "fat": 0.25},
        "muscle_gain": {"protein": 0.30, "carbs": 0.45, "fat": 0.25},
        "maintenance": {"protein": 0.25, "carbs": 0.50, "fat": 0.25},
    }

    KCAL_PER_GRAM = {"protein": 4, "carbs": 4, "fat": 9}

    def calculate(self, profile: UserProfile, target_calories: int) -> dict:
        ratios = self.MACRO_RATIOS[profile.goal]

        protein_g = (target_calories * ratios["protein"]) / self.KCAL_PER_GRAM["protein"]
        carbs_g   = (target_calories * ratios["carbs"])   / self.KCAL_PER_GRAM["carbs"]
        fat_g     = (target_calories * ratios["fat"])     / self.KCAL_PER_GRAM["fat"]

        return {
            "protein_g":   round(protein_g),
            "carbs_g":     round(carbs_g),
            "fat_g":       round(fat_g),
            "protein_pct": round(ratios["protein"] * 100),
            "carbs_pct":   round(ratios["carbs"]   * 100),
            "fat_pct":     round(ratios["fat"]      * 100),
        }
