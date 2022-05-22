sentence = input("Enter a sentence: ")
shift = (int)(input("How much should the shift be? "))
finalCharacter = ""

for char in sentence:
    if char == " ":
        finalCharacter += " "
    else: 
        s = (ord(char) - 97) + shift
        if (s >= 26):
            s -= 26
        s += 97
        finalCharacter += chr(s)
        
print(finalCharacter)