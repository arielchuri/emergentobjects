# Expanding Programming Concepts with Python

## Lesson Overview
This lesson builds upon the foundational concepts introduced in the previous session. Students will deepen their understanding of functions, loops, and conditional logic by applying them in practical mini-projects. Additionally, they will be introduced to lists and error handling to enhance the functionality of their programs.

### Objectives
1. Strengthen understanding of functions by incorporating return values and multiple arguments.
2. Practice using loops and conditionals in small applications.
3. Introduce lists as a way to store and manipulate multiple values.
4. Learn basic error handling using `try` and `except`.

---

## Lesson Plan

### 1. Review and Discussion (10 minutes)
- Go over homework exercises:
  1. Checking if a number is prime.
  2. Calculating a factorial.
  3. Basic calculator program.
- Discuss challenges students faced and solutions they found.

---

### 2. Expanding Functions (20 minutes)
- **Concept**: Functions can take multiple arguments and return values.
- **Example**:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print("The sum is:", result)
```

- **Activity**: Modify the basic calculator from homework to use functions for each operation (addition, subtraction, multiplication, division).

---

### 3. Introducing Lists (20 minutes)
- **Concept**: Lists store multiple values and can be iterated over.
- **Example**:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

- **Activity**: Extend the quiz program from the previous lesson by storing multiple questions and answers in lists, then using a loop to ask them.

---

### 4. Handling Errors (15 minutes)
- **Concept**: Using `try` and `except` to prevent program crashes.
- **Example**:

```python
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That was not a valid number!")
```

- **Activity**: Improve the basic calculator program by handling division by zero and invalid inputs.

---

### 5. Mini-Project: Grocery List Manager (30 minutes)
**Objective**: Use functions, loops, and lists to create a simple interactive program.

**Project Tasks**:
1. Allow the user to add items to a grocery list.
2. Display the list after each addition.
3. Allow the user to remove items.
4. Handle invalid input errors gracefully.

**Example Starter Code**:

```python
grocery_list = []

def add_item(item):
    grocery_list.append(item)
    print(f"{item} added to the list.")

def remove_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print("Item not found.")

while True:
    action = input("Do you want to add, remove, or view your list? (type 'quit' to exit): ")
    if action == "quit":
        break
    elif action == "add":
        item = input("Enter item to add: ")
        add_item(item)
    elif action == "remove":
        item = input("Enter item to remove: ")
        remove_item(item)
    elif action == "view":
        print("Your grocery list:", grocery_list)
    else:
        print("Invalid choice, try again.")
```

---

### Additional Example Scripts

#### Determining if a Number is Odd or Even
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
```

#### Summing All Elements in a List
```python
numbers = [1, 2, 3, 4, 5]
print("Sum of list:", sum(numbers))
```

#### Finding the Largest Number in a List
```python
numbers = [10, 25, 3, 76, 45]
print("The largest number is:", max(numbers))
```

#### Counting How Many Times a Word Appears in a Sentence
```python
sentence = input("Enter a sentence: ")
word = input("Enter a word to count: ")
print(f"The word '{word}' appears {sentence.lower().split().count(word.lower())} times.")
```

---

### Homework
- Expand the grocery list manager by adding:
  1. A way to save and load the list from a file.
  2. A sorting feature.
  3. An option to clear the list.
- Modify the quiz program from the previous lesson to:
  1. Randomize the order of questions.
  2. Allow multiple-choice answers.

---

### Resources
- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Handling Errors](https://www.w3schools.com/python/python_try_except.asp)
- [Loops in Python](https://realpython.com/python-for-loop/)

---

### Closing (5 minutes)
- Recap the new concepts learned.
- Encourage students to experiment with modifying and improving their programs.
- Answer any remaining questions.


