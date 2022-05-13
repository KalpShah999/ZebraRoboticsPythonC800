file = open("encryptedFile.txt")
s = ""

while True:
    character = file.read(1) 
    if not character:
        break
    s += character
    character = file.read(1)
    
file.close()

print(s)