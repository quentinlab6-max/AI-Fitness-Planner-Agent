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
│   └── fitness_agent.py          # Agent orchestrator
├── models/
│   └── user_profile.py           # UserProfile dataclass
├── tools/
│   ├── calorie_calculator.py     # Tool 1: BMR/TDEE calculation
│   ├── macro_calculator.py       # Tool 2: Macronutrient distribution
│   ├── workout_generator.py      # Tool 3: Weekly workout plan
│   └── meal_plan_generator.py    # Tool 4: LLM-generated 7-day meal calendar
├── validation/
│   └── input_validator.py        # Input validation logic
├── tests/
│   ├── test_agent.py
│   ├── test_calorie_calculator.py
│   ├── test_input_validator.py
│   ├── test_macro_calculator.py
│   ├── test_meal_plan_generator.py
│   └── test_workout_generator.py
├── main.py                       # CLI entry point
├── pytest.ini                    # Test configuration
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
| `pytest` and parametrize | 77 tests using fixtures, `@pytest.mark.parametrize`, and `unittest.mock` |
| `unittest.mock.patch` | LLM calls are mocked in tests so the suite runs offline and instantly |
| Type annotations | All public methods use `-> dict`, `-> Tuple[bool, List[str]]`, etc. |
| Local LLM via Ollama | `MealPlanGenerator` calls a local `llama3.2` model through the `ollama` Python library |

### How These Concepts Are Applied

**Dataclass and type hints** — `UserProfile` is defined with `@dataclass` and uses `Literal` types to constrain values like `goal: Literal["weight_loss", "muscle_gain", "maintenance"]`. This means invalid string values cause immediate type errors and keeps the model self-documenting.

**Object-oriented tools** — Each tool (`CalorieCalculator`, `MacroCalculator`, `WorkoutGenerator`) is a class with a single method (`calculate` or `generate`). This makes it straightforward to register them in the agent's tool dictionary and call them by name.

**Mathematical formulas** — `CalorieCalculator` implements the Mifflin-St Jeor equation:
- Male: `BMR = 10 × weight_kg + 6.25 × height_cm − 5 × age + 5`
- Female: `BMR = 10 × weight_kg + 6.25 × height_cm − 5 × age − 161`
- TDEE = BMR × activity multiplier, then adjusted by goal (+300 muscle gain, −500 weight loss, 0 maintenance)

**Error accumulation** — `InputValidator.validate()` checks all seven fields independently and returns the full list of errors in one call. This avoids showing the user one error at a time and improves usability.

**Parameterized tests** — `test_workout_generator.py` uses `@pytest.mark.parametrize` to test all 9 goal/experience combinations (3 goals × 3 levels) with a single test function, avoiding repetition.

**Local LLM integration** — `MealPlanGenerator` sends a structured prompt to a locally running `llama3.2` model via the `ollama` Python library. The prompt includes the user's calorie and macro targets; the model returns a 7-day meal calendar in plain text which is then parsed into a structured dictionary. This is the genuine AI component of the system — the LLM reasons about food combinations and portion sizes rather than following hardcoded rules.

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
MealPlanGenerator.generate(profile, target_calories, macros)
      │  sends prompt to local llama3.2 via Ollama
      │  parses plain-text response into structured dict
      ▼
