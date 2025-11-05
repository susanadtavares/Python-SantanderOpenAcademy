# TRY
try:
    # Code that may generate an exception
    result = 10 / 0  # Division by zero
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")


# EXCEPT
try:
    # Code that may generate an exception
    result = 10 / 0  # Division by zero
    print(result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid value")


# FINALLY
try:
    # Code that may generate an exception
    file = open("file.txt", "r")
    # Perform operations with the file
except FileNotFoundError:
    print("Error: File not found")
finally:
    file.close()  # Always close the file, even if an exception occurs