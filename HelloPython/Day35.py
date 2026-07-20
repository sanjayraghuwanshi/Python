"""
Day 35 — Week 5 Mini Project: Library Management System
Project: Build a Library Management System using OOP.
=================
Classes to build:
=================
Book: title, author, isbn, available.
Member: name, member_id, borrowed_books (list).
Library: collection of books and members.
=================
Library methods:
=================
add_book(book), remove_book(isbn)
register_member(member)
borrow_book(member_id, isbn)
return_book(member_id, isbn)
search_book(title_or_author)
show_available_books()
show_member_books(member_id)
Run as a menu-driven app. Save state to JSON between sessions.
"""
import json
import os

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        # Using a protected attribute to manage status via property
        self._available = available

    @property
    def available(self):
        """Getter: Check if the book is available."""
        return self._available

    @available.setter
    def available(self, status):
        """Setter: Ensures availability is strictly a boolean."""
        if not isinstance(status, bool):
            raise TypeError("Availability must be True or False.")
        self._available = status

    def to_dict(self):
        """Converts object to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "available": self._available
        }


class Member:
    def __init__(self, name, member_id, borrowed_books=None):
        self.name = name
        self.member_id = member_id
        # Stores borrowed book ISBNs internally
        self._borrowed_books = borrowed_books if borrowed_books else []

    @property
    def borrowed_books(self):
        """Getter: Returns a copy of the list to protect the original data structure."""
        return list(self._borrowed_books)

    def borrow_title(self, isbn):
        """Internal helper to add an ISBN to the member's list."""
        if isbn not in self._borrowed_books:
            self._borrowed_books.append(isbn)

    def return_title(self, isbn):
        """Internal helper to remove an ISBN from the member's list."""
        if isbn in self._borrowed_books:
            self._borrowed_books.remove(isbn)

    def to_dict(self):
        """Converts object to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self._borrowed_books
        }


class Library:
    def __init__(self, storage_file="library_data.json"):
        self.storage_file = storage_file
        self.books = {}  # Format: {isbn: Book object}
        self.members = {}  # Format: {member_id: Member object}
        self.load_data()

    def add_book(self, book):
        """Adds a new book to the library catalog."""
        if book.isbn in self.books:
            print(f"❌ Error: Book with ISBN {book.isbn} already exists.")
            return False
        self.books[book.isbn] = book
        self.save_data()
        print(f"✅ Book '{book.title}' added successfully!")
        return True

    def remove_book(self, isbn):
        """Removes a book from the catalog if it isn't currently borrowed."""
        if isbn not in self.books:
            print("❌ Error: Book not found.")
            return False
        if not self.books[isbn].available:
            print("❌ Error: Cannot remove a book that is currently borrowed.")
            return False

        del self.books[isbn]
        self.save_data()
        print("✅ Book removed successfully.")
        return True

    def register_member(self, member):
        """Registers a new library user."""
        if member.member_id in self.members:
            print(f"❌ Error: Member ID {member.member_id} is already taken.")
            return False
        self.members[member.member_id] = member
        self.save_data()
        print(f"✅ Member '{member.name}' registered successfully!")
        return True

    def borrow_book(self, member_id, isbn):
        """Handles borrowing a book logic."""
        if member_id not in self.members:
            print("❌ Error: Member not registered.")
            return False
        if isbn not in self.books:
            print("❌ Error: Book does not exist in this library.")
            return False

        book = self.books[isbn]
        member = self.members[member_id]

        if not book.available:
            print(f"❌ Error: '{book.title}' is already borrowed by someone else.")
            return False

        # Execute borrow transaction
        book.available = False
        member.borrow_title(isbn)
        self.save_data()
        print(f"🎉 Success: '{book.title}' checked out to {member.name}.")
        return True

    def return_book(self, member_id, isbn):
        """Handles returning a borrowed book."""
        if member_id not in self.members:
            print("❌ Error: Member not registered.")
            return False

        member = self.members[member_id]
        if isbn not in member.borrow_books:
            print("❌ Error: This member did not borrow this book.")
            return False

        # Execute return transaction
        book = self.books[isbn]
        book.available = True
        member.return_title(isbn)
        self.save_data()
        print(f"🎉 Success: '{book.title}' returned successfully.")
        return True

    def search_book(self, query):
        """Searches books by matching strings in title or author."""
        query = query.lower()
        results = [b for b in self.books.values() if query in b.title.lower() or query in b.author.lower()]

        if not results:
            print("🔍 No matching books found.")
            return

        print(f"\n🔍 Found {len(results)} matching book(s):")
        for b in results:
            status = "Available" if b.available else "Borrowed"
            print(f"- {b.title} by {b.author} [ISBN: {b.isbn}] ({status})")

    def show_available_books(self):
        """Displays all items currently on the shelves."""
        available_books = [b for b in self.books.values() if b.available]
        if not available_books:
            print("📚 No books are currently available on shelves.")
            return

        print("\n📚 Available Books:")
        for b in available_books:
            print(f"- {b.title} by {b.author} [ISBN: {b.isbn}]")

    def show_member_books(self, member_id):
        """Lists titles currently held by a specific member."""
        if member_id not in self.members:
            print("❌ Error: Member not found.")
            return

        member = self.members[member_id]
        if not member.borrowed_books:
            print(f"👤 {member.name} has no borrowed books.")
            return

        print(f"\n👤 Books borrowed by {member.name}:")
        for isbn in member.borrowed_books:
            book = self.books.get(isbn)
            if book:
                print(f"- {book.title} by {book.author} [ISBN: {isbn}]")

    def save_data(self):
        """Serializes current memory state into a JSON file."""
        data = {
            "books": {isbn: b.to_dict() for isbn, b in self.books.items()},
            "members": {mid: m.to_dict() for mid, m in self.members.items()}
        }
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        """Loads data from file backup if it exists."""
        if not os.path.exists(self.storage_file):
            return
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)

                for isbn, b_data in data.get("books", {}).items():
                    self.books[isbn] = Book(b_data["title"], b_data["author"], b_data["isbn"], b_data["available"])

                for mid, m_data in data.get("members", {}).items():
                    self.members[mid] = Member(m_data["name"], m_data["member_id"], m_data["borrowed_books"])
        except (json.JSONDecodeError, KeyError):
            print("⚠️ Warning: Data file corrupted. Starting with an empty library.")