Assembled result dict → printed to terminal
```

**Data transformation between tools:**
- Raw `dict` → `UserProfile` dataclass: field names must match exactly; validated before conversion.
- `CalorieCalculator` → `MacroCalculator`: `target_calories` (integer) is extracted from the first result and passed directly to the second tool.
- `MacroCalculator` → `MealPlanGenerator`: the full macros dict (`protein_g`, `carbs_g`, `fat_g`) and `target_calories` are forwarded to build the LLM prompt.
- `WorkoutGenerator` is independent; it only requires `profile.goal` and `profile.experience_level`.
- `MealPlanGenerator` returns both a structured `days` dict (parsed from the LLM output) and the `raw` text for fallback display if parsing fails.

All tool outputs are plain Python dictionaries. The only format conversion in the system is the parsing of the LLM's free-text response into a structured dict inside `_parse_response()`.

---

## How to Run

### Requirements

- Python 3.10 or higher
- [Ollama](https://ollama.com) installed and running locally

### Install Ollama model

```bash
ollama pull llama3.2
```

### Install Python dependencies

```bash
pip install -r requirements.txt
```

### Run the program

```bash
python main.py
```

Follow the prompts to enter your name, age, weight, height, gender, activity level, goal, and experience level. The agent will calculate your nutrition targets, generate a workout plan, and use the local LLM to create a personalised 7-day meal calendar.

### Run the tests

```bash
pytest
```

All 77 tests pass. The LLM is mocked during tests so no Ollama connection is required to run the test suite.

---

---

## Step 3 – Testing, Deployment, and Data Conversion (15.05)

### Testing Process

Testing was performed alongside implementation using `pytest`. Each module was tested independently as it was written, and integration tests were added once the agent pipeline was complete. The full test suite runs in under 3 seconds with no external connections required, because all LLM calls are mocked using `unittest.mock.patch`.

The suite is organised into six test files covering 82 tests in total:

| File | Tests | What is covered |
|---|---|---|
| `test_calorie_calculator.py` | 8 | BMR formula for male/female, all activity multipliers, all goal adjustments |
| `test_macro_calculator.py` | 8 | Percentage sums, gram values, calorie coverage within 5% |
| `test_workout_generator.py` | 21 | All 9 goal/experience combinations, day counts, exercise key structure |
| `test_input_validator.py` | 13 | Boundary values, invalid types, multiple error accumulation |
| `test_meal_plan_generator.py` | 16 | Prompt content, response parsing, mocked LLM, error handling |
| `test_agent.py` | 16 | Full pipeline, all goals, all experience levels, error propagation |

### Test Scenarios

**Scenario 1 — Valid male profile, muscle gain**
- Input: age 28, 80 kg, 180 cm, male, active, muscle gain, intermediate
- Expected: `success=True`, `target_calories > tdee`, protein ratio 30%, 4 active training days/week, 7-day meal plan returned

**Scenario 2 — Invalid input, age out of range**
- Input: age 999, otherwise valid data
- Expected: `success=False`, errors list contains age message, no tools called, no LLM contact

**Scenario 3 — Weight loss goal, calorie deficit**
- Input: any valid profile, goal = weight loss
- Expected: `target_calories = tdee - 500`, protein ratio 35%, workout has correct active day count for experience level

**Scenario 4 — Maintenance goal, no calorie adjustment**
- Input: any valid profile, goal = maintenance
- Expected: `target_calories == tdee`, adjustment_kcal = 0, macro split 25/50/25

**Scenario 5 — All 9 workout combinations**
- Input: each combination of (weight_loss, muscle_gain, maintenance) × (beginner, intermediate, advanced)
- Expected: schedule has exactly 7 days, active days match (3/4/5), all exercises have name/sets/reps/rest keys

**Scenario 6 — Macro percentages sum**
- Input: any valid profile and calorie target
- Expected: protein_pct + carbs_pct + fat_pct = 100 for every goal

**Scenario 7 — Ollama connection failure**
- Input: valid profile, Ollama service not running (simulated with mock raising Exception)
- Expected: result contains `error` key with instructions, `days` is empty dict, no crash

**Scenario 8 — Malformed LLM response**
- Input: LLM returns partial or unexpected text format
- Expected: `_parse_response()` returns a partial dict without raising an exception, `raw` field contains the original text as fallback

**Scenario 9 — Multiple simultaneous input errors**
- Input: age = -1, weight = 5, gender = "alien"
- Expected: all three errors returned in a single list, validation does not stop at the first failure

### Deployment Preparation

The system is deployed as a **local command-line application**. No server, cloud service, or internet connection is required except for the initial model download.

**Prerequisites:**
- Python 3.10 or higher
- [Ollama](https://ollama.com) installed on the user's machine

**Installation steps:**

```bash
# 1. Clone the repository
git clone https://github.com/quentinlab6-max/AI-Fitness-Planner-Agent.git
cd AI-Fitness-Planner-Agent

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Download the LLM model (one-time, ~2 GB)
ollama pull llama3.2

# 4. Run the program
python main.py
```

**Running tests (no Ollama required):**

```bash
pytest
```

There are no environment variables required. There is no configuration file to edit. The only user-facing decision is the choice of Ollama model, which can be changed by passing the `ollama_model` parameter to `FitnessAgent()` in `main.py`.

### Data Conversion and Porting

The system transforms data through four distinct conversion steps:

**Step 1 — Raw dict → UserProfile dataclass**

The user answers CLI prompts in `main.py`, which assembles a plain Python dictionary:
```python
{"name": "Alice", "age": 25, "weight_kg": 65.0, ...}
```
After validation, `FitnessAgent` converts this into a typed `UserProfile` object via `UserProfile(**user_data)`. This conversion enforces field types and makes the data safe to pass to tools.

**Step 2 — UserProfile → nutrition integers**

`CalorieCalculator` reads float fields from `UserProfile` (weight, height, age) and string fields (gender, activity_level, goal) to produce rounded integers: `bmr`, `tdee`, `target_calories`. These integers are the only values passed forward — the original profile fields are not reused for nutrition calculations.

**Step 3 — Integers + ratios → macro grams**

`MacroCalculator` receives `target_calories` (int) and uses `profile.goal` to look up ratio constants. It applies `kcal / calories_per_gram` arithmetic and rounds the result to produce `protein_g`, `carbs_g`, `fat_g` as integers.

**Step 4 — Integers → prompt string → structured dict**

`MealPlanGenerator._build_prompt()` converts the integer nutrition targets into a formatted string instruction sent to the LLM. The LLM returns free-text. `_parse_response()` then converts that free text back into a structured Python dictionary by scanning each line for day headers (`Monday:`) and meal prefixes (`Breakfast`, `Lunch`, etc.). If parsing fails or is incomplete, the `raw` field preserves the original LLM text as a fallback so no data is lost.
