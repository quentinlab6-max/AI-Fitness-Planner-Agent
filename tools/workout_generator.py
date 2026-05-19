from models.user_profile import UserProfile

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def _day(type_, dur, *exs):
    return {
        "type": type_, "duration_min": dur,
        "exercises": [{"name": n, "sets": s, "reps": r, "rest": t} for n, s, r, t in exs],
    }


def _rest():
    return {"type": "Rest", "duration_min": 0, "exercises": []}


_DATA = {
    "weight_loss": {
        "beginner": (3, "Full-body circuits with cardio", {
            "Monday":    _day("Full Body Circuit",   30, ("Jumping Jacks",3,"30 s","15 s"), ("Bodyweight Squats",3,"15","30 s"), ("Push-ups",3,"10","30 s"), ("Mountain Climbers",3,"20 s","15 s"), ("Plank",3,"30 s","30 s")),
            "Wednesday": _day("Cardio + Core",       30, ("Brisk Walk / Light Jog",1,"20 min","—"), ("Bicycle Crunches",3,"15 each","30 s"), ("Leg Raises",3,"12","30 s"), ("Side Plank",2,"20 s each","20 s")),
            "Friday":    _day("Full Body Circuit B", 35, ("Burpees",3,"10","30 s"), ("Reverse Lunges",3,"12 each","30 s"), ("Chair Dips",3,"12","30 s"), ("High Knees",3,"30 s","15 s"), ("Dead Bug",3,"10","30 s")),
        }),
        "intermediate": (4, "Upper/Lower split with cardio finishers", {
            "Monday":    _day("Upper Body + Cardio", 45, ("Push-ups",4,"15","45 s"), ("Dumbbell Rows",4,"12","45 s"), ("Dumbbell Press",3,"12","45 s"), ("Lateral Raises",3,"15","45 s"), ("Jump Rope / HIIT",1,"10 min","—")),
            "Tuesday":   _day("Lower Body + Cardio", 45, ("Goblet Squats",4,"15","45 s"), ("Romanian Deadlift",4,"12","60 s"), ("Walking Lunges",3,"12 each","45 s"), ("Glute Bridges",3,"20","30 s"), ("Stair Climber",1,"10 min","—")),
            "Thursday":  _day("Upper Body + Cardio", 45, ("Incline Push-ups",4,"15","45 s"), ("Dumbbell Curls",3,"15","45 s"), ("Tricep Pushdowns",3,"15","45 s"), ("Face Pulls",3,"15","45 s"), ("Cycling / Rowing",1,"10 min","—")),
            "Friday":    _day("Lower Body + Cardio", 45, ("Sumo Squats",4,"15","45 s"), ("Single-Leg Deadlift",3,"10 each","60 s"), ("Step-ups",3,"12 each","45 s"), ("Calf Raises",4,"20","30 s"), ("Sprint Intervals",1,"10 min","—")),
        }),
        "advanced": (5, "HIIT + Strength hybrid", {
            "Monday":    _day("HIIT",                45, ("Box Jumps",4,"10","30 s"), ("Kettlebell Swings",4,"15","30 s"), ("Battle Ropes",4,"30 s","30 s"), ("Tuck Jumps",4,"10","30 s"), ("Sprint x Walk",5,"200 m","60 s")),
            "Tuesday":   _day("Upper Body Strength", 50, ("Barbell Bench Press",4,"8-10","90 s"), ("Weighted Pull-ups",4,"8","90 s"), ("Overhead Press",3,"10","90 s"), ("Cable Rows",3,"12","60 s"), ("Dumbbell Curls",3,"12","60 s")),
            "Wednesday": _day("Lower Body Strength", 50, ("Barbell Back Squat",4,"8-10","120 s"), ("Romanian Deadlift",4,"10","90 s"), ("Leg Press",3,"12","60 s"), ("Bulgarian Split Squat",3,"10 each","60 s"), ("Calf Raises",4,"20","30 s")),
            "Thursday":  _day("HIIT + Core",         40, ("Rowing Machine",1,"2000 m","—"), ("Assault Bike",4,"30 s","30 s"), ("Hanging Leg Raises",4,"12","45 s"), ("Ab Wheel Rollout",3,"12","45 s"), ("Pallof Press",3,"12 each","45 s")),
            "Friday":    _day("Full Body Conditioning",50,("Deadlift",4,"5","120 s"), ("Weighted Push-ups",4,"15","60 s"), ("Goblet Squats",4,"15","60 s"), ("TRX Rows",4,"15","60 s"), ("Farmer's Carry",4,"40 m","60 s")),
        }),
    },
    "muscle_gain": {
        "beginner": (3, "Full-body strength training", {
            "Monday":    _day("Full Body Strength A",  45, ("Goblet Squat",3,"10","90 s"), ("Dumbbell Bench Press",3,"10","90 s"), ("Dumbbell Row",3,"10","90 s"), ("Overhead Press",3,"10","90 s"), ("Plank",3,"30 s","30 s")),
            "Wednesday": _day("Full Body Strength B",  45, ("Romanian Deadlift",3,"10","90 s"), ("Incline Dumbbell Press",3,"10","90 s"), ("Lat Pulldown",3,"10","90 s"), ("Lateral Raises",3,"12","60 s"), ("Glute Bridges",3,"15","30 s")),
            "Friday":    _day("Full Body Strength A+", 50, ("Goblet Squat",4,"10","90 s"), ("Dumbbell Bench Press",4,"10","90 s"), ("Dumbbell Row",4,"10","90 s"), ("Overhead Press",3,"10","90 s"), ("Dumbbell Curls",2,"12","60 s")),
        }),
        "intermediate": (4, "Upper/Lower strength split", {
            "Monday":    _day("Upper Body A", 60, ("Barbell Bench Press",4,"8","120 s"), ("Barbell Row",4,"8","120 s"), ("Overhead Press",3,"10","90 s"), ("Lat Pulldown",3,"10","90 s"), ("Dumbbell Curls",3,"12","60 s"), ("Skull Crushers",3,"12","60 s")),
            "Tuesday":   _day("Lower Body A", 60, ("Barbell Back Squat",4,"8","120 s"), ("Romanian Deadlift",4,"10","90 s"), ("Leg Press",3,"12","90 s"), ("Leg Curl",3,"12","60 s"), ("Calf Raises",4,"15","45 s")),
            "Thursday":  _day("Upper Body B", 60, ("Incline Barbell Press",4,"10","90 s"), ("Cable Row",4,"10","90 s"), ("DB Shoulder Press",3,"12","90 s"), ("Face Pulls",3,"15","60 s"), ("Hammer Curls",3,"12","60 s"), ("Tricep Pushdowns",3,"12","60 s")),
            "Friday":    _day("Lower Body B", 60, ("Conventional Deadlift",4,"6","120 s"), ("Front Squat",3,"10","90 s"), ("Walking Lunges",3,"12 each","60 s"), ("Leg Extension",3,"15","60 s"), ("Hip Thrust",4,"12","60 s")),
        }),
        "advanced": (5, "Push / Pull / Legs split", {
            "Monday":    _day("Push",          60, ("Barbell Bench Press",5,"5","150 s"), ("Incline DB Press",4,"10","90 s"), ("Overhead Press",4,"8","120 s"), ("Cable Flyes",3,"15","60 s"), ("Lateral Raises",4,"15","60 s"), ("Tricep Pushdowns",3,"12","60 s")),
            "Tuesday":   _day("Pull",          60, ("Weighted Pull-ups",5,"5","150 s"), ("Barbell Row",4,"8","120 s"), ("Cable Row",4,"10","90 s"), ("Face Pulls",3,"20","60 s"), ("Incline DB Curls",4,"12","60 s"), ("Hammer Curls",3,"12","60 s")),
            "Wednesday": _day("Legs",          70, ("Barbell Back Squat",5,"5","180 s"), ("Romanian Deadlift",4,"10","120 s"), ("Leg Press",4,"12","90 s"), ("Bulgarian Split Squat",3,"10 each","90 s"), ("Leg Curl",3,"12","60 s"), ("Standing Calf Raises",5,"15","45 s")),
            "Thursday":  _day("Push (Volume)", 60, ("Incline Barbell Press",4,"8","120 s"), ("Dumbbell Bench Press",4,"12","90 s"), ("Arnold Press",4,"10","90 s"), ("Pec Deck",3,"15","60 s"), ("Overhead Tricep Ext.",3,"12","60 s")),
            "Friday":    _day("Pull (Volume)", 60, ("Lat Pulldown",4,"12","90 s"), ("Single-Arm DB Row",4,"12 each","60 s"), ("Chest-Supported Row",4,"12","60 s"), ("Rear Delt Flyes",3,"20","45 s"), ("Preacher Curls",4,"12","60 s")),
        }),
    },
    "maintenance": {
        "beginner": (3, "Balanced fitness — strength and cardio", {
            "Monday":    _day("Full Body Strength",   35, ("Bodyweight Squats",3,"15","45 s"), ("Push-ups",3,"12","45 s"), ("Dumbbell Row",3,"12","45 s"), ("Glute Bridges",3,"15","30 s"), ("Plank",3,"30 s","30 s")),
            "Wednesday": _day("Cardio + Flexibility", 35, ("Brisk Walk",1,"20 min","—"), ("Hip Flexor Stretch",2,"30 s each","—"), ("Hamstring Stretch",2,"30 s each","—"), ("Shoulder Circles",2,"10 each","—"), ("Foam Rolling",1,"5 min","—")),
            "Friday":    _day("Full Body Strength B", 35, ("Reverse Lunges",3,"12 each","45 s"), ("Dumbbell Press",3,"12","45 s"), ("Lat Pulldown",3,"12","45 s"), ("Dumbbell Curls",2,"12","45 s"), ("Dead Bug",3,"10","30 s")),
        }),
        "intermediate": (4, "Strength + Cardio + Flexibility balance", {
            "Monday":    _day("Strength",             50, ("Barbell Squat",4,"8","90 s"), ("Bench Press",4,"8","90 s"), ("Pull-ups",3,"8-10","90 s"), ("Overhead Press",3,"10","60 s"), ("Core Circuit",1,"5 min","—")),
            "Tuesday":   _day("Cardio + Mobility",    45, ("Cycling / Running",1,"25 min","—"), ("Dynamic Stretching",1,"10 min","—"), ("Yoga Flow",1,"10 min","—")),
            "Thursday":  _day("Strength B",           50, ("Romanian Deadlift",4,"10","90 s"), ("Incline Press",4,"10","90 s"), ("Cable Row",3,"12","60 s"), ("Dips",3,"12","60 s"), ("Farmer's Carry",3,"30 m","60 s")),
            "Friday":    _day("Cardio + Flexibility", 45, ("Swimming / Rowing",1,"25 min","—"), ("Static Stretching",1,"15 min","—"), ("Breathing Exercises",1,"5 min","—")),
        }),
        "advanced": (5, "Periodised maintenance with athletic performance", {
            "Monday":    _day("Upper Strength",     55, ("Barbell Bench Press",5,"5","120 s"), ("Weighted Pull-ups",5,"5","120 s"), ("Overhead Press",4,"8","90 s"), ("Dumbbell Row",4,"10","90 s"), ("Tricep/Bicep Superset",3,"12","60 s")),
            "Tuesday":   _day("Cardio",             35, ("Zone 2 Run / Bike",1,"30 min","—"), ("Dynamic Warm-down",1,"5 min","—")),
            "Wednesday": _day("Lower Strength",     60, ("Barbell Squat",5,"5","150 s"), ("Conventional Deadlift",4,"5","150 s"), ("Leg Press",3,"12","90 s"), ("Nordic Curl",3,"8","90 s"), ("Calf Raises",4,"15","45 s")),
            "Thursday":  _day("Cardio + Core",      40, ("Assault Bike / Swim",1,"20 min","—"), ("Weighted Plank",4,"30 s","30 s"), ("Dragon Flag",3,"8","60 s"), ("L-Sit Progression",3,"15 s","45 s")),
            "Friday":    _day("Full Body Athletic", 55, ("Power Clean / Jump Squat",4,"5","120 s"), ("Dumbbell Bench",3,"12","90 s"), ("Single-Leg RDL",3,"10 each","60 s"), ("TRX Rows",3,"15","60 s"), ("Med Ball Slams",4,"10","45 s")),
        }),
    },
}


class WorkoutGenerator:
    """Tool: Generates a personalised weekly workout plan based on goal and experience level."""

    def generate(self, profile: UserProfile) -> dict:
        days_per_week, focus, active = _DATA[profile.goal][profile.experience_level]
        return {
            "goal":             profile.goal,
            "experience_level": profile.experience_level,
            "days_per_week":    days_per_week,
            "focus":            focus,
            "schedule":         {day: active.get(day, _rest()) for day in DAYS},
        }
