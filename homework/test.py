def Main_menu():
    print("1. Add Item")
    print("2. Display Item")
    print("3. Delete Item")
    print("4. Exit")


def Add_Item():
    new_item = input("Enter the name of the item to add: ")
    items.append(new_item)
    print(f"{new_item} added successfully.")


def Display_Items():
    if not items:
        print("The list is currently empty.")
    else:
        print("Items in list:")
        
        for item in items:
            print("- " + item)
    input("Press to continue: ")


def Delete_Items():
    if not items:
        print("Nothing to delete.")
    else:
        item_to_remove = input("Enter the name of the item to delete: ")

        if item_to_remove in items:
            items.remove(item_to_remove)
            print(f"{item_to_remove} removed successfully.")
        else:
            print("Item not found.")


items = []

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




