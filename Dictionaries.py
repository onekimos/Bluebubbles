# A simple dictionary
person = {"age":"21","gender":"female"}
# Accessing value
print("The person's age is " + person["age"])
# Adding a new key-value pair
person["height"] = 180
# Looping through all key-value pairs
ages = {"Jean":20, "Adjoa":21}
for name, age in ages.items():
    print(name + " is " + str(age) + " years old")
# Looping through all keys
ages = {"Jean":20, "Adjoa":21}
for name in ages.keys():
    print(name + " is a name")
# Looping through all the values
ages = {"Jean":20, "Adjoa":21}
for ages in ages.values():
    print(str(age) + " is my age")