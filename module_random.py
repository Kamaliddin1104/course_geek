from random import *

numbers = [1, 2, 3, 4, 5]
shuffle(numbers)
print(numbers)

number = randint(1, 100)
print(number)

float_num = uniform(0, 1)
print(float_num)

num = choice(numbers)
print(num)

START = 1
END = 99
STEP = 2
x = randrange(START, END, STEP)
print(x)

print(sample(numbers, 2))

