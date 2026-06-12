import csv
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
    expense_bar = {}
    expense_bar["Expense name"] = add_expense
    expense_bar["Expense description"] = add_description
    expense_bar["Expense amount"] = add_amount
    with open('data.csv', mode='a', newline='') as csv_file:
        fieldnames = ['expense', 'description', 'amount']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({
            'expense': expense_bar["Expense name"],
            'description': expense_bar["Expense description"],
            'amount': expense_bar["Expense amount"]
        })
def Update_Expense():
    expenses = load_Expense()
    Display_Expense(expenses)
    index = int(input("Enter the number of the expense to update: ")) - 1
    if 0 <= index < len(expenses):
        expenses[index]['expense'] = input("Enter the new expense name: ")
        expenses[index]['description'] = input("Enter the new description: ")
        expenses[index]['amount'] = input("Enter the new amount: ")
        with open('data.csv', mode='w', newline='') as csv_file:
            fieldnames = ['expense', 'description', 'amount']
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
            fieldnames = ['expense', 'description', 'amount']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
        print(f"Expense '{removed['expense']}' deleted successfully.")
    else:
        print("Invalid expense number.")


def Display_Expense(expenses):
    print("Items in your list:")
    for i, expense in enumerate(expenses, 1):
        print(f" {i}. {expense['expense']}")
        print(f"Description: {expense['description']}")
        print(f"Amount: {expense['amount']}")
        print()
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
    else:
        print("Invalid choice, please try again.")
