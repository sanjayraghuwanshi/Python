# 🐍 8-Week Python Practice Plan
### Focus: Lists · Dictionaries · File Handling · OOP · Projects
**Time commitment:** ~1 hour/day | **Start:** Day 1 (your Day 1)

---

## 📌 How to Use This Plan
- One problem per day. Read it, think before you code.
- Each week ends with a **mini-project** that combines everything learned that week.
- Solutions are yours to figure out — use Google, Python docs, or ask Claude for hints.
- By Week 8, you'll build a full-featured console application from scratch.

---

---

# 🗓️ WEEK 1 — Lists & Loops Deep Dive

**Goal:** Get fluent with Python lists — creating, modifying, iterating, and slicing them.

---

### Day 1 — List Basics & Indexing
**Problem:**
You are managing a bookshelf. Create a list of 5 book titles. Then:
1. Print the first and last book using indexing.
2. Add a new book at the end.
3. Insert a book at position 2.
4. Remove the third book.
5. Print the final list and its length.

**Concepts:** `append()`, `insert()`, `remove()`, indexing, `len()`

---

### Day 2 — Slicing & List Operations
**Problem:**
Given a list of 10 numbers (you choose them), do the following:
1. Print the first 4 numbers.
2. Print the last 3 numbers.
3. Print every alternate number.
4. Reverse the list without using `.reverse()`.
5. Print the sorted version without modifying the original list.

**Concepts:** Slicing `[start:end:step]`, `sorted()`, `reversed()`

---

### Day 3 — Loops Over Lists
**Problem:**
You have a list of student scores: `[78, 92, 55, 88, 73, 61, 95, 49, 83, 70]`
1. Print all scores above 75.
2. Count how many students passed (score ≥ 60).
3. Find the highest and lowest score without using `max()` or `min()`.
4. Calculate the class average.

**Concepts:** `for` loops, conditionals, accumulators

---

### Day 4 — List Comprehensions
**Problem:**
Rewrite the following using list comprehensions (one line each):
1. A list of squares of numbers from 1 to 10.
2. A list of only even numbers from 1 to 20.
3. A list of words from `["apple", "banana", "cherry", "date", "elderberry"]` that have more than 5 characters.
4. A list of uppercase versions of the above filtered words.

**Concepts:** List comprehensions, filtering with conditions

---

### Day 5 — Nested Lists
**Problem:**
Create a 3x3 matrix (a list of lists) representing a tic-tac-toe board filled with `"."`.
1. Print the board in a grid format.
2. Place `"X"` at row 0, col 1 and `"O"` at row 2, col 2.
3. Print the updated board.
4. Write a function `get_row(board, row)` that returns all elements in a given row.
5. Write a function `get_col(board, col)` that returns all elements in a given column.

**Concepts:** Nested lists, indexing with `[i][j]`, functions

---

### Day 6 — List Methods & Sorting
**Problem:**
You have a list of names: `["Zara", "Amit", "Priya", "John", "Meera", "Arjun"]`
1. Sort alphabetically and print.
2. Sort by length of name (shortest first).
3. Sort by length, and for same-length names, sort alphabetically.
4. Find if `"Priya"` is in the list. Print her index.
5. Count how many names start with a vowel.

**Concepts:** `sort()` with `key=`, `in`, `.index()`, string methods

---

### Day 7 — Week 1 Mini Project: Student Grade Manager
**Project:**
Build a console program that manages student grades.

Features:
- Store student names and scores in a list (you can hardcode 8–10 students).
- Display the full list sorted by score (highest first).
- Show the top 3 students.
- Show students who are below average.
- Assign a grade: A (≥90), B (≥75), C (≥60), F (<60) and display it alongside each name.

**Sample output:**
```
=== Grade Report ===
1. Sneha    - 95 - A
2. Rahul    - 88 - B
3. Pooja    - 74 - C
...
Class Average: 76.4
Below Average: [Arjun (61), Dev (55)]
```

