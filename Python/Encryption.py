sentence = input("Enter a sentence: ")
shift = (int)(input("How much should the shift be? "))
s = ""

for char in sentence:
    if char == " ":
        s += " "
    else: 
        s += chr(((ord(char) - 97) + shift) % 26 + 97)
        
print(s)