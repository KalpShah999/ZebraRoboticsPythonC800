sentence = input("Enter a sentence: ")
s = ""
vowels = "aeiou"

for char in sentence:
    if char not in vowels:
        s += char
        
print(s)