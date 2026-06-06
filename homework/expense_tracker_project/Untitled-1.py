import csv 
import pandas as pd
from pathlib import Path
df = pd.read_csv('data.csv') 
current_dir = Path(__file__).parent
output_file = current_dir / "data.csv"

def load_expense():
    if output_file.exists():
        with open(output_file, "r") as f:
            return csv.load(f)
    return []

def save_expense(expenses):
    with open(output_file, "w") as f:
        csv.dump(expenses, f)

def Main_menu():
    print("1. Add Expense")
    print("2. Update Expense")
    print("3. Delete Expense")
    print("4. Display Expense")
    print("5. Display Summary")

def Add_Expense():
    # expenses = load_expense()
    # if not expenses:
    #     print("No expense to update.")
    #     return
    add_expense = input("Enter the name of the expense to add: ")
    add_description = input("Enter the description of the expense added: ")
    expense_bar = {}
    expense_bar["Add expense"] == add_expense
    expense_bar["Expense description"] == add_description
    save_expense(expenses)
def Update_Expense():
    choose_expense = input("Choose the expense you want to edit: ")
    
    
    
    
while True:
    Main_menu()
    selection = input("Select your option: ")

    if selection == "1":
        Add_Expense()
    # elif selection == "2":
        
    # elif selection == "3":
        
    # elif selection == "4":
        
    # elif selection == "5":
        
    else:
        print("Invalid choice, please try again.")
    






    

