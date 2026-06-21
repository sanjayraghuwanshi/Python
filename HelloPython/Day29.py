"""
Day 29 — Classes & Objects
Problem: Create a class Car with attributes: make, model, year, color, speed (starts at 0). Methods:

accelerate(amount) — increases speed.
brake(amount) — decreases speed, min 0.
describe() — prints a summary of the car.
is_moving() — returns True if speed > 0.
Create 2 Car objects. Accelerate one, brake the other. Print their descriptions.

Concepts: class, __init__, self, methods, object creation
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

# Create 2 car objects
car1 = Car("Toyota", "Camry", 2024, "Silver")
car2 = Car("Ford", "Mustang", 2023, "Red")

# Accelerate the first car
car1.accelerate(50)

# Accelerate and then brake the second car to demonstrate braking
car2.accelerate(30)
car2.brake(10)

# Print descriptions
car1.describe()
car2.describe()

# Check if car1 and car2 are moving.
print(car1.is_moving())
print(car2.is_moving())