---

---

# 🗓️ WEEK 2 — Dictionaries & Data Structures

**Goal:** Master Python dictionaries — the workhorse of real-world Python programs.

---

### Day 8 — Dictionary Basics
**Problem:**
Create a dictionary representing a person's profile:
- Keys: `name`, `age`, `city`, `occupation`
1. Print each key-value pair using a loop.
2. Add a new key `email`.
3. Update the `city` to a different city.
4. Delete the `occupation` key.
5. Check if `"phone"` exists in the dictionary. Print a message either way.

**Concepts:** Dictionary creation, `keys()`, `values()`, `items()`, `del`, `in`

---

### Day 9 — Iterating Dictionaries
**Problem:**
You have a word frequency dictionary:
`{"python": 5, "code": 3, "list": 7, "loop": 2, "dict": 6, "function": 4}`
1. Print all words with frequency > 4.
2. Find the word with the highest frequency.
3. Sort the dictionary by frequency (highest first) and print it.
4. Create a new dictionary with only words that have 4+ letters.

**Concepts:** `.items()`, sorting dicts, dictionary comprehensions

---

### Day 10 — Nested Dictionaries
**Problem:**
Create a dictionary of 3 employees. Each employee has:
- `name`, `department`, `salary`

Example:
```python
employees = {
    "E001": {"name": "Anjali", "department": "HR", "salary": 55000},
    ...
}
```
1. Print each employee's full details.
2. Give everyone in "HR" a 10% salary raise and update their records.
3. Find the highest-paid employee.
4. List all unique departments.

**Concepts:** Nested dicts, updating nested values, sets for uniqueness

---

### Day 11 — Dictionary Comprehensions
**Problem:**
1. Create a dictionary of `{number: square}` for numbers 1–10 using a comprehension.
2. From a list of words `["sky", "ocean", "mountain", "river", "cloud"]`, create a dict of `{word: length}`.
3. Filter the above to only include words with length > 4.
4. Invert a dictionary: `{"a": 1, "b": 2, "c": 3}` → `{1: "a", 2: "b", 3: "c"}`.

**Concepts:** Dictionary comprehensions, `.items()`, filtering

---

### Day 12 — Combining Lists & Dictionaries
**Problem:**
You have two lists:
```python
subjects = ["Math", "Science", "English", "History", "PE"]
scores   = [88, 76, 92, 65, 80]
```
1. Combine them into a dictionary using `zip()`.
2. Find the subject with the highest and lowest score.
3. Add a new subject `"Art"` with score `71`.
4. Print subjects where score is above average.
5. Create a sorted list of `(subject, score)` tuples by score.

**Concepts:** `zip()`, `dict()`, tuples, combined data structures

---

### Day 13 — Counting & Grouping with Dictionaries
**Problem:**
Given a sentence (use any long sentence you like — at least 15 words):
1. Count the frequency of each word (case-insensitive, ignore punctuation).
2. Find the top 3 most frequent words.
3. Group words by their first letter into a dictionary of lists.
   Example: `{"a": ["and", "apple"], "b": ["bird"], ...}`
4. Find which letter group has the most words.

**Concepts:** `.get()`, `defaultdict` style logic, string methods, sorting

---

### Day 14 — Week 2 Mini Project: Contact Book
**Project:**
Build a contact book using a dictionary where each contact is stored with name as the key and their details as a nested dictionary.

Features:
- Add a new contact (name, phone, email, city).
- Search for a contact by name (case-insensitive).
- Update a contact's phone or email.
- Delete a contact.
- Display all contacts sorted alphabetically.
- Show all contacts from a given city.

Run it as a menu-driven console app:
```
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Filter by City
7. Exit
```

---

---

# 🗓️ WEEK 3 — Functions & Modular Code

**Goal:** Write clean, reusable functions. Understand arguments, return values, and scope.

---

