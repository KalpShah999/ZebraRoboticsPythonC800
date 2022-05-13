animalBabies = {'hippo' : 'calf', 
                 'horse' : 'foal',
                 'dog' : 'pup',
                 'kangaroo' : 'joey',
                 'monkey' : 'infant',
                 'owl' : 'owlet',
                 'parrot' : 'chick',
                 'rabbit' : 'bunny',
                 'rat' : 'pup',
                 'cow' : 'calf',
                 'shunk' : 'kit',
                 'sheep' : 'lamb'}

while True:
    menu = input("Select one of the options:\n1. Lookup animal babies\n2. Add animal and baby\n3. Delete animal and baby\n")
    
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
            animalBabies[animalToAdd] = value
        else: 
            print("This animal already exists")
    elif menu == "3":
        animalToRemove = input("Which animal would you like to remove? ")
        del(animalBabies[animalToRemove])
    else: 
        print("Invalid option.")