class Car:
    def __init__(self, make, model, year, price, used, mileage, doors, available): 
        self.make = make
        self.model = model
        self.year = year
        self.price = price;
        self.used = used
        self.mileage = mileage
        self.doors = doors
        self.available = available
    
    def GetPrice(self):
        return self.price
    
    def GetAvailability(self):
        return self.available
    
    def SetPrice(self, price):
        self.price = price
    
    def SetAvailability(self, available):
        self.available = available
        
    def PrintCarInformation(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Price:", self.GetPrice())
        print("Used:", self.used)
        print("Mileage:", self.mileage)
        print("Doors:", self.doors)
        print("Available:", self.available)