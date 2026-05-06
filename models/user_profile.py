from dataclasses import dataclass
from typing import Literal


@dataclass
class UserProfile:
    name: str
    age: int
    weight_kg: float
    height_cm: float
    gender: Literal["male", "female"]
    activity_level: Literal["sedentary", "light", "moderate", "active", "very_active"]
    goal: Literal["weight_loss", "muscle_gain", "maintenance"]
    experience_level: Literal["beginner", "intermediate", "advanced"]
