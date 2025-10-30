# LIST COMPREHENSIONS - Create a list of squares of even numbers from 1 to 5
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers if x % 2 == 0]
print(squares)  # Prints [4, 16]