### Day 15 — Function Basics & Return Values
**Problem:**
Write the following functions:
1. `greet(name)` — returns `"Hello, <name>!"`
2. `celsius_to_fahrenheit(c)` — converts and returns the value.
3. `is_palindrome(word)` — returns `True` if the word reads the same forwards and backwards.
4. `count_vowels(text)` — returns the number of vowels in a string.
5. Test each function with at least 2 inputs and print results.

**Concepts:** `def`, `return`, calling functions

---

### Day 16 — Default & Keyword Arguments
**Problem:**
1. Write `make_greeting(name, greeting="Hello", punctuation="!")` that returns a customized greeting.
   Test with: just a name, name + greeting, all three args.
2. Write `power(base, exponent=2)` that returns base raised to exponent. Default is squaring.
3. Write `describe_person(name, age, city="Unknown")` — test calling it with and without `city`.
4. What happens when you call `make_greeting(greeting="Hi", name="Ravi")`? Try it and explain in a comment.

**Concepts:** Default args, keyword args, argument order

---

### Day 17 — *args and **kwargs
**Problem:**
1. Write `add_all(*numbers)` that accepts any number of arguments and returns their sum.
2. Write `print_profile(**details)` that prints each key-value pair nicely.
   Example call: `print_profile(name="Meera", city="Pune", hobby="Painting")`
3. Write `summarize(*words, **counts)` that prints the list of words and their counts dictionary.
4. Call a function using `*list_var` and `**dict_var` to unpack them as arguments.

**Concepts:** `*args`, `**kwargs`, unpacking

---

### Day 18 — Scope & Lambda Functions
**Problem:**
1. Demonstrate the difference between a local and global variable with a short example.
2. Use the `global` keyword to modify a global variable inside a function. Show before and after.
3. Write a lambda to: square a number, check if a number is even, convert a name to uppercase.
4. Use `map()` with a lambda to square all numbers in `[1, 2, 3, 4, 5]`.
5. Use `filter()` with a lambda to keep only even numbers from `[1, 2, 3, 4, 5, 6, 7, 8]`.

**Concepts:** Scope, `global`, `lambda`, `map()`, `filter()`

---

### Day 19 — Recursion
**Problem:**
1. Write a recursive function `factorial(n)` that computes n!
2. Write a recursive function `fibonacci(n)` that returns the nth Fibonacci number.
3. Write a recursive function `sum_digits(n)` that returns the sum of digits of a number.
   Example: `sum_digits(1234)` → `10`
4. Write a recursive function `flatten(nested_list)` that flattens one level of nesting.
   Example: `[[1,2],[3,4],[5]]` → `[1,2,3,4,5]`

**Concepts:** Recursion, base case, call stack

---

### Day 20 — Functions as First-Class Objects
**Problem:**
1. Store three functions (`add`, `subtract`, `multiply`) in a list. Loop through and call each with `(10, 5)`.
2. Write a function `apply(func, value)` that takes a function and a value, and applies the function to it.
3. Write a function `make_multiplier(n)` that returns a function that multiplies its input by `n`.
   Test: `double = make_multiplier(2)` then `double(7)` should give `14`.
4. Use `sorted()` with a custom `key` function (not lambda) to sort a list of dictionaries by a field.

**Concepts:** Higher-order functions, closures, functions as arguments/return values

---

### Day 21 — Week 3 Mini Project: Quiz Game
**Project:**
Build a quiz game using functions and dictionaries.

Structure:
- Store questions as a list of dictionaries: `{"question": "...", "options": [...], "answer": "..."}`
- Create at least 8 questions on any topic you like.
- Functions to write:
  - `display_question(q)` — shows the question and options.
  - `check_answer(user_ans, correct_ans)` — returns True/False.
  - `run_quiz(questions)` — runs through all questions, tracks score.
  - `show_result(score, total)` — prints final score with a message (Excellent/Good/Try Again).
- Shuffle questions each time using `random.shuffle()`.

---

---

# 🗓️ WEEK 4 — File Handling

