# Import built-in libraries

import csv
from datetime import datetime

# Import file name from utils.py
from .utils import FILE_NAME


# Function to add expense
def add_expense(category, amount, description):

    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Open CSV file in append mode
    with open(FILE_NAME, mode="a", newline="") as file:

        # Create CSV writer object
        writer = csv.writer(file)

        # Write expense data
        writer.writerow(
            [date, category, amount, description]
        )

    print("Expense added successfully!")


# Function to display all expenses
def view_expenses():

    # Open CSV file in read mode
    with open(FILE_NAME, mode="r") as file:

        # Create CSV reader object
        reader = csv.reader(file)

        print("\n--- All Expenses ---")

        # Loop through rows
        for row in reader:
            print(row)


# Function to calculate total expense
def total_expense():

    total = 0

    # Open CSV file
    with open(FILE_NAME, mode="r") as file:

        # Read CSV data
        reader = csv.reader(file)

        # Loop through rows
        for row in reader:

            try:
                # Add amount column
                total += float(row[2])

            except:
                # Ignore invalid rows
                pass

    return total