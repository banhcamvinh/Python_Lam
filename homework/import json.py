import json
from pathlib import Path

current_dir = Path(__file__).parent
output_file = current_dir / "data.json"


def load_items():
    if output_file.exists():
        with open(output_file, "r") as f:
            return json.load(f)
    return []


def save_items(items):
    with open(output_file, "w") as f:
        json.dump(items, f)


def Main_menu():
    print("1. Add Item")
    print("2. Display Items")
    print("3. Delete Item")
    print("4. Exit")


def Add_Item():
    items = load_items()                          # Step 1: read what's already in the file
    new_item = input("Enter the name of the item to add: ")
    items.append(new_item)                        # Step 2: add the new item to the list
    save_items(items)                             # Step 3: save the updated list back to the file
    print(f'"{new_item}" added successfully.')


def Display_Items():
    items = load_items()
    if not items:
        print("No items found.")
    else:
        print("Items in your list:")
        for i, item in enumerate(items, 1):       # enumerate gives each item a number starting at 1
            print(f" - {i}. {item}")
            print()


def Delete_Items():
    items = load_items()                         
    if not items:
        print("Nothing to delete.")
    else:
        Display_Items()
        item_to_remove = input("Enter the name of the item to delete: ")
        if item_to_remove in items:
            items.remove(item_to_remove)         
            save_items(items)                     
            print(f'"{item_to_remove}" removed successfully.')
        else:
            print("Item not found.")


while True:
    Main_menu()
    selection = input("Select your option: ")

    if selection == "1":
        Add_Item()
    elif selection == "2":
        Display_Items()
    elif selection == "3":
        Delete_Items()
    elif selection == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