**Goal:** Read from and write to files. Handle real data stored in `.txt` and `.csv` formats.

---

### Day 22 — Reading & Writing Text Files
**Problem:**
1. Write a program that creates a file `notes.txt` and writes 5 lines of any text to it.
2. Read the file back and print each line with its line number.
3. Append 3 more lines to the same file without overwriting.
4. Count the total number of lines and words in the file.
5. Search the file for a word (user input) and print all lines containing it.

**Concepts:** `open()`, `write()`, `read()`, `readlines()`, `with` statement, modes `r/w/a`

---

### Day 23 — Working with File Paths & Multiple Files
**Problem:**
1. Create three files: `fruits.txt`, `veggies.txt`, `grains.txt` — each with 5 items (one per line).
2. Read all three files and combine their contents into one list.
3. Remove duplicates and sort the combined list.
4. Write the final sorted list to a new file `all_foods.txt`.
5. Print a summary: how many items came from each file.

**Concepts:** Looping over files, combining data, deduplication, `os.path`

---

### Day 24 — CSV Files
**Problem:**
Create a CSV file `students.csv` with columns: `Name, Age, Grade, Score`.
Add at least 8 rows of data manually in the file or via code.
Then write a program to:
1. Read the CSV and print all rows neatly.
2. Find the student with the highest score.
3. Filter and print all students with grade `"A"`.
4. Calculate the average score.
5. Add a new student row and save the updated CSV.

**Concepts:** `csv` module, `csv.reader()`, `csv.writer()`, `DictReader`

---

### Day 25 — JSON Files
**Problem:**
1. Create a Python dictionary of a library with 5 books. Each book has: `title`, `author`, `year`, `available` (bool).
2. Save it to `library.json` using the `json` module.
3. Read it back and print each book's details.
4. Mark one book as unavailable (update `available` to `False`) and save the file again.
5. Add a new book and save. Print the total count of available books.

**Concepts:** `json.dump()`, `json.load()`, reading/writing JSON, nested structures

---

### Day 26 — Error Handling in File Operations
**Problem:**
1. Try to open a file that doesn't exist. Handle the `FileNotFoundError` gracefully.
2. Write a function `safe_read(filename)` that returns file contents or a friendly error message.
3. Write a function `safe_write(filename, data)` that catches permission or OS errors.
4. Create a log file `errors.log`. Every time an error occurs in your program, append a timestamped message to the log.
5. Demonstrate all error scenarios by intentionally triggering them and showing the log.

**Concepts:** `try/except/finally`, multiple exception types, `datetime` for timestamps

---

### Day 27 — File-Based Data Persistence
**Problem:**
Build a simple to-do list that saves and loads data from a file `todos.json`.
Features:
- Load existing todos when the program starts.
- Add a new todo (text + `done: false`).
- Mark a todo as done.
- Delete a todo.
- Show all todos (with done/pending status).
- Save automatically after every change.

All data must persist between program runs — if you close and reopen, todos must still be there.

**Concepts:** JSON persistence, full CRUD with files

---

### Day 28 — Week 4 Mini Project: Expense Tracker
**Project:**
Build an expense tracker that stores data in a CSV file `expenses.csv`.

Features:
- Add an expense: date (auto-filled), category, description, amount.
- View all expenses in a formatted table.
- Filter by category (e.g., show only "Food" expenses).
- Show total spending by category.
- Show this month's total spending.
- Export a summary report to `report.txt`.

Menu-driven console app. Data must persist across sessions.

---

---

# 🗓️ WEEK 5 — Object-Oriented Programming: Foundations

**Goal:** Understand classes, objects, attributes, and methods — the core of OOP.

---

### Day 29 — Classes & Objects
**Problem:**
Create a class `Car` with attributes: `make`, `model`, `year`, `color`, `speed` (starts at 0).
Methods:
- `accelerate(amount)` — increases speed.
- `brake(amount)` — decreases speed, min 0.
- `describe()` — prints a summary of the car.
- `is_moving()` — returns True if speed > 0.

