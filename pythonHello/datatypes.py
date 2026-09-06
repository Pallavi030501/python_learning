# Numeric datatype-store numeric value-->3 types-->
# --->>>>integer,float,complex --->immutable
x = 10  # int
y = 23.89  # float
z = 11+5j  # complex

# ordered /unordered
# mutable /immutable


# sequence datatype--order collection items,similar or different datatypes ,elements can be accessed by using indexing
# --->
# String---------------immutable,ordered
s = "Pallavi"
print(id(s))
s = "narayan"
print(id(s))

print(s[6])

# List-----------------different datatypes,acess through indexing
# -----------------ordered,mutable
list_type = ["tiger", "banana", 12, True, 5+9j, 56.8]
print(list_type, id(list_type))
list_type[2] = 35.78
print(list_type, id(list_type))

# tuple---->immutable,ordered,multiple items store in single variable,
# accessed through indexing but can not be modified

tuple = ("jina", 3, False, "apple")
print(tuple[2])
# tuple[1]=56 --->error (can not modified)

print("----------------------")

# set--->unordered

set_type = {"jina", "richa", 78+8j, 34, True, 34.9}

print(set_type)

for i in set_type:
    print(i)
set_type.add(90)
print(set_type)


# dictionary------->key:value pair

dict_type = {2: "two", 4: False, 5: "apple"}
print(dict_type)
print(dict_type[2])

dict_type[4] = "toy"
print(dict_type)

# none-->
x = None
print(x)
print(type(x))

dict = {"pallavi": "topper",
        "jina": "10 th topper",
        "Pallavi": "bayani",
        "both": "married",
        "jina": "handsome"}
print(dict)
print(len(dict))  # unique key and give updated value
