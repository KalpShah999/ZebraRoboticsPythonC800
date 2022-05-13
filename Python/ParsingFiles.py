file = open("parsingFiles.txt")

text = file.read()

words = text.split()

file.close()

wordsToLookFor = [["password", 0], ["security", 0], ["e-transfer", 0], ["accounts", 0], ["cards", 0], ["deposit", 0], ["branch", 0]]

for word in words:
    for i in range(len(wordsToLookFor)):
        if word.lower().strip(',') == wordsToLookFor[i][0]:
            wordsToLookFor[i][1] += 1
            
print(wordsToLookFor)