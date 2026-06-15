"""
Day 24 — CSV Files
Problem:
Create a CSV file students.csv with columns: Name, Age, Grade, Score.
Add at least 8 rows of data manually in the file or via code. Then write a program to:
  -  Read the CSV and print all rows neatly.
  -  Find the student with the highest score.
  -  Filter and print all students with grade "A".
  -  Calculate the average score.
  -  Add a new student row and save the updated CSV.
Concepts: csv module, csv.reader(), csv.writer(), DictReader
"""

import csv

headers = ["Name", "Age", "Grade", "Score"]

data = [
    ["Alice", 26, 8, "A"],
    ["Bob", 27, 7, "A"],
    ["Charlie", 28, 9, "A"],
    ["Alpha", 28, 10, "D"],
    ["Beta", 29, 11, "E"],
    ["Gama", 29, 12, "F"],
    ["North", 24, 5, "G"],
    ["South", 23, 9, "H"],
]

# Write content into a csv file
with open("students.csv", "w", newline="", encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(headers)
    writer.writerows(data)

# Print content of students.csv
with open("students.csv", 'r') as students:
        print(students.read())

# Print students with highest grade.
with open("students.csv", "r") as infile:
    reader = csv.DictReader(infile)

    highest_grade = min(reader, key=lambda row: row["Score"])

print(f"The student with the highest score is {highest_grade['Name']} ({highest_grade['Score']}).")

# Print students with grade A
with open("students.csv", "r") as infile:
    reader = csv.DictReader(infile)
    print(f"Students with grade A:")
    for row in reader:
        if row["Score"] == "A":
            print(f"- {row['Name']} (Age: {row['Age']}, Grade Level: {row['Grade']})")


# Calculate average score
# ========================
# Mapping letters to numerical values (A is highest, H is lowest)
grade_mapping = {'A': 8, 'B': 7, 'C': 6, 'D': 5, 'E': 4, 'F': 3, 'G': 2, 'H': 1}
# Reverse mapping to find the letter back from a number
reverse_mapping = {v: k for k, v in grade_mapping.items()}

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    # Convert each score to its numerical value
    scores = [grade_mapping[row['Score']] for row in reader]

if scores:
    average = sum(scores) / len(scores)
    # Round to the nearest whole number to find the representative letter
    avg_letter = reverse_mapping.get(round(average), "N/A")

    print(f"\n=====Average score=====")
    print(f"Numerical Average: {average}")
    print(f"Closest Letter Grade: {avg_letter}")

# Add a new student row and save the updated CSV.
# The data for the new student
new_student = ['Zeta', 25, 10, 'B']

# Open in 'a' (append) mode
with open('students.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print("\nNew student row added successfully.")