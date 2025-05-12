# 🎉 Welcome to runcode: Your Offline LeetCode Playground! 🎉

Hey there, coding champion! 💻✨

Tired of copying and pasting problems into online judges? Want a sandbox where you're the boss, complete with built-in timing, diffs, and a history tracker? Say hello to **runcode**! 🚀

## 🚀 Features

- **Offline CLI**: Run and test problems right from your terminal.
- **Auto-Diff**: Pinpoint exactly where your output diverges from the expected.
- **Timing Metrics**: See how your solution stacks up in milliseconds.
- **Submission History**: Log every run’s input, expected, actual, runtime, and timestamp.
- **Template Problem**: Drop in a new problem in seconds.

### New Features 🎉

#### ✅ Test Case Summary & Analytics
- Displays:
  - Total test cases
  - Passed/failed count
  - Average execution time
- Hides full table if > 10 tests, shows only failures.

#### 🧪 Fancy Test Details
- Colorful tables with emojis per row:
  - 🎉 PASS in green or 💥 FAIL in red
  - Columns for Input, Expected, Got, Time, and Std Output

#### 🛠️ CLI Problem File Generator
Run:
```bash
runcode create
# or use `uv create` for a shortcut!
```
Prompts you to enter:
- Problem filename
- Title & detailed description (multi-line!)
- Test cases (input & optional expected)

Automatically scaffolds `problems/{problem_name}.py` from templates.

---

## 📦 Getting Started

### 1. Install

```bash
git clone https://github.com/yourusername/runcode.git
cd runcode
pip install -r requirements.txt
```
Or, after publishing:
```bash
pip install local-code
```

### 2. Quickstart

```bash
python -m runcode list          # List available problems
python -m runcode run sample_problem
python -m runcode run --all
```

### 3. Create & Solve

```bash
python3 runcode create               # Scaffold a new problem
python3 runcode run my_problem       # Run tests
python3 runcode custom my_problem    # Interactive custom-case mode
```

### 4. Check History

```bash
python3 runcode history              # Preview recent runs
python3 runcode history --full       # Show full code
python3 runcode history -p two_sum -l 3  # Last 3 runs for two_sum
python3 runcode history --id 5       # View entry #5
```

---

> "First, solve the problem. Then, write the code." — John Johnson 🚀

Happy coding & may the ACs be ever in your favor! 🍀✨