"""
Day 25 — JSON Files
Problem:
========
Create a Python dictionary of a library with 5 books. Each book has: title, author, year, available (bool).
Save it to library.json using the json module.
Read it back and print each book's details.
Mark one book as unavailable (update available to False) and save the file again.
Add a new book and save. Print the total count of available books.
Concepts: json.dump(), json.load(), reading/writing JSON, nested structures
"""
import json
from pprint import pprint

library = {
    "book1": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "available": True
    },
    "book2": {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "available": False
    },
    "book3": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "available": True
    },
    "book4": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "year": 1813,
        "available": True
    },
    "book5": {
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "year": 1851,
        "available": False
    }
}

# Save to a JSON file
"""
with open("library.json", "w",encoding="utf-8") as json_file:
    json.dump(library, json_file, indent=4)

# Print json data

with open("library.json", "r",encoding="utf-8") as json_file:
    data = json.load(json_file)
pprint(data)                        # using pprint for printing beautifully
"""

# Mark one book as unavailable (update available to False) and save the file again.
"""
file_name = "library.json"

# Read the existing JSON data
with open(file_name, "r", encoding="utf-8") as json_file:
    books_data = json.load(json_file)

books_data["book3"]["available"] = True

# Write the updated dictionary back to the file
with open(file_name, "w", encoding="utf-8") as json_file:
    json.dump(books_data, json_file, indent=4)

print("Successfully updated book3 availability!")
"""

# Add a new book and save. Print the total count of available books.

"""
file_name = "library.json"
# 1. Read existing data
with open(file_name, "r", encoding="utf-8") as file:
    library = json.load(file)

# 2. Define and append the new book
library["book6"] = {
    "author": "J.R.R. Tolkien",
    "available": True,
    "title": "The Hobbit",
    "year": 1937
}

# 3. Write back to the file
with open(file_name, "w", encoding="utf-8") as file:
    json.dump(library, file, indent=4)

print("Added 'The Hobbit' as book6!")
"""

# Print the count and availability
with open("library.json", "r") as file:
    library = json.load(file)

available_titles = [b["title"] for b in library.values() if b["available"]]
unavailable_titles = [b["title"] for b in library.values() if not b["available"]]
total_books = len(library.items())
print(f"Available: {available_titles}")
print(f"Unavailable: {unavailable_titles}")
print(f"Total books: {total_books}")