# Menu Implementation
def main():
    library = Library()

    while True:
        print("\n=== 🏛️ LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register Member")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Search Book")
        print("7. Show Available Books")
        print("8. Show Member's Borrowed Books")
        print("9. Exit")

        choice = input("Enter choice (1-9): ").strip()

        if choice == "1":
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            if title and author and isbn:
                library.add_book(Book(title, author, isbn))
            else:
                print("❌ All fields are required.")

        elif choice == "2":
            isbn = input("Enter ISBN of the book to remove: ").strip()
            library.remove_book(isbn)

        elif choice == "3":
            name = input("Enter member name: ").strip()
            member_id = input("Enter unique Member ID: ").strip()
            if name and member_id:
                library.register_member(Member(name, member_id))
            else:
                print("❌ All fields are required.")

        elif choice == "4":
            member_id = input("Enter Member ID: ").strip()
            isbn = input("Enter Book ISBN: ").strip()
            library.borrow_book(member_id, isbn)

        elif choice == "5":
            member_id = input("Enter Member ID: ").strip()
            isbn = input("Enter Book ISBN: ").strip()
            library.return_book(member_id, isbn)

        elif choice == "6":
            query = input("Enter search keyword (Title/Author): ").strip()
            library.search_book(query)

        elif choice == "7":
            library.show_available_books()

        elif choice == "8":
            member_id = input("Enter Member ID: ").strip()
            library.show_member_books(member_id)

        elif choice == "9":
            print("👋 Library closed. Data saved securely.")
            break
        else:
            print("❌ Invalid input. Please pick a number from 1 to 9.")

if __name__ == "__main__":
    main()