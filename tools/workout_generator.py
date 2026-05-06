from typing import Any, Dict, List
from models.user_profile import UserProfile


def _ex(name: str, sets: int, reps: str, rest: str) -> Dict[str, Any]:
    return {"name": name, "sets": sets, "reps": reps, "rest": rest}


def _rest() -> Dict[str, Any]:
    return {
        "type": "Rest",
        "duration_min": 0,
        "exercises": [],
        "notes": "Active recovery — light walk or stretching if desired.",
    }


# ---------------------------------------------------------------------------
# Workout plans indexed by [goal][experience_level]
# ---------------------------------------------------------------------------
PLANS: Dict[str, Dict[str, Any]] = {
    # -----------------------------------------------------------------------
    "weight_loss": {
        "beginner": {
            "days_per_week": 3,
            "focus": "Full-body circuits with cardio",
            "schedule": {
                "Monday": {
                    "type": "Full Body Circuit",
                    "duration_min": 30,
                    "exercises": [
                        _ex("Jumping Jacks",      3, "30 s",    "15 s"),
                        _ex("Bodyweight Squats",  3, "15",      "30 s"),
                        _ex("Push-ups",           3, "10",      "30 s"),
                        _ex("Mountain Climbers",  3, "20 s",    "15 s"),
                        _ex("Plank",              3, "30 s",    "30 s"),
                    ],
                    "notes": "Keep rest short to maintain elevated heart rate.",
                },
                "Tuesday": _rest(),
                "Wednesday": {
                    "type": "Cardio + Core",
                    "duration_min": 30,
                    "exercises": [
                        _ex("Brisk Walk / Light Jog", 1, "20 min",   "—"),
                        _ex("Bicycle Crunches",        3, "15 each",  "30 s"),
                        _ex("Leg Raises",              3, "12",       "30 s"),
                        _ex("Side Plank",              2, "20 s each","20 s"),
                    ],
                    "notes": "Focus on steady pace during cardio.",
                },
                "Thursday": _rest(),
                "Friday": {
                    "type": "Full Body Circuit B",
                    "duration_min": 35,
                    "exercises": [
                        _ex("Burpees",          3, "10",      "30 s"),
                        _ex("Reverse Lunges",   3, "12 each", "30 s"),
                        _ex("Chair Dips",       3, "12",      "30 s"),
                        _ex("High Knees",       3, "30 s",    "15 s"),
                        _ex("Dead Bug",         3, "10",      "30 s"),
                    ],
                    "notes": "Progress by reducing rest time each week.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
        "intermediate": {
            "days_per_week": 4,
            "focus": "Upper/Lower split with cardio finishers",
            "schedule": {
                "Monday": {
                    "type": "Upper Body + Cardio",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Push-ups",          4, "15",     "45 s"),
                        _ex("Dumbbell Rows",     4, "12",     "45 s"),
                        _ex("Dumbbell Press",    3, "12",     "45 s"),
                        _ex("Lateral Raises",    3, "15",     "45 s"),
                        _ex("Jump Rope / HIIT",  1, "10 min", "—"),
                    ],
                    "notes": "Finish with 10 min high-intensity cardio.",
                },
                "Tuesday": {
                    "type": "Lower Body + Cardio",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Goblet Squats",       4, "15",     "45 s"),
                        _ex("Romanian Deadlift",   4, "12",     "60 s"),
                        _ex("Walking Lunges",      3, "12 each","45 s"),
                        _ex("Glute Bridges",       3, "20",     "30 s"),
                        _ex("Stair Climber",       1, "10 min", "—"),
                    ],
                    "notes": "Drive through heels on all lower-body movements.",
                },
                "Wednesday": _rest(),
                "Thursday": {
                    "type": "Upper Body + Cardio",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Incline Push-ups",    4, "15",     "45 s"),
                        _ex("Dumbbell Curls",      3, "15",     "45 s"),
                        _ex("Tricep Pushdowns",    3, "15",     "45 s"),
                        _ex("Face Pulls",          3, "15",     "45 s"),
                        _ex("Cycling / Rowing",    1, "10 min", "—"),
                    ],
                    "notes": "Controlled tempo on all upper-body movements.",
                },
                "Friday": {
                    "type": "Lower Body + Cardio",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Sumo Squats",           4, "15",     "45 s"),
                        _ex("Single-Leg Deadlift",   3, "10 each","60 s"),
                        _ex("Step-ups",              3, "12 each","45 s"),
                        _ex("Calf Raises",           4, "20",     "30 s"),
                        _ex("Sprint Intervals",      1, "10 min", "—"),
                    ],
                    "notes": "Sprint intervals at 80–90 % max effort.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
        "advanced": {
            "days_per_week": 5,
            "focus": "HIIT + Strength hybrid",
            "schedule": {
                "Monday": {
                    "type": "HIIT",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Box Jumps",         4, "10",    "30 s"),
                        _ex("Kettlebell Swings", 4, "15",    "30 s"),
                        _ex("Battle Ropes",      4, "30 s",  "30 s"),
                        _ex("Tuck Jumps",        4, "10",    "30 s"),
                        _ex("Sprint x Walk",     5, "200 m", "60 s"),
                    ],
                    "notes": "All intervals at 85–95 % max effort.",
                },
                "Tuesday": {
                    "type": "Upper Body Strength",
                    "duration_min": 50,
                    "exercises": [
                        _ex("Barbell Bench Press", 4, "8–10", "90 s"),
                        _ex("Weighted Pull-ups",   4, "8",    "90 s"),
                        _ex("Overhead Press",      3, "10",   "90 s"),
                        _ex("Cable Rows",          3, "12",   "60 s"),
                        _ex("Dumbbell Curls",      3, "12",   "60 s"),
                    ],
                    "notes": "Focus on progressive overload week to week.",
                },
                "Wednesday": {
                    "type": "Lower Body Strength",
                    "duration_min": 50,
                    "exercises": [
                        _ex("Barbell Back Squat",      4, "8–10",   "120 s"),
                        _ex("Romanian Deadlift",       4, "10",     "90 s"),
                        _ex("Leg Press",               3, "12",     "60 s"),
                        _ex("Bulgarian Split Squat",   3, "10 each","60 s"),
                        _ex("Calf Raises (weighted)",  4, "20",     "30 s"),
                    ],
                    "notes": "Strict form under heavy load.",
                },
                "Thursday": {
                    "type": "HIIT + Core",
                    "duration_min": 40,
                    "exercises": [
                        _ex("Rowing Machine",     1, "2000 m", "—"),
                        _ex("Assault Bike",       4, "30 s",   "30 s"),
                        _ex("Hanging Leg Raises", 4, "12",     "45 s"),
                        _ex("Ab Wheel Rollout",   3, "12",     "45 s"),
                        _ex("Pallof Press",       3, "12 each","45 s"),
                    ],
                    "notes": "Core engaged throughout all movements.",
                },
                "Friday": {
                    "type": "Full Body Conditioning",
                    "duration_min": 50,
                    "exercises": [
                        _ex("Deadlift",         4, "5",    "120 s"),
                        _ex("Weighted Push-ups",4, "15",   "60 s"),
                        _ex("Goblet Squats",    4, "15",   "60 s"),
                        _ex("TRX Rows",         4, "15",   "60 s"),
                        _ex("Farmer's Carry",   4, "40 m", "60 s"),
                    ],
                    "notes": "Prioritise compound movements.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
    },
    # -----------------------------------------------------------------------
    "muscle_gain": {
        "beginner": {
            "days_per_week": 3,
            "focus": "Full-body strength training",
            "schedule": {
                "Monday": {
                    "type": "Full Body Strength A",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Goblet Squat",         3, "10", "90 s"),
                        _ex("Dumbbell Bench Press", 3, "10", "90 s"),
                        _ex("Dumbbell Row",         3, "10", "90 s"),
                        _ex("Overhead Press",       3, "10", "90 s"),
                        _ex("Plank",                3, "30 s","30 s"),
                    ],
                    "notes": "Learn movement patterns before adding weight.",
                },
                "Tuesday": _rest(),
                "Wednesday": {
                    "type": "Full Body Strength B",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Romanian Deadlift",       3, "10", "90 s"),
                        _ex("Incline Dumbbell Press",  3, "10", "90 s"),
                        _ex("Lat Pulldown",            3, "10", "90 s"),
                        _ex("Lateral Raises",          3, "12", "60 s"),
                        _ex("Glute Bridges",           3, "15", "30 s"),
                    ],
                    "notes": "Focus on mind-muscle connection.",
                },
                "Thursday": _rest(),
                "Friday": {
                    "type": "Full Body Strength A+",
                    "duration_min": 50,
                    "exercises": [
                        _ex("Goblet Squat",         4, "10", "90 s"),
                        _ex("Dumbbell Bench Press", 4, "10", "90 s"),
                        _ex("Dumbbell Row",         4, "10", "90 s"),
                        _ex("Overhead Press",       3, "10", "90 s"),
                        _ex("Dumbbell Curls",       2, "12", "60 s"),
                    ],
                    "notes": "Increase weight slightly from Monday if form allows.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
        "intermediate": {
            "days_per_week": 4,
            "focus": "Upper/Lower strength split",
            "schedule": {
                "Monday": {
                    "type": "Upper Body A",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Barbell Bench Press",    4, "8",  "120 s"),
                        _ex("Barbell Row",            4, "8",  "120 s"),
                        _ex("Overhead Press",         3, "10", "90 s"),
                        _ex("Lat Pulldown",           3, "10", "90 s"),
                        _ex("Dumbbell Curls",         3, "12", "60 s"),
                        _ex("Skull Crushers",         3, "12", "60 s"),
                    ],
                    "notes": "Progress bench and row load each week.",
                },
                "Tuesday": {
                    "type": "Lower Body A",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Barbell Back Squat", 4, "8",  "120 s"),
                        _ex("Romanian Deadlift",  4, "10", "90 s"),
                        _ex("Leg Press",          3, "12", "90 s"),
                        _ex("Leg Curl",           3, "12", "60 s"),
                        _ex("Calf Raises",        4, "15", "45 s"),
                    ],
                    "notes": "Drive squat weight up week to week.",
                },
                "Wednesday": _rest(),
                "Thursday": {
                    "type": "Upper Body B",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Incline Barbell Press",   4, "10", "90 s"),
                        _ex("Cable Row",               4, "10", "90 s"),
                        _ex("DB Shoulder Press",       3, "12", "90 s"),
                        _ex("Face Pulls",              3, "15", "60 s"),
                        _ex("Hammer Curls",            3, "12", "60 s"),
                        _ex("Tricep Pushdowns",        3, "12", "60 s"),
                    ],
                    "notes": "Focus on volume and muscle pump.",
                },
                "Friday": {
                    "type": "Lower Body B",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Conventional Deadlift",  4, "6",      "120 s"),
                        _ex("Front Squat",            3, "10",     "90 s"),
                        _ex("Walking Lunges",         3, "12 each","60 s"),
                        _ex("Leg Extension",          3, "15",     "60 s"),
                        _ex("Hip Thrust",             4, "12",     "60 s"),
                    ],
                    "notes": "Treat deadlift as a max-effort movement.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
        "advanced": {
            "days_per_week": 5,
            "focus": "Push / Pull / Legs split",
            "schedule": {
                "Monday": {
                    "type": "Push",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Barbell Bench Press",   5, "5",  "150 s"),
                        _ex("Incline DB Press",      4, "10", "90 s"),
                        _ex("Overhead Press",        4, "8",  "120 s"),
                        _ex("Cable Flyes",           3, "15", "60 s"),
                        _ex("Lateral Raises",        4, "15", "60 s"),
                        _ex("Tricep Pushdowns",      3, "12", "60 s"),
                    ],
                    "notes": "Heavy compound first, isolation last.",
                },
                "Tuesday": {
                    "type": "Pull",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Weighted Pull-ups",      5, "5",  "150 s"),
                        _ex("Barbell Row",            4, "8",  "120 s"),
                        _ex("Cable Row",              4, "10", "90 s"),
                        _ex("Face Pulls",             3, "20", "60 s"),
                        _ex("Incline DB Curls",       4, "12", "60 s"),
                        _ex("Hammer Curls",           3, "12", "60 s"),
                    ],
                    "notes": "Control the eccentric on every rep.",
                },
                "Wednesday": {
                    "type": "Legs",
                    "duration_min": 70,
                    "exercises": [
                        _ex("Barbell Back Squat",     5, "5",      "180 s"),
                        _ex("Romanian Deadlift",      4, "10",     "120 s"),
                        _ex("Leg Press",              4, "12",     "90 s"),
                        _ex("Bulgarian Split Squat",  3, "10 each","90 s"),
                        _ex("Leg Curl",               3, "12",     "60 s"),
                        _ex("Standing Calf Raises",   5, "15",     "45 s"),
                    ],
                    "notes": "Squat depth: thighs at least parallel to floor.",
                },
                "Thursday": {
                    "type": "Push (Volume)",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Incline Barbell Press",  4, "8",  "120 s"),
                        _ex("Dumbbell Bench Press",   4, "12", "90 s"),
                        _ex("Arnold Press",           4, "10", "90 s"),
                        _ex("Pec Deck",               3, "15", "60 s"),
                        _ex("Overhead Tricep Ext.",   3, "12", "60 s"),
                    ],
                    "notes": "Moderate load — focus on hypertrophy range.",
                },
                "Friday": {
                    "type": "Pull (Volume)",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Lat Pulldown",           4, "12",     "90 s"),
                        _ex("Single-Arm DB Row",      4, "12 each","60 s"),
                        _ex("Chest-Supported Row",    4, "12",     "60 s"),
                        _ex("Rear Delt Flyes",        3, "20",     "45 s"),
                        _ex("Preacher Curls",         4, "12",     "60 s"),
                    ],
                    "notes": "Peak contraction on all rowing movements.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
    },
    # -----------------------------------------------------------------------
    "maintenance": {
        "beginner": {
            "days_per_week": 3,
            "focus": "Balanced fitness — strength and cardio",
            "schedule": {
                "Monday": {
                    "type": "Full Body Strength",
                    "duration_min": 35,
                    "exercises": [
                        _ex("Bodyweight Squats", 3, "15",  "45 s"),
                        _ex("Push-ups",          3, "12",  "45 s"),
                        _ex("Dumbbell Row",      3, "12",  "45 s"),
                        _ex("Glute Bridges",     3, "15",  "30 s"),
                        _ex("Plank",             3, "30 s","30 s"),
                    ],
                    "notes": "Consistency matters more than intensity.",
                },
                "Tuesday": _rest(),
                "Wednesday": {
                    "type": "Cardio + Flexibility",
                    "duration_min": 35,
                    "exercises": [
                        _ex("Brisk Walk",          1, "20 min",   "—"),
                        _ex("Hip Flexor Stretch",  2, "30 s each","—"),
                        _ex("Hamstring Stretch",   2, "30 s each","—"),
                        _ex("Shoulder Circles",    2, "10 each",  "—"),
                        _ex("Foam Rolling",        1, "5 min",    "—"),
                    ],
                    "notes": "Focus on breathing and relaxation.",
                },
                "Thursday": _rest(),
                "Friday": {
                    "type": "Full Body Strength B",
                    "duration_min": 35,
                    "exercises": [
                        _ex("Reverse Lunges",   3, "12 each","45 s"),
                        _ex("Dumbbell Press",   3, "12",     "45 s"),
                        _ex("Lat Pulldown",     3, "12",     "45 s"),
                        _ex("Dumbbell Curls",   2, "12",     "45 s"),
                        _ex("Dead Bug",         3, "10",     "30 s"),
                    ],
                    "notes": "Finish with light stretching.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
        "intermediate": {
            "days_per_week": 4,
            "focus": "Strength + Cardio + Flexibility balance",
            "schedule": {
                "Monday": {
                    "type": "Strength",
                    "duration_min": 50,
                    "exercises": [
                        _ex("Barbell Squat",   4, "8",     "90 s"),
                        _ex("Bench Press",     4, "8",     "90 s"),
                        _ex("Pull-ups",        3, "8–10",  "90 s"),
                        _ex("Overhead Press",  3, "10",    "60 s"),
                        _ex("Core Circuit",    1, "5 min", "—"),
                    ],
                    "notes": "Submaximal effort — no need for max-out attempts.",
                },
                "Tuesday": {
                    "type": "Cardio + Mobility",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Cycling / Running",  1, "25 min", "—"),
                        _ex("Dynamic Stretching", 1, "10 min", "—"),
                        _ex("Yoga Flow",          1, "10 min", "—"),
                    ],
                    "notes": "Keep heart rate at 60–70 % max.",
                },
                "Wednesday": _rest(),
                "Thursday": {
                    "type": "Strength B",
                    "duration_min": 50,
                    "exercises": [
                        _ex("Romanian Deadlift", 4, "10",   "90 s"),
                        _ex("Incline Press",     4, "10",   "90 s"),
                        _ex("Cable Row",         3, "12",   "60 s"),
                        _ex("Dips",              3, "12",   "60 s"),
                        _ex("Farmer's Carry",    3, "30 m", "60 s"),
                    ],
                    "notes": "Alternate main lifts week to week for variety.",
                },
                "Friday": {
                    "type": "Cardio + Flexibility",
                    "duration_min": 45,
                    "exercises": [
                        _ex("Swimming / Rowing",   1, "25 min", "—"),
                        _ex("Static Stretching",   1, "15 min", "—"),
                        _ex("Breathing Exercises", 1, "5 min",  "—"),
                    ],
                    "notes": "Active recovery mindset — enjoy the movement.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
        "advanced": {
            "days_per_week": 5,
            "focus": "Periodised maintenance with athletic performance",
            "schedule": {
                "Monday": {
                    "type": "Upper Strength",
                    "duration_min": 55,
                    "exercises": [
                        _ex("Barbell Bench Press",  5, "5",  "120 s"),
                        _ex("Weighted Pull-ups",    5, "5",  "120 s"),
                        _ex("Overhead Press",       4, "8",  "90 s"),
                        _ex("Dumbbell Row",         4, "10", "90 s"),
                        _ex("Tricep/Bicep Superset",3, "12", "60 s"),
                    ],
                    "notes": "Submaximal — leave 2 reps in the tank.",
                },
                "Tuesday": {
                    "type": "Cardio",
                    "duration_min": 35,
                    "exercises": [
                        _ex("Zone 2 Run / Bike", 1, "30 min", "—"),
                        _ex("Dynamic Warm-down", 1, "5 min",  "—"),
                    ],
                    "notes": "Conversational pace — nose-breathing test.",
                },
                "Wednesday": {
                    "type": "Lower Strength",
                    "duration_min": 60,
                    "exercises": [
                        _ex("Barbell Squat",        5, "5",  "150 s"),
                        _ex("Conventional Deadlift",4, "5",  "150 s"),
                        _ex("Leg Press",            3, "12", "90 s"),
                        _ex("Nordic Curl",          3, "8",  "90 s"),
                        _ex("Calf Raises",          4, "15", "45 s"),
                    ],
                    "notes": "Track squat and deadlift numbers each week.",
                },
                "Thursday": {
                    "type": "Cardio + Core",
                    "duration_min": 40,
                    "exercises": [
                        _ex("Assault Bike / Swim",  1, "20 min", "—"),
                        _ex("Weighted Plank",       4, "30 s",   "30 s"),
                        _ex("Dragon Flag",          3, "8",      "60 s"),
                        _ex("L-Sit Progression",    3, "15 s",   "45 s"),
                    ],
                    "notes": "Core targets anti-rotation and anti-extension.",
                },
                "Friday": {
                    "type": "Full Body Athletic",
                    "duration_min": 55,
                    "exercises": [
                        _ex("Power Clean / Jump Squat", 4, "5",      "120 s"),
                        _ex("Dumbbell Bench",            3, "12",     "90 s"),
                        _ex("Single-Leg RDL",           3, "10 each","60 s"),
                        _ex("TRX Rows",                 3, "15",     "60 s"),
                        _ex("Med Ball Slams",            4, "10",     "45 s"),
                    ],
                    "notes": "Explosive movements first, then hypertrophy accessory work.",
                },
                "Saturday": _rest(),
                "Sunday":   _rest(),
            },
        },
    },
}


class WorkoutGenerator:
    """Tool: Generates a personalised weekly workout plan based on goal and experience level."""

    def generate(self, profile: UserProfile) -> dict:
        plan = PLANS[profile.goal][profile.experience_level]
        return {
            "goal": profile.goal,
            "experience_level": profile.experience_level,
            "days_per_week": plan["days_per_week"],
            "focus": plan["focus"],
            "schedule": plan["schedule"],
        }
