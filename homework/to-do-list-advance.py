import json
from pathlib import Path
import uuid
from datetime import datetime
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
    print("3. Delete Items")
    print("4. Update Items")
    print("5. Update Status")
    print("6. Exit")

def Update_status():
    items = load_items()
    if not items:
        print("No items to update.")
        return
    Display_Items()
    name_status = input("Enter the name status to update: ")
    for item in items:
        if item["task name"] == name_status:
            item["status"] = input("New status: ")
            item["updatedAt"] = str(datetime.now())
            save_items(items)
            print("Item updated successfully.")
            return
    print("Item not found.")

def Update_Item():
    items = load_items()
    if not items:
        print("No items to update.")
        return
    Display_Items()
    name = input("Enter the task name to update: ")
    for item in items:
        if item["task name"] == name:
            item["task name"] = input("New name: ")
            item["description"] = input("New description: ")
            item["updatedAt"] = str(datetime.now())
            save_items(items)
            print("Item updated successfully.")
            return
    print("Item not found.")




def Add_Item():
    items = load_items()                        
    new_item = input("Enter the name of the item to add: ")
    new_description = input("Enter the description of the item added: ")
    status = input("Enter the status of task (todo, in-progress, done): ")
    items_visual = {}
    items_visual["uuid"]= str(uuid.uuid1())
    items_visual["task name"] = new_item
    items_visual["description"] = new_description
    items_visual["status"] = status
    items_visual["updatedAt"] = str(datetime.now())

    items.append(items_visual)                  # Step 2: add the new item to the list
    save_items(items)                             # Step 3: save the updated list back to the file
    print(f'"{new_item}: {new_description}" added successfully.')


def Display_Items():
    items = load_items()
    if not items:
        print("No items found.")
    else:
        print("Items in your list:")
        for i, item in enumerate(items, 1):
            print(f" {i}. {item['task name']}")
            print(f"    Description : {item['description']}")
            print(f"    Status      : {item['status']}")
            print(f"    Updated at  : {item['updatedAt']}")
            print()


def Delete_Items():
    items = load_items()                         
    if not items:
        print("Nothing to delete.")
    else:
        Display_Items()
        item_to_remove = input("Enter the name of the item to delete: ")
        for item in items:
            if item["task name"] == item_to_remove:
                items.remove(item)
                save_items(items)
                print(f'"{item_to_remove}" removed successfully.')
                return
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
        Update_Item()
    elif selection == "5":
        Update_status()
    elif selection == "6":
        print("Goodbye")
        break
    else:
        print("Invalid choice, please try again.")
