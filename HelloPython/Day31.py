"""
Day 31 — Class Variables vs Instance Variables
Problem: Create a class Employee with:

Class variable: company_name, employee_count (auto-increments with each new object).
Instance variables: name, department, salary.
Method give_raise(percent) — updates salary.
Class method get_employee_count() — returns total employees created.
Static method is_valid_salary(amount) — returns True if amount > 0.
Create 3 employees. Give one a raise. Print count and details.

Concepts: Class vs instance variables, @classmethod, @staticmethod
"""

class Employee:
    count = 0
    def __init__(self, name, department, salary):
        self.percent = None
        self.name = name
        self.department = department
        self.salary = salary

        Employee.count +=1

    @staticmethod
    def get_employee_count():
        return Employee.count

    @staticmethod
    def is_valid_salary(amount):
        return amount > 0

    def give_raise(self, percent):
        raise_amount = (percent / 100) * self.salary
        self.salary += raise_amount

    def __str__(self):
        return f"Employee Name: {self.name}, Employee Department: {self.department}. Salary: {self.salary}"

emp1 = Employee("Matthew", "HR", 10000)
emp2 = Employee("Gordon", "CS", 15000)
emp3 = Employee("Jim", "PS", 20000)
emp4 = Employee("Olivier", "CS", 25000)
emp5 = Employee("Jordan", "ENG", 30000)

print(f"{emp1} \n{emp2} \n{emp3} \n{emp4} \n{emp5}")

emp1.give_raise(100)
print(emp1)

total_staff = Employee.get_employee_count()
print(f"Total Employees: {total_staff}")
salary_valid = Employee.is_valid_salary(10)
print(f"Salary Valid: {salary_valid}")