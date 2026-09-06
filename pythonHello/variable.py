x = 7  # x is variable 5-->literal value
name = "jina"
print(type(name))

my_name = "Alok"
my_name1 = "jina"
MY_name = "Alok"
_color = "blue"
print(_color)

"""
Names can contain letters, digits and underscores (_).
The first character cannot be a digit.
Names are case-sensitive, so myVar and myvar are treated differently.
Keywords such as if, else and for cannot be used as variable names.
"""
# dynamic var
name = "RIChaa"
name = 10
print(name, type(name))

# multiple var
a = b = c = 10
print(a, b, c)
laptop, price, colour = "Dell", 29000, "Grey"
print("laptop details : ", laptop, price, colour)


x = 8
y = x  # x adress assign to y address
print(id(x), id(y))  # adress of x,y
print(x)
print(y)

"""

x = 10
print(id(x))
"""

y = 45
print(id(y), id(x))
print(y)

cat_name = "kitty"
del cat_name
#print(cat_name)

cat_name = "tony"
print(cat_name)

##length
name="Narayan Sahu"
print("length of the name :",len(name))