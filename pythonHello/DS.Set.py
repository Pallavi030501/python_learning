s = {10, 50, 20}
print(s)
print(type(s))

print("======================")
#Type Casting
#set() method is used to convert other data types, such as lists or tuples into sets.
s1 = set(["a", "b", "c"])
print(s1)

print("======================")

#unique
# a set cannot have duplicate values
food = {"mutton","biriyani", "food", "biriyani"}
print(food)

print("======================")

#mutable
# values of a set cannot be changed
#food[1] = "Hello"
#print(food) ----------Error

#set can store a mixture of string, integer, boolean, etc datatypes.

mix={"hello",True,False,78,90.6}
print(mix)

print("========================")
#Methods for Sets
#Adding elements: add() function is used to insert new elements into a set. It automatically ignores duplicates.
alpha = {"a", "b", "c"}
alpha.add("d")
print(alpha)

# Union: union() function combines two sets and 
# returns a new set with all unique elements.
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# Intersection: intersection() function returns a new set containing 
# elements that are common to both sets.

a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

#Difference: 
# difference() function returns a set containing elements 
# that are in the first set but not in the second.


a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

#Clear: clear() function removes all elements from a set, 
# leaving it empty.

s = {1, 2, 3}
s.clear()
print(s)


