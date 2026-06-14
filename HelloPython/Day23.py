"""
Day 23 — Working with File Paths & Multiple Files
Problem:
========
1. Create three files: fruits.txt, veggies.txt, grains.txt — each with 5 items (one per line).
2. Read all three files and combine their contents into one list.
3. Remove duplicates and sort the combined list.
4. Write the final sorted list to a new file all_foods.txt.
5. Print a summary: how many items came from each file.
Concepts: Looping over files, combining data, deduplication, os.path
"""
import os

with open('fruits.txt', 'w') as fruits:
    fruits.write("Orange\nBanana\nApple\nKiwi\nWatermelon")

with open('veggies.txt', 'w') as veggies:
    veggies.write("Veg1\nVeg2\nVeg3\nVeg4\nVeg5")

with open('grains.txt', 'w') as grains:
    grains.write("Grain1\nGrain2\nGrain3\nGrain4\nGrain5")

with open('fruits.txt', 'r') as fruits:
    print(fruits.read())
with open('veggies.txt', 'r') as veggies:
        print(veggies.read())
with open('grains.txt', 'r') as grains:
        print(grains.read())


text_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('s.txt')]
output_file = "all_foods.txt"
with open(output_file, "w") as output:
    for f in text_files:
        if f == output_file:
            continue
        with open(f, "r") as infile:
            output.write(f"--- Content from {f} ---\n")
            output.write(infile.read())
            output.write("\n\n")
print(f"Successfully combined {len(text_files)} files into {output_file}")

# remove duplicates and sort the file
with open("all_foods.txt", "r") as infile:
    lines = infile.readlines()

unique_sorted_content = sorted(set(line.strip() for line in lines if line.strip() ))

with open("clean_file.txt", "w") as clean_file:
    for item in unique_sorted_content:
        clean_file.write(f"{item} \n")

print(f"Duplicates removed and file sorted Successfully!")

# print a summary of how many foods came from each file
files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('s.txt')]

for f in files:
    with open(f, "r") as infile:
        lines = infile.readlines()
        item_count = len(lines)
        print(f"Total number of items in file {f} : {item_count}")
