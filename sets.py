# SET - Creation
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 4, 5])

# SET - Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2
print(union)  # Prints {1, 2, 3, 4, 5}

intersection = set1 & set2
print(intersection)  # Prints {3}

difference = set1 - set2
print(difference)  # Prints {1, 2}

symmetric_difference = set1 ^ set2
print(symmetric_difference)  # Prints {1, 2, 4, 5}


# SET - Methods
fruits = {"apple", "banana", "orange"}

fruits.add("pear")
print(fruits)  # Prints {"apple", "banana", "orange", "pear"}

fruits.remove("banana")
print(fruits)  # Prints {"apple", "orange", "pear"}

fruits.discard("grape")
print(fruits)  # Prints {"apple", "orange", "pear"}

fruits.clear()
print(fruits)  # Prints set()