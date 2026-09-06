# Strings are commonly used for text handling and manipulation.
# create___String
# Strings can be created using either single ('...') or double ("...") quotes

a = 'i love biriyani'
b = "I love biriyani !!!"

print(a)
print(b)

print("=======================================")

# multilinee
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
biriyani lover'''
print(s)
print("=======================================")

# Acess strings from character
st = "Quackers"
print(st[7])
print(st[-4])

print("=======================================")


# string slicing::
# extract portion of string using start and end index (end index-excluded)


word = "Mynataa"
print(len(word))
print(word[1:4])
print(word[1:])
print(word[:6])
print(word[:7])
print(word[:-5])

print("=======================================")
# Looping Through Strings
# Strings are iterable,
# access each character one by one using a loop.


s = "Narayan"
for char in s:
    print(char)

print("=======================================")

# String immutability
p = "aBCDEF"
p = "A" + s[1:]
print(p)

print("=======================================")

# delete string
q = "biriyanii"
print(q)
del q

print("=======================================")

# update string
s = "ABCD EF"
s1 = "H" + s[1:]
s2 = s.replace("ABC", "abc")

print(s1)
print(s2)

print("=======================================")

# upper() lower()
s = "Hello World"
print(s.upper())
print(s.lower())

print("=======================================")

# strip() &replace()
s = "   ABC   "
print(s.strip())

s = "i love biriyani"
print(s.replace("biriyani", "mutton-biriyani"))

print("=======================================")

# concatention
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)

print("=======================================")


# Repetition:
# A string can be repeated multiple times using *.

s = "Hello "
print(s * 3)
print("=======================================")

# formatting string
name = "Naryan"
age = 22
print(f"Name: {name}, Age: {age}")

print("=======================================")

# using format():
text = "My name is {} and I am {} years old.".format("Narayan", 22)
print(text)

print("=========================================")


# string memebership testing: checking substring is present or not and return boolean value

food = "muttoncurry"
print("mutton" in food)
print("biriyani" in food)
