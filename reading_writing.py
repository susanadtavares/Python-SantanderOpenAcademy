# Reading files
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Writing files
file = open("data.txt", "w")
file.write("Hello, world!")
file.close()

# Using 'with' statement - automatic file closing
with open("data.txt", "r") as file:
    content = file.read()
    print(content)