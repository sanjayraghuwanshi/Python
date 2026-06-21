"""
The __str__ and __repr__ Methods
Problem:

Add __str__ to your Car class so print(car) gives a nice readable output.
Add __repr__ so that the developer-friendly representation shows the class and key attributes.
Create a class Book with title, author, pages. Add __str__ and __repr__.
Create a list of 3 Book objects and print the list — see how __repr__ is used automatically.
Add a __len__ method to Book that returns the number of pages.
Concepts: Dunder/magic methods, __str__, __repr__, __len__
"""

class Car:
    def __init__(self, make: str, model: str, year: int, color: str):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def accelerate(self, amount: float):
        self.speed += amount

    def brake(self, amount: float):
        self.speed = max(0, self.speed - amount)

    def describe(self):
        print(f"{self.year} {self.color} {self.make} {self.model} (Current Speed: {self.speed} km/h)")

    def is_moving(self) -> bool:
        return self.speed > 0

    def __repr__(self):
        return f"Car({self.make}, {self.model}, {self.year}, {self.color})"
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color} {self.speed} km/h"

# Create 2 car objects
car1 = Car("Honda", "Camry", 2024, "Silver")
car2 = Car("Tata", "Mustang", 2023, "Red")

print(str(car1))
print(repr(car2))

"""
Create a class Book with title, author, pages. Add __str__ and __repr__.
Create a list of 3 Book objects and print the list — see how __repr__ is used automatically.
Add a __len__ method to Book that returns the number of pages.
"""
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.pages})"
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    def __len__(self):
        return self.pages

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 200)
book2 = Book("Pride and Prejudice", "Jane Austen", 225)
book3 = Book("Moby-Dick", "Herman Melville", 362)

print(book1)
print(f"Number of pages in book1 : {len(book1)}")
print(f"Number of pages in book2 : {len(book2)}")
print(f"Number of pages in book3 : {len(book3)}")