# 🚀 Welcome to runcode: Your Ultimate Offline Coding Playground! 🎉

**Tired of online distractions while solving coding problems?**  
**runcode** is here to revolutionize your problem-solving experience! Designed for developers, students, and coding enthusiasts, **runcode** brings the power of an offline LeetCode-style environment right to your terminal. Whether you're preparing for interviews, practicing algorithms, or just having fun with code, **runcode** is your perfect companion.

---

### 🌟 **Why Choose runcode?**

- **Offline First**: No internet? No problem! Solve problems anytime, anywhere.
- **Interactive CLI**: Intuitive and user-friendly commands make navigation a breeze.
- **Custom Problem Creation**: Easily create and test your own coding challenges.
- **Built-in Analytics**: Track your progress with detailed test summaries and history logs.
- **Debugging Made Easy**: Auto-diff highlights differences between your output and the expected result.
- **Fun & Engaging**: Colorful outputs, emojis, and a playful interface make coding enjoyable.

---

With **runcode**, you’re not just solving problems—you’re mastering them. Dive in, explore, and let your coding journey begin! 🚀


## 🛠️ Setting Up **runcode** on Your Local System

Welcome to the **Setting Up** section! Here, I’ll guide you step-by-step on how to get **runcode** running on your local system. Don’t worry if you’re new to Python or programming—this guide is beginner-friendly and packed with helpful tips! Let’s get started! 🚀

---

### 1️⃣ **Prerequisites**

Before we begin, make sure you have the following installed on your system:

