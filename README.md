# 🎉 Welcome to runcode: Your Offline LeetCode Playground! 🎉

Hey there, coding champion! 💻✨

Tired of copying and pasting problems into online judges? Want a sandbox where you're the boss, complete with built-in timing, diffs, and a history tracker? Say hello to **runcode**! 🚀

## 🚀 Features

- **Offline CLI**: Run and test problems right from your terminal.
- **Auto-Diff**: Pinpoint exactly where your output diverges from the expected.
- **Timing Metrics**: See how your solution stacks up in milliseconds.
- **Submission History**: Log every run’s input, expected, actual, runtime, and timestamp.
- **Template Problem**: Drop in a new problem in seconds.
- 
### New Features

#### ✅ Test Case Summary & Analytics
- Displays:
  - Total test cases
  - Passed/failed count
  - Average execution time
  - Optionally shows failed test case details only (if >10)

#### 🛠️ CLI Problem File Generator
Run:
```bash
runcode create
```
Prompts you to enter:
- Problem name (e.g., `two_sum`)
- Function signature
- Example test cases

Automatically creates a stub in `problems/{problem_name}.py`.

## 📦 Getting Started

### 1. Clone & Install

```bash
git clone https://github.com/yourusername/runcode.git
cd runcode
pip install -r requirements.txt
``` 

### 2. Quickstart

Run a single problem:
```bash
python -m runcode run sample_problem
```

Run **all** problems:
```bash
python -m runcode run --all
```

### 3. Create Your Own Problem

```bash
cp problems/template_problem.py problems/my_awesome_problem.py
# Edit title, description, and tests.
``` 

Test cases are defined as:
```python
{
  "input": ([arg1, arg2, ...],),
  "output": <expected>  # Optional: if omitted or None, `reference_solution` is used.
}
```

### 4. Custom Tests

```bash
python -m runcode custom my_awesome_problem
``` 
Enter something like `[1,2,3], 4` and watch!

### 5. Inspect Your Code

- Preview history:
  ```bash
  python -m runcode history
  ```  
- Full code:
  ```bash
  python -m runcode history --full
  ```
- Last 2 runs of `sample_problem`:
  ```bash
  python -m runcode history -p sample_problem -l 2
  ```
- Specific entry by ID:
  ```bash
  python -m runcode history --id 5
  ```

## 🛠️ Advanced Setup

You can streamline things even more with our `setup.sh`:
```bash
chmod +x setup.sh
./setup.sh
```
This will create a virtual environment, install dependencies, and get you coding in style. 🕶️

---

> "First, solve the problem. Then, write the code." — John Johnson 🚀

Happy coding, and may all your submissions be **Accepted**! 🌟