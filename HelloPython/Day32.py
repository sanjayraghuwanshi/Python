"""
Day 32 — Inheritance
Problem: Create a base class Animal with attributes name,
sound and a method speak() that prints "<name> says <sound>".

Create subclasses:
Dog — adds method fetch(item).
Cat — adds method purr().
Bird — adds attribute can_fly and method fly_status().
Override speak() in Dog to add "*wags tail*" at the end. Create one of each animal and demonstrate all methods.

Concepts: Inheritance, super(), method overriding, isinstance()
"""


class Animal:
    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    def __init__(self):
        super().__init__("Dog", "Woof")

    def speak(self) -> None:
        print(f"{self.name} says {self.sound} *wags tail*")

    def fetch(self, item: str):
        print(f"{self.name} fetches the {item}")

class Cat(Animal):
    def __init__(self):
        super().__init__("Cat", "Meow")
    def purr(self):
        print(f"{self.name} purrring..purr!")

class Bird(Animal):
    def __init__(self, can_fly: bool = True):
        super().__init__("Bird", "Krrrr")
        self.can_fly = can_fly

    def fly_status(self):
        if self.can_fly:
            print(f"{self.name} can fly")
        else :
            print(f"{self.name} can not fly")

if __name__ == "__main__":
    # Create instances of classes
    dog = Dog()
    cat = Cat()
    bird = Bird(can_fly=True)

# Demonstration base and overridden methods
dog.speak()
cat.speak()
bird.speak()

print("=" * 20)

# Demonstration of subclasses
dog.fetch("ball")   # Output: Dog fetches the ball!
cat.purr()          # Output: Cat is purring... purr...
bird.fly_status()

print("=" * 20)

# Demonstration of isinstance() concept
print(f"Is dog an Animal? {isinstance(dog, Animal)}")  # True
print(f"Is bird a Dog? {isinstance(bird, Dog)}")       # False