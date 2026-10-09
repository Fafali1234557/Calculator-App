#  Python Calculator — Command-Line Application

A simple, interactive, command-line calculator developed using **Python**. This project demonstrates fundamental programming concepts, including functions, dictionaries, loops, conditional statements, and user input handling.

The calculator performs basic arithmetic operations and allows users to continue calculating with previous results without restarting the program.

##  Project Overview

The **Python Calculator** is a console-based application that lets users perform mathematical calculations through an interactive interface.

Rather than using lengthy conditional statements to select mathematical operations, the program uses a **dictionary to map arithmetic operators to their corresponding functions**, making the code more organized, readable, and easier to extend.

This project was developed as part of my practical Python programming journey to strengthen my problem-solving skills and understanding of programming fundamentals.

##  Features

-  **Addition:** Add two numbers.
-  **Subtraction:** Subtract one number from another.
-  **Multiplication:** Multiply two numbers.
-  **Division:** Divide one number by another.
-  **Continuous Calculations:** Reuse the previous result for additional calculations.
-  **Interactive Interface:** Accept numerical inputs and mathematical operators from users.
-  **Operation Validation:** Detect unsupported arithmetic operators and display an appropriate message.
-  **Function-Based Design:** Use reusable functions and dictionary-based function selection.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Python Functions | Implement arithmetic operations |
| Dictionaries | Map operators to functions |
| While Loops | Support continuous calculations |
| Conditional Statements | Control program execution |

**Dependencies:** None. The project uses only built-in Python functionality.

##  Project Structure

```text
python-calculator/
│
├── calculator.py       # Main Python calculator
└── README.md           # Project documentation
```

##  Getting Started

### Prerequisites

Ensure Python 3 is installed on your computer.

Verify your installation by running:

```bash
python --version
```

On some systems, you may need to use `python3` instead.

### Installation and Execution

**Step 1: Clone the repository**

Clone this GitHub repository to your local computer or download its ZIP file.

**Step 2: Navigate to the project directory**

```bash
cd python-calculator
```

**Step 3: Run the application**

```bash
python calculator.py
```

Alternatively:

```bash
python3 calculator.py
```

The calculator will start running in your terminal.

##  Example Usage

```text
What's the first number?: 10

Please select operations form the following:
+
-
*
/

Pick an operation: +
What's the second number?: 5

10.0 + 5.0 = 15.0

Do you want to continue calculating with the answer?
Type 'yes' or 'no'. yes

Pick another operation: *
What's the next number?: 2

15.0 * 2.0 = 30.0

Do you want to continue calculating with the answer?
Type 'yes' or 'no'. no
```

The application ends when the user chooses not to continue.

##  How the Calculator Works

### 1. Arithmetic Functions

The application defines four reusable functions for performing basic mathematical operations.

```python
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2
```

Each function accepts two numbers as parameters and returns the calculated result.

### 2. Dictionary-Based Operation Selection

Instead of relying on multiple `if-elif` statements to identify arithmetic operations, the calculator stores references to functions inside a dictionary.

```python
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
```

When a user selects an operator, the program retrieves the corresponding function from the dictionary.

```python
calculation_function = operations[selected_operation]
answer = calculation_function(first_number, second_number)
```

This demonstrates that **Python functions are first-class objects** and can be stored as dictionary values and called dynamically.

### 3. Continuous Calculations

The application uses a `while` loop to allow users to continue calculating with the previous result.

```python
new_answer = calculation_function(answer, next_number)
answer = new_answer
```

The updated answer becomes the starting value for the next calculation.

This eliminates the need to re-enter previous results manually.

### 4. Operator Validation

The calculator checks whether the selected operator exists in its dictionary.

```python
if operations.get(selected_operation) is None:
    print("Invalid operation selected. Please try again.")
```

Unsupported operations are rejected, preventing invalid dictionary lookups. In the current version, an invalid selection ends the calculation flow rather than prompting again.

##  Programming Concepts Practised

Through this project, I strengthened my understanding of:

- Function definition and execution
- Function parameters and return values
- Dictionaries and key-value pairs
- Storing functions as dictionary values
- Dynamic function calls
- `if`, `elif`, and `else` conditions
- `while` loops and `break` statements
- User interaction using `input()`
- Type conversion using `float()`
- Formatted output using f-strings
- Writing readable and reusable Python code

##  Current Limitations

This is an early version of the calculator, and some improvements are still needed:

- Division by zero is not yet handled and raises a `ZeroDivisionError`.
- Non-numeric input raises a `ValueError`.
- Invalid arithmetic operators terminate the current calculation instead of allowing users to select another operator.
- Users cannot begin an entirely new calculation without restarting the application.
- The application currently runs only through the command line.

##  Future Improvements

Planned enhancements include:

- [ ] Implement exception handling using `try` and `except`.
- [ ] Prevent division-by-zero errors.
- [ ] Improve validation of numerical and operator inputs.
- [ ] Allow users to restart a new calculation.
- [ ] Add a calculation history feature.
- [ ] Support additional mathematical operations.
- [ ] Refactor the application for better maintainability.
- [ ] Build a graphical user interface using Tkinter.

##  Project Objective

The primary goal of this project is to apply Python programming fundamentals to a practical problem while improving my understanding of program flow and reusable code.

It represents another step in my journey toward becoming a proficient software developer and AI/ML engineer.

##  Contributions

Suggestions, feedback, and constructive contributions are welcome.

Feel free to fork the repository, explore the code, and suggest improvements.

##  Support

If you find this project helpful, consider giving the repository a star!

**Built with Python, curiosity, and a passion for continuous learning.** 