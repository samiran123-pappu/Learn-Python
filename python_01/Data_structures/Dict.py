d = {"name": "Sam", "age": 21}
print(d)


d["age"] = 22
print(d)



print(d.keys())   # dict_keys(['name', 'age'])
print(d.values()) # dict_values(['Sam', 22])
print(d.items())  # dict_items([('name', 'Sam'), ('age', 22)]


d["city"] = "Kolkata"
print(d)



d.pop("age")
print(d)



d.popitem()
print(d)


print("name" in d)  # True
print("age" in d)   # False



print(d.get("age", "Not found"))  # Not found
print(d.get("name"))               # Sam


print(d)
d2 = {"age": 21, "country": "India"}
d.update(d2)
print(d)


d.clear()
print(d)



d = {"name": "Sam", "age": 21}
d_copy = d.copy()
print(d_copy)


for key, value in d.items():
    print(key, "->", value)
