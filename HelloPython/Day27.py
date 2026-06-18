"""
Day 27 — File-Based Data Persistence
Problem: Build a simple to-do list that saves and loads data from a file todos.json.
###################################################################################
Features:
Load existing todos when the program starts.
Add a new todo (text + done: false).
Mark a todo as done.
Delete a todo.
Show all todos (with done/pending status).
Save automatically after every change.
All data must persist between program runs — if you close and reopen, todos must still be there.

Concepts: JSON persistence, full CRUD with files
"""

import json

#todo = ["Buy veggies", "Do coding practice", "workout"]

def load_todos():
    try:
        with open("todos.json", "r") as file:
            current_todos = json.load(file)
            if isinstance(current_todos, list):
                return current_todos
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass
    return []

def save_todos(todos):
    with open("todos.json", "w") as file:
        json.dump(todos, file, indent=4)

def add_todo(text, done = False):
    text = text.strip()
    if not text:
        return

    current_todos = load_todos()

    for todo in current_todos:
        if todo["task"].lower() == text.lower():
            todo["completed"] = done
            save_todos(current_todos)
            print(f"Updated status for {text} to {done}")
            return

    new_task = {"task": text, "completed": done}
    current_todos.append(new_task)
    save_todos(current_todos)
    print(f"New task added : '{text}'")

def remove_todo(text):
    text = text.strip()
    current_todos = load_todos()

    updated_todos = [todo for todo in current_todos if todo["task"].lower() != text.lower()]

    if len(updated_todos) == len(current_todos):
        print(f" Task '{text}' not found.")
    else:
        save_todos(updated_todos)
        print(f"Removed task '{text}' from todos.")

"""
add_todo("Buy Food", False)
add_todo("Workout", True)
add_todo("Code Practice", True)
remove_todo("Buy Food")
"""