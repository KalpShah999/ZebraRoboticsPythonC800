file = open("animalDictionary.txt")

animalBabies = {}

while True: 
    line = file.readline()
    
    if not line:
        break
    
    lineSplit = line.split(",")
    
    animalBabies[lineSplit[0]] = lineSplit[1]

file.close()

while True:
    menu = input("Select one of the options:\n1. Lookup animal babies\n2. Add animal and baby\n3. Delete animal and baby\n4. Exit\n")
    
    if menu == "1":
        animal = input("Which animal would you like to see? ").lower()

        if (not animalBabies.get(animal)):
            answer = input("There is no such animal, would you like to add it (yes/no)? ")
            if answer.lower() == 'yes':
                value = input("What is the animal baby name? ")
                animalBabies[animal] = value
            else:
                print("Alright then.")
        else:
            print(animalBabies.get(animal))
    elif menu == "2":
        animalToAdd = input("What is the name of the animal? ")
        if not animalBabies.get(animalToAdd):
            value = input("What is the animal baby name? ")
            animalBabies[animalToAdd.lower()] = value.lower()
            file2 = open("animalDictionary.txt", "a")
            file2.write("\n" + animalToAdd.lower() + "," + value.lower())
            file2.close()
        else: 
            print("This animal already exists")
    elif menu == "3":
        animalToRemove = input("Which animal would you like to remove? ")
        del(animalBabies[animalToRemove])
    elif menu == "4":
        break
    else: 
        print("Invalid option.")