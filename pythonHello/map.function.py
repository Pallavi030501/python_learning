#map::::::::::::::
## syntax:---- map(function,iterable..) --iterable ---list,tuple,set

list_type=["1","3","7","8","10"]
result=map(int,list_type)
"""
print(list(result))
print(type(list(result)))
"""
print(type(list(result)[0])) #int type


list_char=["a","b","c","d"]
def UpperCase(char):
    return char.upper()

resultofupper=map(UpperCase,list_char)
print(list(resultofupper))

#convert map() with lambda

uppercase=map(lambda char:char.upper(),list_char)
print(list(uppercase))

print("=====================================")
#example::::;  map () with multiple iterables
list1=[23,78,4,6,23]
list2=[1,2,3,8,9]

def add(x,y):
    return x+y

resultOf=list(map(add,list1,list2))
print(resultOf)


#extracting first character from string

fruits=["apple","banana","sugarcane","berryblues","strawbery"]
firstCharOfString= map(lambda firstchar:firstchar[0],fruits)
print(list(firstCharOfString))

#remove whiteshapes using map
words=[" hello ","  bye","hi   ","  namaste  "]
resulttt=map(str.strip,words)
 #---str.strip()--used to trim the whitespace from each element

print(list(resulttt))


#ques
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))