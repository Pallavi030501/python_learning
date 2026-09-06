#create a tuple:::
tup = ()
print(tup)

# Using String
python = ('Geeks', 'For')
print(python)

# Using List
num = [1, 2, 4, 5, 6]
print(tuple(num))

# Using Built-in Function
word= tuple("apple")
print(word)

#Creating a Tuple with Mixed Datatypes
##Tuples can store elements of different data types
#integers, strings, lists and dictionaries,
#within a single structure.

tuplee = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tuplee)

print("=============================")
#Accessing of Tuples:::::::::::
#indexing or slicing
word = tuple("Geeks")
print(word[0])
print(word[1:4])  
print(word[:3])

# Tuple unpacking
tup = ("mutton", "biriyani", "raita")

a, b, c = tup
print(a)
print(b)
print(c)


#concatenation tuple:::::::::::

t1=("hii","meena","world")
t2=(1,45,89,5.7,True)

concat=t1+t2
print(concat)

print("=======================")

#slicing:::::::::

dish=tuple("MuttonBiriyani")
print(dish[0:])
print(dish[1:4])
print(dish[:13])
print(dish[5:10])
print(dish[::-1])


#deleting tuple::::::::

tuples=(1,7,8,9)
del tuples
##print(tuples)
    #print(tuples)
#NameError: name 'tuples' is not defined. Did you mean: 'tuplee'?
print("===============================")
#Tuple Unpacking with Asterisk (*)
# *operator is used in tuple unpacking 
# to grab multiple items into a list. 

fruits=("apple","grapes","strawbery","gauva","orange")
a,*b,c=fruits
print(a)
print(b)
print(c)