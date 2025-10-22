# Tuple data type
'''y = (2, "yam", 4.5, True)
print(y)
print(y[1])
print(y[0:3])
print(len(y))
print(type(y))'''

# List data type
x = [3, "apple", 9.8, 56, "vanished", False]
print(x)
print("This data is of type", type(x))
print()
print(x[2])
print(x[3:4])
print()
print(len(x))
x[1] = "orange"
print(x)
print()
x.append("Bola is a Shark")
print(x)
x.remove(9.8)
print()
print(x)
'''x.sort()  # This will raise an error because the list contains mixed data types'''
print()
print()

# Dictionary data type
'''d = {"name": "Alice", "age": 30, "city": "New York"}
print(d)
print(d["name"])
print(d.get("age"))
d["age"] = 31'''