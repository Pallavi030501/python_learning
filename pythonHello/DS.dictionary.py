data = {"name": "pallavi", "age": 25}
print(data)

details = dict(name="Jina", gender="Male", age=28)
print(details)

# accesing dictionary keys:::::::::
data = {"name": "pallavi", "age": 25}

print(data["name"])     # Access using key
print(data.get("age"))  # Access using get()

# adding and updating::::::::::
person = {"name": "Sam"}

person["age"] = 21        # Adding a new key-value pair
person["name"] = "shann"   # Updating an existing value
print(person)

print("===============================")
# del: removes an item using its key


dict_1 = {"a": 1, "b": 2, "c": 3}
del dict_1["a"]
print(dict_1)

print("===============================")
# pop(): removes the item with the given key and returns its value

dictt = {"a": 1, "b": 2, "c": "apple", "d": 45}
val = dictt.pop("c")
print(val)
print(dictt)

print("===============================")

# popitem(): removes and returns last inserted key-value pair

d = {"a": 1, "b": 2}
print(d.popitem())
print("===============================")

# clear(): removes all items from the dictionary


d = {"a": 1, "b": 2}
d.clear()
print(d)


# iterating

d1 = {"a": 1, "b": 2, "c": "apple"}
for key in d1:
    print(key)
print("========================")

# iterate values:return all the values
d1 = {"a": 1, "b": 2, "c": "apple"}

for value in d1.values():
    print(value)

print("========================")


# iterate key vale pairs
d = {"a": 1, "b": 2, "c": 3}
for key, value in d.items():
    print(key, value)

print("========================")

# nesed dict ::::::::
dict_nest = {"student": {"name": "Sam", "age": 20, "class": 8}}

print(dict_nest["student"]["name"])
print(dict_nest["student"])