Create 2 Car objects. Accelerate one, brake the other. Print their descriptions.

**Concepts:** `class`, `__init__`, `self`, methods, object creation

---

### Day 30 — The `__str__` and `__repr__` Methods
**Problem:**
1. Add `__str__` to your `Car` class so `print(car)` gives a nice readable output.
2. Add `__repr__` so that the developer-friendly representation shows the class and key attributes.
3. Create a class `Book` with `title`, `author`, `pages`. Add `__str__` and `__repr__`.
4. Create a list of 3 Book objects and print the list — see how `__repr__` is used automatically.
5. Add a `__len__` method to `Book` that returns the number of pages.

**Concepts:** Dunder/magic methods, `__str__`, `__repr__`, `__len__`

---

### Day 31 — Class Variables vs Instance Variables
**Problem:**
Create a class `Employee` with:
- Class variable: `company_name`, `employee_count` (auto-increments with each new object).
- Instance variables: `name`, `department`, `salary`.
- Method `give_raise(percent)` — updates salary.
- Class method `get_employee_count()` — returns total employees created.
- Static method `is_valid_salary(amount)` — returns True if amount > 0.

Create 3 employees. Give one a raise. Print count and details.

**Concepts:** Class vs instance variables, `@classmethod`, `@staticmethod`

---

### Day 32 — Inheritance
**Problem:**
Create a base class `Animal` with attributes `name`, `sound` and a method `speak()` that prints `"<name> says <sound>"`.

Create subclasses:
- `Dog` — adds method `fetch(item)`.
- `Cat` — adds method `purr()`.
- `Bird` — adds attribute `can_fly` and method `fly_status()`.

Override `speak()` in `Dog` to add `"*wags tail*"` at the end.
Create one of each animal and demonstrate all methods.

**Concepts:** Inheritance, `super()`, method overriding, `isinstance()`

---

### Day 33 — Multiple Inheritance & MRO
**Problem:**
1. Create two classes: `Flyable` (method: `fly()`) and `Swimmable` (method: `swim()`).
2. Create a class `Duck` that inherits from both and also has a `quack()` method.
3. Create a class `FlyingFish` that inherits from `Flyable` and `Swimmable`.
4. Print the MRO (Method Resolution Order) of `Duck` using `Duck.__mro__`.
5. Add a `move()` method to both parent classes. Call `Duck().move()` — which one runs? Why? Add a comment explaining.

**Concepts:** Multiple inheritance, MRO, `super()`, diamond problem

---

### Day 34 — Encapsulation & Properties
**Problem:**
Create a class `BankAccount` with:
- Private attribute `__balance` (starts at 0).
- `deposit(amount)` — validates amount > 0.
- `withdraw(amount)` — validates against balance and amount > 0.
- `@property balance` — returns the current balance.
- `@balance.setter` — prevents direct invalid setting.
- `transaction_history` — list of all transactions with type and amount.
- `show_history()` — prints the full transaction log.

**Concepts:** Encapsulation, name mangling, `@property`, `@setter`

---

### Day 35 — Week 5 Mini Project: Library Management System
**Project:**
Build a Library Management System using OOP.

Classes to build:
- `Book`: title, author, isbn, available.
- `Member`: name, member_id, borrowed_books (list).
- `Library`: collection of books and members.

Library methods:
- `add_book(book)`, `remove_book(isbn)`
- `register_member(member)`
- `borrow_book(member_id, isbn)`
- `return_book(member_id, isbn)`
- `search_book(title_or_author)`
- `show_available_books()`
- `show_member_books(member_id)`

Run as a menu-driven app. Save state to JSON between sessions.

---

---

# 🗓️ WEEK 6 — OOP: Advanced Concepts

**Goal:** Polymorphism, abstract classes, iterators, and design patterns.

---

