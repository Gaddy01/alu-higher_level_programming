#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

if (number < 0):
    last_digit = "-"+str(number)[-1]
else:
    last_digit = str(number)[-1]

print("Last digit of", number, "is", last_digit, end=" ")

if int(last_digit) > 5:
    print("and is greater than 5")
elif int(last_digit) == 0:
    print("and is 0")
elif 6 > int(last_digit) and int(last_digit) != 0:
    print("and is less than 6 and not 0")
else:
    print("TypeError")
