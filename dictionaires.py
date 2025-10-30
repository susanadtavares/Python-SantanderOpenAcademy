# DICTIONARIES - CREATION AND ACCESS
person = {"name": "Juan", "age": 25, "city": "Madrid"}

print(person["name"])  # Prints "Juan"
print(person["age"])    # Prints 25
print(person["city"])  # Prints "Madrid"

person = {"name": "Juan", "age": 25, "city": "Madrid"}


# DICTIONARY METHODS - KEYS, VALUES, ITEMS, UPDATE
print(person.keys())    # Prints dict_keys(["name", "age", "city"])
print(person.values())  # Prints dict_values(["Juan", 25, "Madrid"])
print(person.items())   # Prints dict_items([("name", "Juan"), ("age", 25), ("city", "Madrid")])


person.update({"profession": "Engineer"})
print(person)  # Prints {"name": "Juan", "age": 25, "city": "Madrid", "profession": "Engineer"}