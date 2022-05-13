class ShoppingCart:
    def __init__(self):
        self.numberOfItems = 0 
        self.itemNames = []
        self.totalPrice = 0
        self.priceWithTax = self.totalPrice * 1.13 
        
    def AddItem(self, item):
        self.numberOfItems += 1
        self.itemNames.append(item.name)
        self.totalPrice += item.price
        self.priceWithTax = self.totalPrice * 1.13 
        
    def PrintCart(self):
        print(self.itemNames)
        print("Total Price:", self.totalPrice)
        print("Total Price with Tax:", self.priceWithTax)
        
        
class Grocery:
    def __init__(self, name, price, id):
        self.name = name
        self.price = price
        self.id = id
        
groceries = []
groceries.append(Grocery("Apples", 2, 1093))
groceries.append(Grocery("Bananas", 2, 1116))
groceries.append(Grocery("Mangos", 6, 1359))
groceries.append(Grocery("Bread", 4, 1570))

print("Welcome to our store! Listed below are all of our items for purchase.\nCart:")
for i in groceries:
    print(i.name)
    
print()

userCart = ShoppingCart()

while True: 
    menu = input("What would you like to do?\n   1. View items in your shopping\n   2. Add item to cart\n   3. Remove an item from your cart\n   4. Exit\n")
    
    if menu == "1":
        userCart.PrintCart()
    elif menu == "2":
        itemToAdd = input("What item would you like to add?")
        for i in groceries:
            if i.name == itemToAdd:
                userCart.AddItem(i);
    elif menu == "3": 
        print(userCart.itemNames)
        itemToRemove = input("What item would you like to remove? ")
        for i in userCart.itemNames:
            if (i == itemToRemove):
                for i in groceries:
                    if i.name == itemToRemove:
                        userCart.totalPrice -= i.price
                        userCart.itemNames.remove(i.name)
        userCart.priceWithTax = userCart.totalPrice * 1.13 
    elif menu == "4":
        break
    else: 
        print("Invalid Option")
            