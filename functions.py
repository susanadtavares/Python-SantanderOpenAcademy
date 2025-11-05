# Definition and Funtion Call
def greeting():
    print("Hello, world!")

greeting()  # Prints "Hello, world!"


# Parameters and Arguments
def greeting(name):
    print(f"Hello, {name}!")

greeting("John")  # Prints "Hello, John!"
greeting("Mary")  # Prints "Hello, Mary!"


# Return Values
def sum(a, b):
    return a + b

result = sum(3, 4)
print(result)  # Prints 7

# Anonymous Functions (Lambda)
square = lambda x: x ** 2
print(square(5))  # Prints 25


# Variable Scope (local vs global)
def function():
    local_variable = 10
    print(local_variable)  # Accessible within the function

global_variable = 20

def function2():
    print(global_variable)  # Accessible from anywhere

function()  # Prints 10
function2()  # Prints 20
print(global_variable)  # Prints 20
# print(local_variable)  # Generates an error, the variable is not defined in this scope.


# User-defined Funtions
# Function Documentation (docstrings)

def rectangle_area(base, height):
    """
    Calculates the area of a rectangle.

    Args:
        base (float): The base of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return base * height

# Funtions with Variable Number of Arguments

def variable_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total


print(variable_sum(1, 2, 3))  # Prints 6
print(variable_sum(4, 5, 6, 7))  # Prints 22