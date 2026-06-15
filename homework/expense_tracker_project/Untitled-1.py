import csv
import os
import datetime
def load_Expense():
    expenses = []
    with open('data.csv', mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            expenses.append(row)
    return expenses

def Main_menu():
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. Display Expense")
    print("5. Display Summary")

def Add_Expense():
    add_expense = input("Enter the name of the expense to add: ")
    add_description = input("Enter the description of the expense added: ")
    add_amount = input("Enter the amount of the expense: ")
    add_month = datetime.datetime.now().month
    expense_bar = {}
    expense_bar["Expense name"] = add_expense
    expense_bar["Expense description"] = add_description
    expense_bar["Expense amount"] = add_amount
    expense_bar["Month"] = add_month
    file_is_empty = not os.path.exists("data.csv") or os.stat("data.csv").st_size == 0
    with open('data.csv', mode='a', newline='') as csv_file:
        fieldnames = ['Expense name', 'Expense description', 'Expense amount', 'Month']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        headerwriter = csv.writer(csv_file)
        if file_is_empty:
            headerwriter.writerow(fieldnames)
        writer.writerow(expense_bar)

def Update_Expense():
    expenses = load_Expense()
    Display_Expense(expenses)
    index = int(input("Enter the number of the expense to update: ")) - 1
    if 0 <= index < len(expenses):
        expenses[index]['Expense name'] = input("Enter the new expense name: ")
        expenses[index]['Expense description'] = input("Enter the new description: ")
        expenses[index]['Expense amount'] = input("Enter the new amount: ")
        with open('data.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Expense name', 'Expense description', 'Expense amount', 'Month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
        print("Expense updated successfully.")
    else:
        print("Invalid expense number.")


def Delete_Expense():
    expenses = load_Expense()
    Display_Expense(expenses)
    index = int(input("Enter the number of the expense to delete: ")) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        with open('data.csv', mode='w', newline='') as csv_file:
            fieldnames = ['Expense name', 'Expense description', 'Expense amount', 'Month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expense '{removed['Expense name']}' deleted successfully.")
    else:
        print("Invalid expense number.")


def Display_Expense(expenses):
    print("Items in your list:")
    for i, expense in enumerate(expenses, 1):
        print(f" {i}. {expense['Expense name']}")
        print(f"Description: {expense['Expense description']}")
        print(f"Amount: {expense['Expense amount']}")
        print()
def Display_Summary():
    expenses = load_Expense()
    month = input("Enter the month to view summary: ")
    total = 0
    for expense in expenses:
        if expense['Month'] == month:
            total = total + float(expense['Expense amount'])
    print("Total expenses for month " + month + ": " + str(total))


while True:
    Main_menu()
    selection = input("Select your option: ")

    if selection == "1":
        Add_Expense()
    elif selection == "2":
        Update_Expense()
    elif selection == "3":
        Delete_Expense()
    elif selection == "4":
        Display_Expense(load_Expense())
    elif selection == "5":
        Display_Summary()

    else:
        print("Invalid choice, please try again.")
