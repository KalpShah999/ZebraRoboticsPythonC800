def TipCalculator(cost, tipAmount = 15):
    return cost * tipAmount / 100

tipVal = TipCalculator(30)
print(tipVal)
tipVal = TipCalculator(30, 20)
print(tipVal)