### Day 36 — Polymorphism
**Problem:**
1. Create a base class `Shape` with a method `area()` that raises `NotImplementedError`.
2. Create subclasses: `Circle`, `Rectangle`, `Triangle` — each implements `area()` and `perimeter()`.
3. Create a list of mixed shapes (3–4 objects). Loop through and print each shape's area using the same method call on all.
4. Write a function `total_area(shapes)` that accepts a list of any shapes and returns total area.
5. Add `__str__` to each shape so they print nicely.

**Concepts:** Polymorphism, duck typing, `NotImplementedError`

---

### Day 37 — Abstract Classes
**Problem:**
Rewrite Day 36 using the `abc` module properly.
1. Make `Shape` an abstract class using `ABC` and `@abstractmethod`.
2. Try to instantiate `Shape()` directly and handle the error.
3. Add an abstract method `describe()` to `Shape` that all subclasses must implement.
4. Add a concrete method `compare_area(other)` in the base class that compares itself to another shape.
5. Demonstrate that all subclasses work correctly.

**Concepts:** `abc`, `ABC`, `@abstractmethod`, abstract vs concrete methods

---

### Day 38 — Iterators & Generators
**Problem:**
1. Create a class `Countdown` that is an iterator (implements `__iter__` and `__next__`) starting from a given number down to 0.
2. Use it in a `for` loop.
3. Write a generator function `fibonacci_gen(limit)` that yields Fibonacci numbers up to `limit`.
4. Write a generator `read_large_file(filename)` that yields one line at a time (memory efficient).
5. Use `next()` manually to get values from a generator and handle `StopIteration`.

**Concepts:** `__iter__`, `__next__`, `yield`, generator functions, lazy evaluation

---

### Day 39 — Operator Overloading
**Problem:**
Create a class `Vector` representing a 2D vector `(x, y)`.
Overload:
- `__add__` for `v1 + v2`
- `__sub__` for `v1 - v2`
- `__mul__` for `v1 * scalar`
- `__eq__` for `v1 == v2`
- `__abs__` for magnitude using `abs(v)`
- `__str__` for pretty printing

Create several vectors and test all operations. Create a list of vectors and sort them by magnitude.

**Concepts:** Operator overloading, dunder methods, `__add__`, `__eq__`, etc.

---

### Day 40 — Decorators
**Problem:**
1. Write a decorator `@timer` that prints how long a function takes to run.
2. Write a decorator `@logger` that prints the function name and arguments every time it's called.
3. Write a decorator `@validate_positive` that ensures all numeric arguments to a function are positive, raising `ValueError` otherwise.
4. Apply multiple decorators to a single function and observe the order.
5. Write a decorator factory `@repeat(n)` that runs a function `n` times.

**Concepts:** Decorators, `functools.wraps`, closures, stacking decorators

---

### Day 41 — Exception Handling & Custom Exceptions
**Problem:**
1. Create a custom exception `InsufficientFundsError` with a meaningful message.
2. Create `InvalidAgeError` and `NegativeAmountError`.
3. Use them in a `BankAccount` class — raise appropriate custom exceptions in `withdraw()` and a `set_age()` method.
4. Write a function that catches multiple exception types in one `except` block.
5. Write a context manager using `__enter__` and `__exit__` that logs when a code block starts and ends, and catches any exceptions inside.

**Concepts:** Custom exceptions, multiple `except`, context managers, `with`

---

### Day 42 — Week 6 Mini Project: Online Store Inventory
**Project:**
Build an inventory management system for an online store.

Classes:
- `Product`: id, name, category, price, stock.
- `ElectronicProduct(Product)`: adds `warranty_years`.
- `ClothingProduct(Product)`: adds `size`, `color`.
- `Inventory`: manages all products.

Inventory features:
- Add/remove products.
- Search by name or category.
- Update stock and price.
- Low stock alert (stock < 5).
- Total inventory value calculator.
- Generate a stock report saved to `inventory_report.txt`.

