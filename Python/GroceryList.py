groceryList = ["Apples", "Bananas", "Mangos", "Strawberries", "Pineapples"]

itemToAdd = input("What item would you like to add to the grocery list? ")
groceryList.append(itemToAdd)

print(groceryList)

groceryList.sort()

print(groceryList)

itemToRemove = input("Which item would you like to remove from the grocery list? ")
groceryList.remove(itemToRemove)

print(groceryList)

print("Length: " + (str)(len(groceryList)))

itemToReplace = input("Which item would you like to replace in the grovery list? ")
itemToReplaceWith = input("Which item would you like to replace it with? ")
groceryList.insert(groceryList.index(itemToReplace), itemToReplaceWith)
groceryList.remove(itemToReplace)

print(groceryList)