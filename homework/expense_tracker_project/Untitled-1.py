import csv
def load_Expense():
    try:
        with open('data.csv', mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        print("No expense file found. Starting fresh.")
    return []

def Main_menu():
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. Display Expense")
    print("5. Display Summary")

def Add_Expense():
    expenses = load_Expense()
    add_expense = input("Enter the name of the expense to add: ")
    add_description = input("Enter the description of the expense added: ")
    add_amount = input("Enter the amount of the expense")
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
    Display_Expense()
    update_expense = input("Enter the update name of the expense to add: ")
    update_description = input("Enter the update description of the expense added: ")
    update_amount = input("Enter the update amount of the expense")
    if expense in expenses:
        expense_bar["Expense name"] = update_expense
        expense_bar["Expense description"] = update_description
        expense_bar["Expense amount"] = update_amount


def Display_Expense():
        print("Items in your list:")
        for i, expense_bar in enumerate(expense_bar, 1):
            print(f" {i}. {expense_bar["Expense name"]}")
            print(f"Description: {expense_bar["Expense description"]}")
            print(f"Status: {expense_bar["Expense amount"]}")
            print()
while True:
    Main_menu()
    selection = input("Select your option: ")

    if selection == "1":
        Add_Expense()
    elif selection == "2":
        Update_Expense()
    else:
        print("Invalid choice, please try again.")
