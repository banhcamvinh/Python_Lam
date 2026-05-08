def Main_menu():
    print("1. Add Item")
    print("2. Display Item")
    print("3. Delete Item")
def Add_Item():
    new_item = input("Enter the name of the item to add: ")
    items.append(new_item)
def Display_Items():
    print(items)
    if not items:
        print("The list is currently empty.")
def Delete_Items():
    if not items:
            print("Nothing to delete.")
    else:
        item_to_remove = input("Enter the name of the item to delete: ")
        if item_to_remove in items:
            items.remove(item_to_remove)

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
        
    else:
        print("Invalid choice, please try again.")




