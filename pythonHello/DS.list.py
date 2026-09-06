#Creating a List
fruits=["apple","bannana"]
print(fruits)

print("====================================")

#Using list() Constructor: A list can also be created by passing an 
# iterable  (such as tuple, string or another list) 
# to the list() constructor

fruitts=list(("bannana","strwabery","mangao"))
print(fruitts)

a=list("aHAJKJAIUHSABJ")
print(a)
print("=======================================")

#Creating List with Repeated Elements: A list with repeated elements 
# can be created using the multiplication (*) operator.

a=[5]*4
print(a)
print("=======================================")

#Python list stores references to objects,
#  not the actual values directly.

#The list keeps memory addresses of objects 
# like integers, strings or booleans.
#Actual objects exist separately in memory.
#Modifying a mutable object inside a list changes the original object.
#Reassigning an immutable object creates a new 
# object instead of changing the old one.


p=[1,4,56,"python"]
print(p[3])
print(p)

#accesing elements:::
# index based p[0]-starts first element=+ve
#p[-1]-starts from last element -ve index

print(p[0])
print(p[-1])
print("====================================")
#Adding Elements:::::::::::::::::

#append(): Adds an element at the end of the list.

List=["hello","shivaji",34,"hi",87]
List.append(96)
print(List)

#insert(): Adds an element at a specific position.
b= [1, 3]
b.insert(0, 0.0)
b.insert(1, 2)

b.insert(2, 27)
print(b)

#extend(): Adds multiple elements to the end of the list.

a = [1, 2]
a.extend([3, 4,5,7])
print(a)

print("====================================")


#Updating Elements
#lists are mutable, elements can be updated by assigning 
# new values using their index.


n = [10, 20, 30, 40, 50]
n[1] = 25 
print(n)

print("====================================")

# remove(): Removes the first occurrence of an element.

a = [1, 2, 3,52,7,2,8]
a.remove(2)
print(a)

print("====================================")

#pop(): 
# Removes the element at a specific index or
#  the last element if no index is specified.


a = [1, 2, 3,9,6,4,3,5]
a.pop(3) #index specified 
print(a)
a.pop()
print(a) #--last element

print("====================================")
#del statement: Deletes an element at a specified index.

num= [1, 2, 3]
del num[1]
print(num)

print("====================================")

#clear(): removes all items.

a = [1, 2, 3]
a.clear()
print(a)

print("====================================")

#Iterating Over Lists
#Lists can be iterated using loop nd iterate each element

basket = ['apple', 'banana', 'cherry']
for item in basket:
    print(item)

print("====================================")

#ested Lists::

##A nested list is a list that contains another list as its element.
#used to represent matrices or tabular data.
#Nested elements can be accessed by chaining multiple indexes.


nested_list= [[1, 2], [3, 4],[56,"hii"]]
print(nested_list[0])
print(nested_list[2][1])
