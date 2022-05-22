groceryList = ["Apples", "Bananas", "Mangos", "Strawberries", "Pineapples"]

while True: 
    menu = input("\nWhat would you like to do?\n   1. Add an item\n   2. Sort the grocery list\n   3. Remove an item\n   4. Replace an item\n   5. Print the list length\n   6. Print the list\n   7. Exit")
    
    if (menu == "1"):
        itemToAdd = input("What item would you like to add to the grocery list? ")
        groceryList.append(itemToAdd)
        print(groceryList)
    elif (menu == "2"):
        groceryList.sort()
        print(groceryList)
    elif (menu == "3"):
        itemToRemove = input("Which item would you like to remove from the grocery list? ")
        groceryList.remove(itemToRemove)
        print(groceryList)
    elif (menu == "4"):
        itemToReplace = input("Which item would you like to replace in the grovery list? ")
        itemToReplaceWith = input("Which item would you like to replace it with? ")
        groceryList.insert(groceryList.index(itemToReplace), itemToReplaceWith)
        groceryList.remove(itemToReplace)
    elif (menu == "5"):
        print("Length: " + (str)(len(groceryList)))
    elif (menu == "6"):
        print(groceryList)
    elif (menu == "7"):
        break;
    else:
        print("Invalid option, choose again.")