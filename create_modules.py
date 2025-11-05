# create_modules.py
#my_module.py
def greet(name):
    print(f"Hello, {name}!")

def calculate_sum(a, b):
    return a + b


# main.py
import my_module

my_module.greet("Juan")  # Prints "Hello, Juan!"
result = my_module.calculate_sum(5, 3)
print(result)  # Prints 8


# Code organization into modules
# operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# utilities.py
def print_message(message):
    print(message)

def get_user_name():
    return input("Enter your name: ")

# Import funtions in main.py
import operations
import utilities


result = operations.add(5, 3)
utilities.print_message(f"The result of the addition is: {result}")


name = utilities.get_user_name()
utilities.print_message(f"Hello, {name}!")