# LIST METHODS - Demonstrate various list methods in Python

fruits = ["apple", "banana", "orange"]

fruits.append("pear")
print(fruits)  # Prints ["apple", "banana", "orange", "pear"]

fruits.insert(1, "grape")
print(fruits)  # Prints ["apple", "grape", "banana", "orange", "pear"]

fruits.remove("banana")
print(fruits)  # Prints ["apple", "grape", "orange", "pear"]

removed_fruit = fruits.pop(2)
print(fruits)  # Prints ["apple", "grape", "pear"]
print(removed_fruit)  # Prints "orange"

fruits.sort()
print(fruits)  # Prints ["apple", "pear", "grape"]

fruits.reverse()
print(fruits)  # Prints ["grape", "pear", "apple"]