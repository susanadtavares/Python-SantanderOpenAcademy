# Importing the math module to use its functions
import math

result = math.sqrt(25)
print(result)  # Prints 5.0


# Alternatively, importing only the sqrt function from the math module
from math import sqrt

result = sqrt(25)
print(result)  # Prints 5.0


# Creating a custom module named my_module.py with a function
import random
import datetime

random_number = random.randint(1, 10)
print(random_number)  # Prints a random integer between 1 and 10

current_date = datetime.datetime.now()
print(current_date)  # Prints the current date and time