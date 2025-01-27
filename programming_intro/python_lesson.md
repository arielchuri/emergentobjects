# Introduction to Programming Concepts with Python

## Lesson Overview
This lesson introduces the basics of programming using Python. Students will learn about variables, data types, basic input/output, conditional statements, loops, and functions. By the end of the lesson, students will create a simple program that combines these concepts.

### Objectives
1. Understand and use variables and data types.
2. Write basic input and output commands.
3. Use conditional statements to control program flow.
4. Create and use loops to handle repetition.
5. Define and call functions to organize code.

---

## Lesson Plan

### 1. Introduction (10 minutes)
- Explain what programming is and its importance.
- Discuss why Python is a great beginner-friendly language.
- Show a simple Python program:

```python
print("Hello, world!")
```

**Activity**: Ask students to run this code in their Python environment.

---

### 2. Variables and Data Types (15 minutes)
- **Concept**: Explain variables as containers for storing data.
- **Example**:

```python
name = "Alice"
age = 25
height = 5.6
is_student = True
```

- Discuss basic data types:
  - `str` (string)
  - `int` (integer)
  - `float` (floating-point number)
  - `bool` (boolean)

**Activity**: Have students declare their own variables and print them.

---

### 3. Input and Output (15 minutes)
- **Concept**: Getting input from users and displaying output.
- **How to Accept Input**: Explain the `input()` function.
  - Syntax: `variable = input("Prompt text")`
  - Input is always stored as a string; use type conversion (`int()`, `float()`) when needed.
- **Example**:

```python
name = input("What is your name? ")
print("Hello, " + name + "!")

age = int(input("How old are you? "))
print("You are", age, "years old.")
```

**Activity**: Create a program that asks for the user’s age and calculates the year they were born.

---

### 4. Conditional Statements (20 minutes)
- **Concept**: Making decisions using `if`, `elif`, and `else`.
- **Example**:

```python
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")
```

**Activity**: Write a program to determine if a number entered by the user is odd or even.

---

### 5. Loops (20 minutes)
- **Concept**: Repeating actions using `for` and `while` loops.
- **Examples**:

**For Loop**:
```python
for i in range(5):
    print("This is iteration", i)
```

**While Loop**:
```python
count = 0
while count < 5:
    print("Count is", count)
    count += 1
```

**Activity**: Write a program that prints the first 10 numbers of the Fibonacci sequence.

---

### 6. Functions (20 minutes)
- **Concept**: Organizing code into reusable blocks.
- **Example**:

```python
def helloFunction():
    return "Hello World!"

print(helloFunction)
```

- **Concept**: Using functions with arguments.
- **Example**:

```python
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
```

**Activity**: Create a function to calculate the area of a rectangle, given its length and width.

---

### 7. Final Project (30 minutes)
**Objective**: Combine all the learned concepts into a single program.

**Project**: Create a simple quiz program.
- Ask the user 3-5 questions.
- Track their score.
- Provide feedback at the end based on their score.

**Example Starter Code**:
```python
def ask_question(question, correct_answer):
    answer = input(question + " ")
    return answer.lower() == correct_answer.lower()

score = 0

if ask_question("What is the capital of France?", "Paris"):
    score += 1

if ask_question("What is 2 + 2?", "4"):
    score += 1

print("Your final score is:", score)
```

---

### Homework
- Practice writing Python programs that use the concepts learned in class.
- Suggested problems:
  1. Write a program to check if a number is prime.
  2. Create a program that calculates the factorial of a number.
  3. Build a basic calculator that can add, subtract, multiply, and divide.

---

### Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Replit Online Python Compiler](https://replit.com/~)

---

### Closing (5 minutes)
- Recap the concepts learned.
- Encourage students to explore Python further and practice regularly.
- Answer any remaining questions.

