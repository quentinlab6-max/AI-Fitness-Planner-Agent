Quentin Pierre Roger Labourdette

# AI Fitness Planner Agent

---

## Step 1 – Initial System Design (24.04)

### System Description

The goal of this project is to develop an AI-based fitness planning assistant using Python. The system will generate personalized nutrition and workout programs based on user characteristics such as age, weight, height, and fitness goals.

Instead of simply providing general advice, the system will process user data and compute structured results using specific tools. The output will include daily calorie needs, macronutrient distribution, and a weekly workout plan.

### Agent-Based Approach

The system will be implemented as a single intelligent agent. This agent will be responsible for interpreting user input and selecting the appropriate tools to generate a personalized fitness plan.

The agent will follow a structured workflow:

1. receive user input
2. validate the data
3. determine the user's goal
4. call the necessary tools
5. combine results into a final structured output

This approach ensures that the system is not only reactive but also decision-oriented and tool-driven.

### Tools Used in the System

The system will include the following tools:

- **Calorie Calculation Tool** — Calculates daily energy needs based on user characteristics.
- **Macronutrient Calculation Tool** — Determines protein, carbohydrate, and fat distribution.
- **Workout Plan Generator** — Creates a weekly training schedule adapted to the user's level and goal.
- **Input Validation Module** — Ensures that user data is correct and usable.

### Preliminary Programming Concepts

The following programming concepts will be required:

- Python classes and object-oriented design
- Functions and modular programming
- Conditional logic (if/else)
- Mathematical calculations and formulas
- Data structures (lists, dictionaries)
- Error handling and input validation
- File organization into modules

---

## Step 2 – Implementation Progress (08.05)

### Updated System Description

The system has been fully implemented as a modular Python application. It is organized into four packages — `models`, `validation`, `tools`, and `agent` — plus a CLI entry point in `main.py` and a `tests` package.

The agent follows a sequential tool-calling pipeline. It receives raw user input from the command line, validates it, constructs a typed `UserProfile` object, and then calls three tools in order. The results are combined into a single structured plan that is printed to the terminal in a formatted layout.

The project structure is as follows:

```
AI-Fitness-Planner-Agent/
├── agent/
│   └── fitness_agent.py        # Agent orchestrator
├── models/
│   └── user_profile.py         # UserProfile dataclass
├── tools/
│   ├── calorie_calculator.py   # Tool 1: BMR/TDEE calculation
│   ├── macro_calculator.py     # Tool 2: Macronutrient distribution
│   └── workout_generator.py    # Tool 3: Weekly workout plan
├── validation/
│   └── input_validator.py      # Input validation logic
├── tests/
│   ├── test_agent.py
│   ├── test_calorie_calculator.py
│   ├── test_input_validator.py
│   ├── test_macro_calculator.py
│   └── test_workout_generator.py
├── main.py                     # CLI entry point
├── pytest.ini                  # Test configuration
└── requirements.txt
```

### Refined List of Programming Concepts

The following concepts are actively used in the implementation:

| Concept | Where it is applied |
|---|---|
| Python `dataclasses` | `UserProfile` — typed model for user data |
| `Literal` type hints | Constrains allowed values for gender, goal, activity level, experience |
| Object-oriented design | Each tool is a class with a single public method |
| Modular project structure | Code split across `agent/`, `tools/`, `models/`, `validation/` |
| Dictionary-based data structures | Workout plans stored as nested dictionaries keyed by goal and experience |
| Mathematical formulas | Mifflin-St Jeor BMR equation in `CalorieCalculator` |
| Conditional logic | Gender-specific BMR formula; goal-based calorie adjustment |
| Error accumulation pattern | `InputValidator` collects all errors before returning instead of failing on the first |
| f-strings and format specifiers | CLI output formatting in `main.py` |
| `pytest` and parametrize | 66 tests using fixtures and `@pytest.mark.parametrize` |
| Type annotations | All public methods use `-> dict`, `-> Tuple[bool, List[str]]`, etc. |

### How These Concepts Are Applied

**Dataclass and type hints** — `UserProfile` is defined with `@dataclass` and uses `Literal` types to constrain values like `goal: Literal["weight_loss", "muscle_gain", "maintenance"]`. This means invalid string values cause immediate type errors and keeps the model self-documenting.

**Object-oriented tools** — Each tool (`CalorieCalculator`, `MacroCalculator`, `WorkoutGenerator`) is a class with a single method (`calculate` or `generate`). This makes it straightforward to register them in the agent's tool dictionary and call them by name.

**Mathematical formulas** — `CalorieCalculator` implements the Mifflin-St Jeor equation:
- Male: `BMR = 10 × weight_kg + 6.25 × height_cm − 5 × age + 5`
- Female: `BMR = 10 × weight_kg + 6.25 × height_cm − 5 × age − 161`
- TDEE = BMR × activity multiplier, then adjusted by goal (+300 muscle gain, −500 weight loss, 0 maintenance)

**Error accumulation** — `InputValidator.validate()` checks all seven fields independently and returns the full list of errors in one call. This avoids showing the user one error at a time and improves usability.

**Parameterized tests** — `test_workout_generator.py` uses `@pytest.mark.parametrize` to test all 9 goal/experience combinations (3 goals × 3 levels) with a single test function, avoiding repetition.

### Tool Integration into the System

The agent orchestrates tool calls in a fixed sequence:

```
User input (dict)
      │
      ▼
InputValidator.validate()  ──── invalid ──→  return errors, stop
      │ valid
      ▼
UserProfile(**user_data)         ← typed dataclass created here
      │
      ▼
CalorieCalculator.calculate(profile)
      │  returns: bmr, tdee, target_calories, adjustment_kcal
      ▼
MacroCalculator.calculate(profile, target_calories)
      │  returns: protein_g, carbs_g, fat_g, percentages
      ▼
WorkoutGenerator.generate(profile)
      │  returns: 7-day schedule with exercises, sets, reps, rest
      ▼
Assembled result dict → printed to terminal
```

**Data transformation between tools:**
- Raw `dict` → `UserProfile` dataclass: field names must match exactly; validated before conversion.
- `CalorieCalculator` → `MacroCalculator`: `target_calories` (integer) is extracted from the first result and passed directly to the second tool.
- `WorkoutGenerator` is independent and runs last; it only requires the `profile.goal` and `profile.experience_level` fields.

All tool outputs are plain Python dictionaries. No serialization or format conversion is needed within this system.

---

## How to Run

### Requirements

- Python 3.10 or higher

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the program

```bash
python main.py
```

Follow the prompts to enter your name, age, weight, height, gender, activity level, goal, and experience level. The agent will then display your personalised calorie targets, macronutrient breakdown, and weekly workout plan.

### Run the tests

```bash
pytest
```

All 66 tests should pass.

---

## Next Steps (Step 3 – 15.05)

- Document test scenarios with expected results
- Describe deployment preparation
- Explain data conversion and porting
