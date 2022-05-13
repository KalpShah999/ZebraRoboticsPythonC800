def ReverseString(text, isReverse = False):
    l = []
    for i in text:
        l.append(i);
    if (isReverse):  
        l.reverse()
    return l

print(ReverseString("blue"))
print(ReverseString("blue", True))