# 🐍 Python Practice Problems — Intermediate Level

> **20 Problems** · Ordered by topic so similar concepts stay together and you build knowledge step by step.

---

## 📋 Table of Contents

| # | Problem | Topics |
|---|---------|--------|
| **🔁 LOOPS & STRINGS** |||
| [1](#1-multiplication-table-generator) | Multiplication Table Generator | Loops |
| [2](#2-number-guessing-game) | Number Guessing Game | Loops |
| [3](#3-caesar-cipher) | Caesar Cipher | Strings, Loops |
| [4](#4-anagram-checker) | Anagram Checker | Strings, Functions |
| [5](#5-password-strength-checker) | Password Strength Checker | Strings, Functions |
| **📦 FUNCTIONS** |||
| [6](#6-number-to-words) | Number to Words | Functions, Loops |
| [7](#7-unit-converter) | Unit Converter | Functions |
| [8](#8-roman-numeral-converter) | Roman Numeral Converter | Functions, Loops |
| **📚 DICTIONARIES** |||
| [9](#9-grade-book) | Grade Book | Dictionaries, Functions |
| [10](#10-inventory-system) | Inventory System | Dicts, Loops |
| [11](#11-contact-book-crud) | Contact Book (CRUD) | Dicts, Loops, Functions |
| **🏗️ OOP — CLASSES** |||
| [12](#12-bank-account-class) | Bank Account Class | OOP |
| [13](#13-student-report-card) | Student Report Card | OOP, Functions |
| [14](#14-shape-area-calculator-inheritance) | Shape Area Calculator | OOP, Inheritance |
| **⚙️ ALGORITHMS** |||
| [15](#15-bubble-sort-manual) | Bubble Sort (Manual) | Algorithms, Loops |
| [16](#16-binary-search) | Binary Search | Algorithms |
| **🔄 RECURSION** |||
| [17](#17-factorial-with-recursion) | Factorial with Recursion | Recursion, Functions |
| [18](#18-sum-of-digits-recursive) | Sum of Digits (Recursive) | Recursion, Functions |
| **🗂️ MINI-PROJECTS** |||
| [19](#19-atm-machine-simulator) | ATM Machine Simulator | Loops, Functions |
| [20](#20-to-do-list-with-file-storage) | To-Do List with File Storage | File I/O, Loops, Functions |

---

## 🗺️ Learning Path

```
Phase 1  →  #1  – #5    🔁  Loops & Strings      (build confidence with iteration)
Phase 2  →  #6  – #8    📦  Functions             (reusable, clean code)
Phase 3  →  #9  – #11   📚  Dictionaries          (key-value data + CRUD)
Phase 4  →  #12 – #14   🏗️  OOP / Classes         (basics → inheritance)
Phase 5  →  #15 – #16   ⚙️  Algorithms            (sorting & searching)
Phase 6  →  #17 – #18   🔄  Recursion             (functions calling themselves)
Phase 7  →  #19 – #20   🗂️  Mini-Projects         (combine everything)
```

---

## 🏷️ Topic Tags

`Loops` `Strings` `Functions` `Dictionaries` `OOP` `Algorithms` `Recursion` `File I/O`

---

## Problems

---

## 🔁 Phase 1 — Loops & Strings

> Get comfortable with `for`/`while` loops and string manipulation before moving on.

---

### #1 Multiplication Table Generator

**Topics:** `Loops`

Ask the user for a number and print its full multiplication table from **1 to 10** in a neat, aligned format.

**Example (n = 4):**
```
4 x  1 =  4
4 x  2 =  8
4 x  3 = 12
...
4 x 10 = 40
```

> 💡 **Hint:** Use f-strings with padding like `f"{n} x {i:2} = {n*i:3}"` for alignment.

---

### #2 Number Guessing Game

**Topics:** `Loops`

Generate a **random number between 1 and 100**. Let the user guess and give hints. Count their attempts and display it at the end.

**Example:**
```
Guess a number (1-100): 50  →  📈 Too high!
Guess a number (1-100): 25  →  📉 Too low!
Guess a number (1-100): 37  →  🎉 Correct! You got it in 3 tries!
```

> 💡 **Hint:** Use `import random` and `random.randint(1, 100)`.

---

### #3 Caesar Cipher

**Topics:** `Strings` `Loops`

Encrypt a message by shifting each letter by **N positions** in the alphabet. Non-letter characters (spaces, punctuation) should remain unchanged.

**Example (shift = 3):**
```
Input:  Hello, World!
Output: Khoor, Zruog!
```

> 💡 **Hint:** Use `ord()` and `chr()` to work with ASCII values. Handle uppercase and lowercase separately.

---

### #4 Anagram Checker

**Topics:** `Strings` `Functions`

Check if two words are **anagrams** of each other (same letters, different order). Ignore case and spaces.

**Examples:**
```
"listen"      &  "silent"      →  ✅ Yes, anagram!
"hello"       &  "world"       →  ❌ No, not an anagram.
"Astronomer"  &  "Moon starer" →  ✅ Yes, anagram!
```

> 💡 **Hint:** Sort both strings after lowercasing and removing spaces, then compare.

---

### #5 Password Strength Checker

**Topics:** `Strings` `Functions`

Check if a password is **Weak**, **Medium**, or **Strong** based on these rules:

| Criterion | Requirement |
|-----------|-------------|
| Length | At least 8 characters |
| Uppercase | At least 1 uppercase letter |
| Lowercase | At least 1 lowercase letter |
| Digit | At least 1 number |
| Special char | At least 1 symbol (`!@#$%...`) |

- **Strong** → meets all 5
- **Medium** → meets 3–4
- **Weak** → meets fewer than 3

> 💡 **Hint:** Use `import string` and check `string.punctuation` for special characters.

---

## 📦 Phase 2 — Functions

> Learn to write clean, reusable functions. Each problem here is purely function-focused.

---

### #6 Number to Words

**Topics:** `Functions` `Loops`

Convert a number from **0 to 99** into its English word representation.

**Example:**
```
Input:  42
Output: forty-two
```

> 💡 **Hint:** Use two lists — one for ones (`"one", "two"...`) and one for tens (`"twenty", "thirty"...`). Combine them for numbers 21–99.

---

### #7 Unit Converter

**Topics:** `Functions`

Build a converter with individual functions for each conversion. Ask the user what to convert and in which direction.

**Supported conversions:**

| Type | Conversion |
|------|------------|
| Distance | km ↔ miles |
| Weight | kg ↔ lbs |
| Temperature | Celsius ↔ Fahrenheit |

**Example:**
```
100 km  →  62.14 miles
  0 °C  →  32.0 °F
 70 kg  →  154.32 lbs
```

> 💡 **Hint:** Write one function per direction (e.g., `km_to_miles()` and `miles_to_km()`).

---

### #8 Roman Numeral Converter

**Topics:** `Functions` `Loops`

Convert an integer **(1 – 3999)** to its **Roman numeral** equivalent.

**Examples:**
```python
to_roman(2024)  # → "MMXXIV"
to_roman(58)    # → "LVIII"
to_roman(1994)  # → "MCMXCIV"
```

> 💡 **Hint:** Store value-symbol pairs in a list (largest to smallest):
> ```python
> values = [(1000,"M"), (900,"CM"), (500,"D"), (400,"CD"), ...]
> ```

---

## 📚 Phase 3 — Dictionaries

> Practice storing, accessing, and modifying data using Python dictionaries.

---

### #9 Grade Book

**Topics:** `Dictionaries` `Functions`

Store student names and scores in a dictionary. Then calculate and print:
- The **average** score
- The **highest scorer**
- The **lowest scorer**

**Example:**
```python
grades = {"Alice": 88, "Bob": 72, "Carol": 95}

# Output:
Average:       85.0
Highest score: Carol (95)
Lowest score:  Bob (72)
```

> 💡 **Hint:** Use `max()` and `min()` with a `key=` argument on the dictionary.

---

### #10 Inventory System

**Topics:** `Dictionaries` `Loops`

Manage a store inventory stored as `{item: quantity}`. Support:
- **Add** new item
- **Restock** (increase quantity)
- **Sell** (decrease quantity — prevent going below 0)
- **View** all items
- **Low-stock warning** for items with quantity ≤ 2

**Example:**
```python
inventory = {"apple": 5, "banana": 2, "milk": 0}

⚠️  Low stock warning:
    - banana: 2 remaining
    - milk:   0 remaining
```

---

### #11 Contact Book (CRUD)

**Topics:** `Dictionaries` `Loops` `Functions`

Build a mini contact book that runs in a loop. Store contacts as `{name: phone_number}` and support:

```
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. View all contacts
6. Quit
```

**Example:**
```
> Add:    Alice → 555-1234
> Search: Alice → 📞 555-1234
> Update: Alice → 555-9999
> Delete: Alice → ✅ Deleted
```

> 💡 **Hint:** Wrap each operation in its own function for clean code.

---

## 🏗️ Phase 4 — OOP (Classes)

> Introduction to Object-Oriented Programming. Start simple, finish with inheritance.

---

### #12 Bank Account Class

**Topics:** `OOP`

Create a `BankAccount` class with the following methods:

| Method | Description |
|--------|-------------|
| `deposit(amount)` | Add money to balance |
| `withdraw(amount)` | Remove money (block if insufficient) |
| `get_balance()` | Return current balance |

**Example:**
```python
acc = BankAccount(100)
acc.deposit(50)      # Balance: 150
acc.withdraw(200)    # ❌ "Insufficient funds!"
acc.withdraw(50)     # Balance: 100
print(acc.get_balance())  # 100
```

> 💡 **Hint:** Store `balance` as an instance variable in `__init__`. Check before withdrawing.

---

### #13 Student Report Card

**Topics:** `OOP` `Functions`

Create a `Student` class that stores a **name** and a **list of grades**. Add methods to:
- Calculate the **average**
- Determine the **letter grade**
- Print a full **report card**

**Letter Grade Scale:**

| Grade | Range |
|-------|-------|
| A | 90 – 100 |
| B | 80 – 89 |
| C | 70 – 79 |
| D | 60 – 69 |
| F | Below 60 |

**Example output:**
```
====== Report Card ======
Name:    Alice
Grades:  [85, 92, 78, 90]
Average: 86.25
Grade:   B
=========================
```

---

### #14 Shape Area Calculator (Inheritance)

**Topics:** `OOP` `Inheritance`

Create a base `Shape` class with an `area()` method. Then create **3 subclasses** that override it:

```
Shape
├── Circle
├── Rectangle
└── Triangle
```

**Example:**
```python
Circle(5).area()        # → 78.54
Rectangle(4, 6).area()  # → 24
Triangle(3, 8).area()   # → 12.0
```

> 💡 **Hint:** Use `import math` for `math.pi`. Each subclass calls `super().__init__()` and overrides `area()`.

---

## ⚙️ Phase 5 — Algorithms

> Classic computer science algorithms — understand how they work by building them yourself.

---

### #15 Bubble Sort (Manual)

**Topics:** `Algorithms` `Loops`

Sort a list of numbers using the **bubble sort** algorithm — without using `sort()` or `sorted()`. Print the list after each full pass so you can see it being sorted step by step.

**Example:**
```
Input:  [5, 3, 8, 1, 2]

Pass 1: [3, 5, 1, 2, 8]
Pass 2: [3, 1, 2, 5, 8]
Pass 3: [1, 2, 3, 5, 8]

Sorted: [1, 2, 3, 5, 8]
```

> 💡 **Hint:** Compare adjacent pairs and swap if the left is bigger. Repeat until no swaps occur.

---

### #16 Binary Search

**Topics:** `Algorithms`

Implement **binary search** on a sorted list. Return the **index** of the target (or `-1` if not found). Count how many steps it took.

**Example:**
```
List:   [1, 3, 5, 7, 9, 11, 13]
Target: 7

→ Found at index 3 in 2 steps ✅
```

> 💡 **Hint:** Start with `low = 0` and `high = len(list) - 1`. Check the middle element each time and cut the search in half.

---

## 🔄 Phase 6 — Recursion

> Functions that call themselves. Master the base case and recursive case.

---

### #17 Factorial with Recursion

**Topics:** `Recursion` `Functions`

Calculate the factorial of a number using a **recursive function** (no loops allowed). Handle edge cases: `0` and negative numbers.

**Example:**
```python
factorial(5)   # → 120  (5 × 4 × 3 × 2 × 1)
factorial(0)   # → 1
factorial(-3)  # → "Invalid input"
```

> 💡 **Hint:** Base case is `factorial(0) = 1`. Recursive case: `n * factorial(n - 1)`.

---

### #18 Sum of Digits (Recursive)

**Topics:** `Recursion` `Functions`

Recursively sum the digits of a number until you reach a **single digit** (this is called the digital root).

**Example:**
```
digital_root(9875)
→ 9 + 8 + 7 + 5 = 29
→ 2 + 9 = 11
→ 1 + 1 = 2   ✅
```

> 💡 **Hint:** Base case — if the number is less than 10, return it. Otherwise, sum its digits and call the function again.

---

## 🗂️ Phase 7 — Mini-Projects

> Combine everything you've learned. These problems use multiple concepts together.

---

### #19 ATM Machine Simulator

**Topics:** `Loops` `Functions`

Simulate a basic ATM:
1. User enters a **PIN** (max 3 attempts, then lock out)
2. After login, show a menu in a loop:

```
====== ATM Menu ======
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

> 💡 **Hint:** Use a `while` loop with a `logged_in` flag. Track balance as a variable. Use functions for each menu option.

---

### #20 To-Do List with File Storage

**Topics:** `File I/O` `Loops` `Functions`

Build a to-do list app that **saves tasks to a `.txt` file** so they persist between runs. Support:

```
1. Add task
2. View all tasks
3. Mark task complete
4. Delete task
5. Exit
```

**File format:**
```
[ ] Buy groceries
[✓] Study Python
[ ] Call dentist
```

> 💡 **Hint:** Use `open()` with `"r"`, `"w"`, and `"a"` modes. Read all lines with `readlines()`, modify the list in memory, then write it back.

---

## 📚 Concepts Summary

| Concept | Problems |
|---------|----------|
| **Loops** | #1, #2, #3, #10, #11, #15, #19 |
| **Strings** | #3, #4, #5 |
| **Functions** | #4, #5, #6, #7, #8, #9, #11, #17, #18, #19, #20 |
| **Dictionaries** | #9, #10, #11 |
| **OOP (Classes)** | #12, #13, #14 |
| **Algorithms** | #15, #16 |
| **Recursion** | #17, #18 |
| **File I/O** | #20 |

---

## ✅ Completion Tracker

**Phase 1 — Loops & Strings**
- [ ] #1  Multiplication Table Generator
- [ ] #2  Number Guessing Game
- [ ] #3  Caesar Cipher
- [ ] #4  Anagram Checker
- [ ] #5  Password Strength Checker

**Phase 2 — Functions**
- [ ] #6  Number to Words
- [ ] #7  Unit Converter
- [ ] #8  Roman Numeral Converter

**Phase 3 — Dictionaries**
- [ ] #9  Grade Book
- [ ] #10 Inventory System
- [ ] #11 Contact Book (CRUD)

**Phase 4 — OOP (Classes)**
- [ ] #12 Bank Account Class
- [ ] #13 Student Report Card
- [ ] #14 Shape Area Calculator (Inheritance)

**Phase 5 — Algorithms**
- [ ] #15 Bubble Sort (Manual)
- [ ] #16 Binary Search

**Phase 6 — Recursion**
- [ ] #17 Factorial with Recursion
- [ ] #18 Sum of Digits (Recursive)

**Phase 7 — Mini-Projects**
- [ ] #19 ATM Machine Simulator
- [ ] #20 To-Do List with File Storage

---

*Happy coding! 🚀 — Complete each phase before moving to the next.*
