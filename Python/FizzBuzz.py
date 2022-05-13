def FizzBuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        return 'FizzBuzz'
    elif (number % 3 == 0):
        return 'Fizz'
    elif (number % 5 == 0):
        return 'Buzz'
    else: 
        return number 

print(FizzBuzz(10))
print(FizzBuzz(9))
print(FizzBuzz(15))
print(FizzBuzz(4))