Persistence via JSON. Menu-driven interface.

---

---

# 🗓️ WEEK 7 — Putting It All Together

**Goal:** Build bigger, more real-world projects combining all skills.

---

### Day 43 — Regular Expressions
**Problem:**
1. Validate an email address format using `re`.
2. Extract all phone numbers from a paragraph of text.
3. Find all hashtags in a social media post string.
4. Replace all occurrences of swear words (pick safe placeholders) with `***`.
5. Extract all dates in format `DD-MM-YYYY` from a block of text.

**Concepts:** `re` module, `re.match`, `re.findall`, `re.sub`, patterns

---

### Day 44 — Working with Dates & Times
**Problem:**
1. Print today's date and time in multiple formats using `datetime`.
2. Calculate the number of days between two dates.
3. Add 30 days to today's date.
4. Write a function `age_calculator(birthdate_str)` that returns someone's age in years.
5. Build a deadline tracker: given a list of tasks with due dates, print which are overdue, due today, and upcoming.

**Concepts:** `datetime`, `timedelta`, `strftime`, `strptime`

---

### Day 45 — Modules & Packages
**Problem:**
Organize a previous project (like the Contact Book or Quiz Game) into multiple files:
1. `models.py` — contains class definitions.
2. `utils.py` — contains helper functions.
3. `storage.py` — contains file read/write logic.
4. `main.py` — runs the application.

Use `import` and `from ... import` correctly.
Add `if __name__ == "__main__":` guard.
Write a brief `README.md` explaining how to run the project.

**Concepts:** Modular code, imports, `__name__`, project structure

---

### Day 46 — List/Dict Advanced Patterns
**Problem:**
1. Given a list of transaction dictionaries (each with `type`, `amount`, `date`), group transactions by type using `defaultdict`.
2. Use `Counter` from `collections` to find the top 5 most common words in a paragraph.
3. Use `namedtuple` to represent a 2D point and compute distances.
4. Use `deque` to build a browser history simulation (back/forward navigation).
5. Use `ChainMap` to merge two config dictionaries with priority.

**Concepts:** `collections` module — `defaultdict`, `Counter`, `namedtuple`, `deque`, `ChainMap`

---

### Day 47 — Comprehensions Masterclass
**Problem:**
All answers must use comprehensions (no regular loops):
1. From a list of sentences, create a list of word counts per sentence.
2. Transpose a 3x3 matrix (list of lists) using a list comprehension.
3. Create a dictionary of `{word: [positions]}` for each word in a sentence (where it appears).
4. Create a set of all unique characters in a paragraph (excluding spaces).
5. Flatten a deeply nested list `[[1,[2,3]],[4,[5,[6]]]]` into `[1,2,3,4,5,6]` — hint: this needs recursion + comprehension.

**Concepts:** Nested comprehensions, set comprehensions, dict comprehensions

---

### Day 48 — Testing Your Code
**Problem:**
1. Install and use `unittest` (built-in). Write tests for your `BankAccount` class from Day 34.
2. Test: valid deposit, valid withdrawal, overdraft rejection, invalid (negative) amounts.
3. Write a test for your `is_palindrome()` function — include edge cases (empty string, single char, mixed case).
4. Write a test that checks file creation and content for your to-do file system from Day 27.
5. Run all tests and make sure they pass. Fix any bugs you find.

**Concepts:** `unittest`, `TestCase`, `assertEqual`, `assertRaises`, test-driven thinking

---

### Day 49 — Week 7 Mini Project: Personal Finance Dashboard
**Project:**
Build a personal finance tracker combining everything.

Features:
- `Transaction` class with date, amount, category, description, type (income/expense).
- `FinanceDashboard` class that manages all transactions.
- Load/save to JSON.
- Add income or expense.
- Monthly summary: total income, total expense, net savings.
- Category-wise breakdown.
- Filter transactions by date range or category.
- Export monthly report to `finance_report_<month>.txt`.