1. **Python 3.8 or higher**  
   - Check if Python is installed by running:
     ```bash
     python3 --version
     ```
     or
     ```bash
     python --version
     ```
     **Output Example:**
     ```
     Python 3.10.5
     ```
     If Python is not installed, download it from the [official Python website](https://www.python.org/downloads/).

2. **pip** (Python’s package manager)  
   - Check if `pip` is installed by running:
     ```bash
     pip --version
     ```
     **Output Example:**
     ```
     pip 22.0.4
     ```
     If not installed, it usually comes bundled with Python. Otherwise, follow [this guide](https://pip.pypa.io/en/stable/installation/) to install it.

---

### 2️⃣ **Download the Code**

To get the **runcode** project on your local system, you’ll need to clone it from GitHub. Follow these steps:

1. Open your terminal (Command Prompt, PowerShell, or any CLI tool).
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/DrKakku/local_code.git
   ```
   **Output Example:**
   ```
   Cloning into 'local_code'...
   remote: Enumerating objects: 42, done.
   remote: Counting objects: 100% (42/42), done.
   remote: Compressing objects: 100% (30/30), done.
   Receiving objects: 100% (42/42), done.
   ```

3. Navigate into the project directory:
   ```bash
   cd local_code
   ```

---

### 3️⃣ **Install Dependencies**

The project uses some Python libraries to work. These are listed in the `requirements.txt` file. To install them:

1. Run the following command:
   ```bash
   pip install -r requirements.txt
   ```
   **Output Example:**
   ```
   Collecting click==8.1.3
   Collecting rich==12.6.0
   Collecting jinja2==3.1.2
   ...
   Successfully installed click-8.1.3 rich-12.6.0 jinja2-3.1.2
   ```

2. If you encounter any errors:
   - **Error: `pip` not recognized**  
     Ensure Python and pip are added to your system’s PATH. Reinstall Python if needed and check the “Add Python to PATH” option during installation.
   - **Error: Permission denied**  
     Use `pip` with admin privileges:
     ```bash
     sudo pip install -r requirements.txt
     ```

---

### 4️⃣ **Verify the Setup**

Let’s check if everything is working correctly:

1. Run the following command to list all available problems:
   ```bash
   python -m runcode list
   ```
   **Expected Output:**
   ```
   - sample_problem
   - my_problem
   ```

2. Run a sample problem to ensure the program works:
   ```bash
   python -m runcode run sample_problem
   ```
   **Expected Output:**
   ```
   🎉 PASS: Test case 1
   💥 FAIL: Test case 2
   Details: Expected [1, 2], Got [1, 3]
   ```

---

### 5️⃣ **Quick Fixes for Common Issues**

- **Problem: `ModuleNotFoundError`**  
  Ensure you’re in the correct directory (`local_code`) and installed the dependencies using `pip install -r requirements.txt`.

- **Problem: `python` command not found**  
  Use `python3` instead of `python`:
  ```bash
  python3 -m runcode list
  ```

- **Problem: Git not installed**  
  Download the repository as a ZIP file from GitHub:
  1. Go to [this link](https://github.com/DrKakku/local_code).
  2. Click on the green **Code** button and select **Download ZIP**.
  3. Extract the ZIP file and navigate to the extracted folder in your terminal.

---

### 🎉 **You’re All Set!**

Congratulations! You’ve successfully set up **runcode** on your local system. Now you can start solving problems, creating new ones, and exploring all the features. 🚀

If you face any issues, feel free to revisit this guide or check the **Troubleshooting** section in the README. Happy coding! 🎨✨


## 🌟 Features

Welcome to the **Features** section, where we dive into the exciting capabilities of **runcode**! This is your ultimate offline coding playground, packed with tools and features to make problem-solving fun, efficient, and engaging. Let’s explore what makes **runcode** your go-to solution for coding challenges:

---

### 🖥️ **Offline Problem Solving**
No internet? No problem! With **runcode**, you can solve coding challenges directly from your terminal without relying on online platforms. Whether you're on a plane, in a remote area, or just want to focus without distractions, **runcode** has you covered.

**Example:**
```bash
python -m runcode run sample_problem
```
Output:
```
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [1, 2], Got [1, 3]
```

---

### 🔍 **Auto-Diff for Debugging**
Ever struggled to figure out why your output doesn’t match the expected result? **runcode** provides an **auto-diff** feature that highlights the exact differences between your output and the expected output. This makes debugging faster and more intuitive.

**Example:**
```bash
python -m runcode run my_problem
```
Output:
```
💥 FAIL: Test case 3
Expected: [1, 2, 3]
Got: [1, 2, 4]
```

---

### ⏱️ **Execution Metrics**
Curious about how fast your solution runs? **runcode** measures the runtime of your code in milliseconds, helping you optimize your solutions for performance.

**Example:**
```bash
python -m runcode run my_problem
```
Output:
```
Test case 1: ✅ PASS (Time: 1.23 ms)
Test case 2: ✅ PASS (Time: 0.98 ms)
```

---

### 📜 **History Tracker**
Keep track of all your runs with the built-in history tracker. It logs your inputs, outputs, runtimes, and even timestamps, so you can revisit and analyze your past submissions.

**Example Commands:**
- View recent runs:
  ```bash
  python -m runcode history
  ```
- View detailed history for a specific problem:
  ```bash
  python -m runcode history -p my_problem
  ```

---

### 🛠️ **Problem Generator**
Tired of manually creating problem files? Use the **problem generator** to scaffold new problems in seconds. It’s as simple as answering a few prompts, and your problem file is ready to go!

**Example:**
```bash
python -m runcode create
```
Prompts:
```
Problem filename (without .py): my_problem
Problem title: My First Problem
Enter detailed description (end with blank line):
> Write a function to add two numbers.
> 
Enter test case input (leave blank to finish): 1, 2
Enter expected output: 3
```
Output:
```
🎉 Problem file created: problems/my_problem.py
```

---

### 🎨 **Colorful Test Results**
Say goodbye to boring terminal outputs! **runcode** makes testing fun with colorful and emoji-filled results. Passes are celebrated with 🎉, while failures are marked with 💥, making it easy to spot issues at a glance.

**Example Output:**
```
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [10], Got [5]
```

---

### 🧪 **Custom Test Cases**
Want to test your solution with your own inputs? Use the **custom test case** feature to interactively provide inputs and see the results instantly.

**Example:**
```bash
python -m runcode custom my_problem
```
Prompts:
```
Enter input tuple, e.g. ([1,2], 3): [1, 2]
Expected output: 3
```
Output:
```
🎉 PASS: Your custom test case passed!
```

---

### 📊 **Test Case Analytics**
For problems with multiple test cases, **runcode** provides a detailed summary and analytics. You’ll see the total number of test cases, how many passed or failed, and the average execution time.

**Example Output:**
```
🚀 Test Summary 🚀
🎯 Total: 10
✅ Passed: 8
❌ Failed: 2
⏱️ Avg(ms): 1.45
```

---

### 🔧 **Extensibility**
Built with Python, **runcode** is highly customizable. You can add your own problems, modify templates, or even extend the functionality to suit your needs. The codebase is clean and developer-friendly, making it easy to contribute or tweak.

---

### 🎉 **Why Choose runcode?**
- **Offline First**: No distractions, no dependencies on online platforms.
- **Developer-Friendly**: Built with Python, easy to extend and modify.
- **Fun & Engaging**: Colorful outputs, emojis, and a playful CLI experience.
- **Efficient**: Built-in tools like auto-diff, execution metrics, and history tracking save you time and effort.

---

With all these features, **runcode** isn’t just a tool—it’s your coding companion. Whether you’re practicing for interviews, solving challenges, or just having fun with code, **runcode** makes the journey enjoyable and productive! 🚀
## 📖 Usage

The **Usage** section is your guide to mastering **runcode**. Here, we’ll walk you through how to use the program effectively, with detailed explanations and examples for every feature. Whether you’re running problems, creating new ones, or testing custom cases, this section has you covered!

---

### 🏃 **Running Problems**

To run a specific problem, use the `run` command followed by the problem name:

```bash
python -m runcode run <problem_name>
```

**Example:**
```bash
python -m runcode run sample_problem
```
Output:
```
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [1, 2], Got [1, 3]
```

To run all available problems at once, use the `--all` flag:

```bash
python -m runcode run --all
```

---

### 🔍 **Interactive Problem Selection**

Not sure which problem to run? Use our **interactive CLI tool** to select problems from a list. When you run the `run` or `custom` commands without specifying a problem, the CLI will display a list of available problems for you to choose from.

**Example:**
```bash
python -m runcode run
```
Interactive prompt:
```
Select a problem to run:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to run (comma-separated): 1
```
Output:
```
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [1, 2], Got [1, 3]
```

This feature makes it easy to explore and test problems without needing to remember their names.

---

### 🧪 **Testing with Custom Inputs**

Want to test your solution with your own inputs? Use the `custom` command to interactively provide inputs and see the results instantly:

```bash
python -m runcode custom <problem_name>
```

Or, use the interactive CLI to select a problem for custom testing:

```bash
python -m runcode custom
```

**Example:**
Interactive prompt:
```
Select a problem to run custom tests for:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to test (comma-separated): 2
```

Prompts:
```
Enter input tuple, e.g. ([1,2], 3): [1, 2]
Expected output: 3
```
Output:
```
🎉 PASS: Your custom test case passed!
```

---

### 🛠️ **Creating New Problems**

To create a new problem file, use the `create` command. This will guide you through a series of prompts to define the problem title, description, and test cases.

```bash
python -m runcode create
```

**Example:**
```
Problem filename (without .py): my_problem
Problem title: My First Problem
Enter detailed description (end with blank line):
> Write a function to add two numbers.
>
Enter test case input (leave blank to finish): 1, 2
Enter expected output: 3
```
Output:
```
🎉 Problem file created: problems/my_problem.py
```

---

### 📜 **Viewing History**

Track your progress with the `history` command. This feature allows you to view past runs, including inputs, outputs, and runtimes.

- View recent runs:
  ```bash
  python -m runcode history
  ```

- View detailed history for a specific problem:
  ```bash
  python -m runcode history -p <problem_name>
  ```

- Use the interactive CLI to select a problem for history viewing:
  ```bash
  python -m runcode history
  ```
  Interactive prompt:
  ```
  Select a problem to view history for:
  1. sample_problem
  2. my_problem
  Enter the number(s) of the problem(s) to view history (comma-separated): 1
  ```

---

### 🔍 **Listing Available Problems**

To see all the problems available in your workspace, use the `list` command:

```bash
python -m runcode list
```

**Example Output:**
```
- sample_problem
- my_problem
```

---

This section ensures you have all the tools and commands at your fingertips to make the most of **runcode**. Whether you’re solving problems, testing custom cases, or creating new challenges, the usage commands are designed to be intuitive and powerful!

## 📖 Usage

The **Usage** section is your guide to mastering **runcode**. Here, we’ll walk you through how to use the program effectively, with detailed explanations and examples for every feature. Whether you’re running problems, creating new ones, or testing custom cases, this section has you covered!

---

### 🏃 **Running Problems**

To run a specific problem, use the `run` command followed by the problem name:

```bash
python -m runcode run <problem_name>
```

**Example:**
```bash
python -m runcode run sample_problem
```
Output:
```
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [1, 2], Got [1, 3]
```

To run all available problems at once, use the `--all` flag:

```bash
python -m runcode run --all
```

---

### 🔍 **Interactive Problem Selection**

Not sure which problem to run? Use our **interactive CLI tool** to select problems from a list. When you run the `run` or `custom` commands without specifying a problem, the CLI will display a list of available problems for you to choose from.

**Example:**
```bash
python -m runcode run
```
Interactive prompt:
```
Select a problem to run:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to run (comma-separated): 1
```
Output:
```
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [1, 2], Got [1, 3]
```

This feature makes it easy to explore and test problems without needing to remember their names.

---

### 🧪 **Testing with Custom Inputs**

Want to test your solution with your own inputs? Use the `custom` command to interactively provide inputs and see the results instantly:

```bash
python -m runcode custom <problem_name>
```

Or, use the interactive CLI to select a problem for custom testing:

```bash
python -m runcode custom
```

**Example:**
Interactive prompt:
```
Select a problem to run custom tests for:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to test (comma-separated): 2
```

Prompts:
```
Enter input tuple, e.g. ([1,2], 3): [1, 2]
Expected output: 3
```
Output:
```
🎉 PASS: Your custom test case passed!
```

---

### 🛠️ **Creating New Problems**

To create a new problem file, use the `create` command. This will guide you through a series of prompts to define the problem title, description, and test cases.

```bash
python -m runcode create
```

**Example:**
```
Problem filename (without .py): my_problem
Problem title: My First Problem
Enter detailed description (end with blank line):
> Write a function to add two numbers.
>
Enter test case input (leave blank to finish): 1, 2
Enter expected output: 3
```
Output:
```
🎉 Problem file created: problems/my_problem.py
```

---

### 📜 **Viewing History**

Track your progress with the `history` command. This feature allows you to view past runs, including inputs, outputs, and runtimes.

- View recent runs:
  ```bash
  python -m runcode history
  ```

- View detailed history for a specific problem:
  ```bash
  python -m runcode history -p <problem_name>
  ```

- Use the interactive CLI to select a problem for history viewing:
  ```bash
  python -m runcode history
  ```
  Interactive prompt:
  ```
  Select a problem to view history for:
  1. sample_problem
  2. my_problem
  Enter the number(s) of the problem(s) to view history (comma-separated): 1
  ```

---

### 🔍 **Listing Available Problems**

To see all the problems available in your workspace, use the `list` command:

```bash
python -m runcode list
```

**Example Output:**
```
- sample_problem
- my_problem
```

---

## 🛠️ Details About Different Commands

This section provides an in-depth look at the commands available in **runcode**. Each command is designed to make your experience seamless and efficient. Below is a detailed breakdown of the commands, their options, and examples.

---

### 📋 **Command Overview**

| **Command**       | **Description**                                                                 | **Example**                                                                 |
|--------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `list`            | Lists all available problems in the `problems` directory.                      | `python -m runcode list`                                                    |
| `run`             | Runs test cases for a specific problem or multiple problems.                   | `python -m runcode run sample_problem`                                      |
| `custom`          | Allows you to run custom test cases interactively for a problem.               | `python -m runcode custom sample_problem`                                   |
| `history`         | Displays the history of past runs for a problem or all problems.               | `python -m runcode history -p sample_problem`                               |
| `create`          | Launches an interactive wizard to create a new problem file.                   | `python -m runcode create`                                                  |

---

### 🔍 **`list` Command**

| **Option** | **Description**                     | **Example**               |
|------------|-------------------------------------|---------------------------|
| None       | Lists all problems in the workspace. | `python -m runcode list` |

**Output Example:**
```
- sample_problem
- my_problem
```

---

### 🏃 **`run` Command**

| **Option**       | **Description**                                                                 | **Example**                                                                 |
|-------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `<problem>`       | Runs test cases for the specified problem.                                      | `python -m runcode run sample_problem`                                      |
| `--all`           | Runs test cases for all available problems.                                    | `python -m runcode run --all`                                               |
| `--select`        | Allows you to select problems interactively or via a comma-separated list.     | `python -m runcode run --select 1,2`                                        |

**Interactive Example:**
```bash
python -m runcode run
```
Prompt:
```
Select a problem to run:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to run (comma-separated): 1
```

---

### 🧪 **`custom` Command**

| **Option**       | **Description**                                                                 | **Example**                                                                 |
|-------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `<problem>`       | Runs custom test cases for the specified problem.                              | `python -m runcode custom sample_problem`                                   |
| `--select`        | Allows you to select problems interactively or via a comma-separated list.     | `python -m runcode custom --select 1,2`                                     |

**Interactive Example:**
```bash
python -m runcode custom
```
Prompt:
```
Select a problem to run custom tests for:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to test (comma-separated): 2
```

---

### 📜 **`history` Command**

| **Option**       | **Description**                                                                 | **Example**                                                                 |
|-------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| `-p <problem>`    | Displays the history for a specific problem.                                   | `python -m runcode history -p sample_problem`                               |
| `--full`          | Displays detailed history for all test cases.                                  | `python -m runcode history --full`                                          |
| `--limit <n>`     | Limits the number of history entries displayed.                                | `python -m runcode history --limit 5`                                       |
| `--id <id>`       | Displays a specific history entry by ID.                                       | `python -m runcode history --id 10`                                         |
| `--select`        | Allows you to select problems interactively or via a comma-separated list.     | `python -m runcode history --select 1,2`                                    |

**Interactive Example:**
```bash
python -m runcode history
```
Prompt:
```
Select a problem to view history for:
1. sample_problem
2. my_problem
Enter the number(s) of the problem(s) to view history (comma-separated): 1
```

---

### 🛠️ **`create` Command**

| **Option** | **Description**                     | **Example**               |
|------------|-------------------------------------|---------------------------|
| None       | Launches the interactive problem creation wizard. | `python -m runcode create` |

**Interactive Example:**
```bash
python -m runcode create
```
Prompts:
```
Problem filename (without .py): my_problem
Problem title: Sum of Two Numbers
Enter detailed description (end with blank line):
> Write a function that takes two integers and returns their sum.
>
Add test case? (y/n): y
Enter input tuple, e.g. ([1,2], 3): 1, 2
Enter expected output (leave blank for ref): 3
Add test case? (y/n): n
🎉 Problem file created: problems/my_problem.py
```

---

This table-based breakdown ensures you have all the information you need to use **runcode** commands effectively! 🚀

## 🛠️ Example Workflow

Here’s a step-by-step example workflow to help you get started with **runcode**. This will guide you through creating a problem, running test cases, and using the program’s features effectively.

---

### 1️⃣ **Create a New Problem**

Start by creating a new problem file using the `create` command. This will guide you through an interactive process to define the problem.

```bash
python -m runcode create
```

**Example Interaction:**
```
Problem filename (without .py): sum_two_numbers
Problem title: Sum of Two Numbers
Enter detailed description (end with blank line):
> Write a function that takes two integers and returns their sum.
>
Add test case? (y/n): y
Enter input tuple, e.g. ([1,2], 3): 1, 2
Enter expected output (leave blank for ref): 3
Add test case? (y/n): y
Enter input tuple, e.g. ([1,2], 3): 5, 7
Enter expected output (leave blank for ref):
Add test case? (y/n): n
🎉 Problem file created: problems/sum_two_numbers.py
```

---

### 2️⃣ **Implement Your Solution**

Open the newly created file (`problems/sum_two_numbers.py`) and implement your solution in the `user_solution` method.

```python
@staticmethod
def user_solution(a: int, b: int) -> int:
    return a + b
```

---

### 3️⃣ **Run Test Cases**

Run the test cases for your problem to verify your solution.

```bash
python -m runcode run sum_two_numbers
```

**Example Output:**
```
🎉 PASS: Test case 1
🎉 PASS: Test case 2
🚀 Test Summary 🚀
🎯 Total: 2
✅ Passed: 2
❌ Failed: 0
⏱️ Avg(ms): 0.45
```

---

### 4️⃣ **Test with Custom Inputs**

If you want to test your solution with custom inputs, use the `custom` command.

```bash
python -m runcode custom sum_two_numbers
```

**Example Interaction:**
```
Enter input tuple, e.g. ([1,2], 3): 10, 20
Expected output: 30
🎉 PASS: Your custom test case passed!
```

---

### 5️⃣ **View History**

Check the history of your past runs to analyze your progress.

```bash
python -m runcode history -p sum_two_numbers
```

**Example Output:**
```
History for: sum_two_numbers
1. ✅ Test case 1 (Time: 0.45 ms)
2. ✅ Test case 2 (Time: 0.50 ms)
```

---

### 6️⃣ **Explore Other Problems**

List all available problems in your workspace to explore more challenges.

```bash
python -m runcode list
```

**Example Output:**
```
- sum_two_numbers
- sample_problem
```

---

### 7️⃣ **Run All Problems**

Run test cases for all problems in your workspace.

```bash
python -m runcode run --all
```

**Example Output:**
```
Running: sum_two_numbers
🎉 PASS: Test case 1
🎉 PASS: Test case 2

Running: sample_problem
🎉 PASS: Test case 1
💥 FAIL: Test case 2
Details: Expected [1, 2], Got [1, 3]
```

---

This workflow provides a solid starting point for using **runcode**. You can expand on it by creating more problems, testing edge cases, and exploring advanced features like reference solutions and analytics! 🚀

