file = open("encryptedFile.txt")
s = ""

while True:
    character = file.read(2) 
    
    if not character:
        break
    
    s += character[0]
    
file.close()

print(s)