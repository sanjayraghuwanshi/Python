"""
Day 28 — Week 4 Mini Project: Expense Tracker
Project: Build an expense tracker that stores data in a CSV file expenses.csv.

Features:
========
Add an expense: date (auto-filled), category, description, amount.
View all expenses in a formatted table.
Filter by category (e.g., show only "Food" expenses).
Show total spending by category.
Show this month's total spending.
Export a summary report to report.txt.
Menu-driven console app. Data must persist across sessions.
"""
import csv
from datetime import datetime

def add_expense(category: object, description: object, amount: object) -> None:
    headers = ["Date", "Category", "Description", "Amount"]
    data = {
        "Date": datetime.now().strftime("%d/%m/%Y"),
        "Category": category.strip(),
        "Description": description.strip(),
        "Amount": amount
        }

    with open("expenses.csv", "a", newline="", encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)

            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    print("Expenses Added Successfully!")

#add_expense("Fitness", "Protein", 5000) - Testing add_expense function
#add_expense("Rent", "June Month", 15000)

def view_expenses():
    with open("expenses.csv", 'r') as infile:
        print(infile.read())

#view_expenses()

def print_filtered_expenses(column_name, filter_value):
    try:
        with open("expenses.csv", 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)

            print(f"\n--- Showing expenses where {column_name} = {filter_value} ---\n")

            found = False
            for row in reader:
                if row[column_name].strip().lower() == filter_value.strip().lower():
                    print(f"Date: {row['Date']} | Description: {row['Description']} | Amount: {row['Amount']}")
                    found = True

            if not found:
                print("No matching records found.")

    except FileNotFoundError:
        print("The file expenses.csv does not exist yet. Add some data first!")

#print_filtered_expenses("Category", "Rent") #Testing filtered view function

def show_total_for_category(target_category):
    target_category = target_category.strip().lower()
    total_sum = 0
    match_found = False
    try:
        with open("expenses.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Check if the current row matches the filtered category
                if row["Category"].strip().lower() == target_category:
                    match_found = True
                    try:
                        total_sum += int(row["Amount"])
                    except ValueError:
                        continue  # Skip rows with corrupted amount data

        # Print the filtered result
        print(f"\n--- Filtered Total ---")
        if match_found:
            # Capitalize the category name nicely for display
            print(f"Total spent on '{target_category.title()}': ₹{total_sum}")
        else:
            print(f"No expenses found for the category: '{target_category}'")
    except FileNotFoundError:
        print("The file expenses.csv does not exist yet.")

#show_total_for_category("Rent") # Checking the function

def total_spending():
    total_sum = 0
    with open("expenses.csv", 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # Check if the current row matches the filtered category
            try:
                total_sum += int(row["Amount"])
            except ValueError:
                continue  # Skip rows with corrupted amount data
    return f"Total Amount Spend This Month : {total_sum}"

# print(total_spending()) # printing total spending.

def export_report_to_txt():
    try:
        with open("expenses.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            total_spend = 0
            transaction_count = 0
            category_totals = {}

            for row in reader:
                try:
                    amount = int(row["Amount"])
                except ValueError:
                    continue  # Skip corrupt rows

                total_spend += amount
                transaction_count += 1

                category = row["Category"].strip()
                category_totals[category] = category_totals.get(category, 0) + amount

        report_filename = f"expense_report_{datetime.now().strftime('%Y-%m-%d')}.txt"

        with open(report_filename, "w", encoding="utf-8") as report_file:
            report_file.write("=====================================\n")
            report_file.write("        EXPENSE SUMMARY REPORT       \n")
            report_file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            report_file.write("=====================================\n\n")

            report_file.write(f"Total Amount Spent : ₹{total_spend}\n")
            report_file.write(f"Total Transactions : {transaction_count}\n")
            if transaction_count > 0:
                report_file.write(f"Average Per Expense: ₹{round(total_spend / transaction_count, 2)}\n\n")

            report_file.write("--- Breakdown By Category ---\n")
            for cat, total in category_totals.items():
                report_file.write(f"* {cat}: ₹{total}\n")

            report_file.write("\n=====================================\n")
            report_file.write("End of Report\n")

        print(f"Report successfully saved as '{report_filename}'!")

    except FileNotFoundError:
        print("No expenses.csv file found to generate a report from.")

def main_menu():
    while True:
        print("\n=============================")
        print("     EXPENSE TRACKER MENU    ")
        print("=============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter & Total Single Category")
        print("4. View Breakdown By Category")
        print("5. Show Total Spending")
        print("6. Export Report To File")
        print("7. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":
            cat = input("Category: ").strip()
            desc = input("Description: ").strip()
            try:
                amount = int(input("Amount: ").strip())
                add_expense(cat, desc, amount)
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category = input("Category: ").strip()
            show_total_for_category(category)
        elif choice == "4":
            column_name = input("Column Name: ").strip()
            filter_value = input("Filter Value: ").strip()
            print_filtered_expenses(column_name, filter_value)
        elif choice == "5":
            print(total_spending())
        elif choice == "6":
            export_report_to_txt()
        elif choice == "7":
            print("Goodbye! Thanks for using the Expense Tracker. 👋")
            break  # This breaks the while loop and closes the app
        else:
            print("❌ Invalid choice. Please type a number between 1 and 5.")

# This line triggers the menu when you run the file
if __name__ == "__main__":
    main_menu()