This should feel like a real mini-application.

---

---

# 🗓️ WEEK 8 — Capstone Project

**Goal:** Build one complete, polished Python application that showcases everything.

---

### Day 50 — Project Planning
**Task (No coding today):**
Plan your capstone project. Choose ONE from the options below (or propose your own):

**Option A — Student Management System**
Full CRUD for students, courses, grades, attendance. OOP, file persistence, reports.

**Option B — Inventory & Billing System**
Products, customers, invoices, stock management. CSV/JSON. Auto-bill generation.

**Option C — Personal Task Manager (CLI)**
Projects, tasks, priorities, deadlines, tags. Full OOP. Statistics dashboard.

Write a planning document with:
- Features list
- Classes and their responsibilities
- File structure
- Data storage format

---

### Day 51 — Core Models
**Task:** Build all your classes with `__init__`, `__str__`, properties. No app logic yet — just the data layer. Test each class works independently.

---

### Day 52 — Storage Layer
**Task:** Build the complete file I/O system. All data loads on startup, saves on change. Test that data persists correctly between runs.

---

### Day 53 — Business Logic
**Task:** Implement all the main features (add, edit, delete, search, filter, calculate). Write helper functions in a `utils.py`. Keep classes clean.

---

### Day 54 — User Interface (Console)
**Task:** Build the full menu-driven console UI. Each menu option calls the right method. Input validation everywhere — no crashes from bad input. Clear output formatting.

---

### Day 55 — Reports & Export
**Task:** Add all reporting features. Generate nicely formatted `.txt` reports with summaries. Test all edge cases — empty data, single items, large data sets.

---

### Day 56 — Testing & Bug Fixes
**Task:** Write unit tests for every major function. Run them. Fix all bugs. Try to break your own program with weird inputs. Polish error messages.

---

### Day 57 — Final Polish & README
**Task:** Clean up your code — consistent naming, remove dead code, add comments where needed. Write a proper `README.md` with:
- Project description
- How to run it
- Features list
- Sample screenshots (describe output)
- What you learned

---

### Day 58 — Reflection & What's Next

Congratulations — you made it! 🎉

**Today's task:** No coding. Instead, look back and reflect:
1. Open your Day 8 code and your Day 55 code. Notice the difference.
2. Write (in a text file or notebook) 3 things you found hardest and how you got past them.
3. Write 3 things you're most proud of from this journey.

**Where to go from here:**
- **Web Development** → Learn Flask or FastAPI to build web apps with Python.
- **Data Science** → Learn pandas, NumPy, matplotlib for data analysis.
- **Automation** → Learn `selenium`, `requests`, `BeautifulSoup` to automate tasks.
- **Databases** → Learn SQLite with Python (`sqlite3` or `SQLAlchemy`).
- **APIs** → Build or consume REST APIs using `requests` and Flask.
- **Open Source** → Find a beginner-friendly Python project on GitHub and contribute.

**The best next step:** Pick one area, build one real project in it. That's how you go from learning Python to *using* Python.

---

---

## 📚 Quick Reference Cheatsheet

| Topic | Key Functions/Concepts |
|---|---|
| Lists | `append`, `insert`, `remove`, `pop`, `sort`, `sorted`, slicing, comprehensions |
| Dictionaries | `get`, `update`, `items`, `keys`, `values`, `pop`, comprehensions |
| File Handling | `open()`, `with`, modes `r/w/a`, `csv`, `json` |
| OOP | `class`, `__init__`, `self`, inheritance, `super()`, `@property`, `@classmethod` |
| Error Handling | `try/except/finally`, custom exceptions, `raise` |
| Functional | `lambda`, `map()`, `filter()`, `sorted(key=)` |
| Useful Modules | `os`, `sys`, `datetime`, `random`, `re`, `json`, `csv`, `collections`, `abc`, `unittest` |

---

*Built for a focused 8-week Python journey. One day at a time. 🐍*
