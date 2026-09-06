

# no built-in fuc array like other language
# Can store mixed data types in one list
# Elements can be added or removed easily
# Provide functions like append(), remove(), sort()


List = a = [1, "Hello", [3.14, "world"]]
List.append(2)  # Add an integer to the end
print(List)

#import numpy as np-- before install numpy

import numpy as np
a = np.array([1, 2, 3, 4])

# Element-wise operations
print(a * 2)  

# Multi-dimensional array
res = np.array([[1, 2], [3, 4]])
print(res * 2)

import array as arr
number = arr.array('i', [1, 2, 3]) 
#i- typecode-it tells python to treat as integer


# accessing first array
print(number[0])

# adding element to array
number.append(5)
print(number)

print("================")
#creat an array :::::::::::::
a = arr.array('i', [1, 2, 3])

for i in range(0, 3):
    print(a[i], end=" ")

#adding element :insert() -add in specfic index
a.insert(1, 4)  # Insert 4 at index 1
print(*a)   #* used to unpack the array elements

a.append(78) #add at last
print(*a)

#accessing elemenets
n = arr.array('i', [1, 2, 3, 4, 5,1,3,10, 6])

print(n[0])
print(n[3])

# remove first occurence of 1
n.remove(1)
print(*n)

# remove item at index 2
n.pop(2)
print(*n)

#slicing
a=[1,78,34,1,34,67,2,3,5,6]
b=arr.array('i',a)
res = b[3:8]
print(res)

res=b[:10]
print(res)

res=b[::-1]
print(res)

#Searching Element
# use index()  returns the index of the first occurrence of value mention in arguments.

element= arr.array('i', [1, 2, 3, 1, 2, 5])
# index of 1st occurrence of 2
print(element.index(2))
# index of 1st occurrence of 1
print(element.index(1))

#update element
# update item at index 2 &5
element[2] = 6
element[5] = 8
print(element)


#methods of array

# Counting Elements: 
# count() method to count given item in array.

import array
a = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = a.count(2)
print(count)


#Reversing Elements: reverse elements of an array use reverse method.
import array as ele
elements= ele.array('i', [1, 2, 3, 4, 5])
elements.reverse()
print(*elements)

# Extend Element: 
# extend()is used to attach an item from iterable to the end of the array.

extened_element = array.array('i', [1, 2, 3,4,5])
extened_element.extend([6,7,8,9,10])
print(*extened_element)