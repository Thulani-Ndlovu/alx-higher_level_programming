#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number > 0:
    if ((lastDigit < 6) and not (lastDigit == 0)):
        print("Last digit of", number, "is", lastDigit, end=' ')
        print("and is less than 6 and not 0")
    elif (lastDigit == 0):
        print("Last digit of", number, "is", lastDigit, "and is 0")
    elif (lastDigit > 5):
        print("Last digit of", number, "is", end=' ')
        print(lastDigit, "and is greater than 5")
elif number < 0:
    if ((-1*lastDigit < 6) and not (-1*lastDigit == 0)):
        print("Last digit of", number, "is", -lastDigit, end=' ')
        print("and is less than 6 and not 0")
    elif (-1*lastDigit == 0):
        print("Last digit of", number, "is", lastDigit, "and is 0")
    elif (-1*lastDigit > 5):
        print("Last digit of", number, "is", -lastDigit, end=' ')
        print("and is greater than 5")
else:
    print("Last digit of 0 is 0 and is 0")
