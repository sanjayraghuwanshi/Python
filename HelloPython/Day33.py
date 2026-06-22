"""
### Day 33 — Multiple Inheritance & MRO
**Problem:**
1. Create two classes: `Flyable` (method: `fly()`) and `Swimmable` (method: `swim()`).
2. Create a class `Duck` that inherits from both and also has a `quack()` method.
3. Create a class `FlyingFish` that inherits from `Flyable` and `Swimmable`.
4. Print the MRO (Method Resolution Order) of `Duck` using `Duck.__mro__`.
5. Add a `move()` method to both parent classes. Call `Duck().move()` — which one runs? Why? Add a comment explaining.

**Concepts:** Multiple inheritance, MRO, `super()`, diamond problem
"""

# 1. Create two parent classes with fly(), swim(), and move() methods
class Flyable:
    def fly(self):
        print("Flying high in the sky!")

    def move(self):
        print("Moving through the air!")

class Swimmable:
    def swim(self):
        print("Swimming deep in the water!")

    def move(self):
        print("Moving through the water!")

# 2. Create Duck class inheriting from both, plus a quack() method
class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack, quack!")

# 3. Create FlyingFish class inheriting from both Flyable and Swimmable
class FlyingFish(Flyable, Swimmable):
    pass

# --- Execution and Verification ---

# 4. Print the Method Resolution Order (MRO) of Duck
print("Method Resolution Order (MRO) for Duck:")
print(Duck.__mro__)
print("-" * 50)

# 5. Call Duck().move() to see which one runs
duck_instance = Duck()
duck_instance.move()