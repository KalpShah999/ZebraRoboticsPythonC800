from CarClass import Car

cars = []
cars.append(Car("Toyota", "Corolla", "2010", "15000", "TRUE", "4500", "4", "TRUE"))

while True: 
    menu = input("What would you like to do?\n   1. Find a car (using the model)\n   2. Add a car\n   3. Mark a car as sold (Make it unavailble)\n   4. Exit\n")
    
    if menu == "2":
        firstName = input("What is the car make? ")
        lastName = input("What is the car model? ")
        studentNumber = input("What is the car year? ")
        birthday = input("What is the car price? ")
        mark = input("Is the car used or new? ")
        grade = input("What is the cars mileage? ")
        classNumber = input("How many doors does the car have? ")
        classesAttended = input("Is the car Available or Unavailable? ")
        cars.append(Car(firstName, lastName, mark, birthday, studentNumber, grade, classNumber, classesAttended))
    elif menu == "3":
        carMake = input("What is the car's make? ")
        for i in cars:
            if (i.make == carMake):
                menuOption = input("What would you like to change?\n   1. Mileage\n   2. Availability")
                if menuOption == "1":
                    newMileage = input("What is the new mileage? ")
                    i.mileage = newMileage
                elif menuOption == "2":
                    i.SetAvailability("Unavailable")
    elif menu == "1":
        carMakeToFind = input("What is the cars make? ")
        for i in cars:
            if (i.make == carMakeToFind):
                i.PrintCarInformation()
    elif menu == "4":
        break;
    else: 
        print("Invalid Menu Option")
    