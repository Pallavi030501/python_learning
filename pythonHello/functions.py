# function in python---->
# readability,
# maintainablity,
# reusabaility,
# modularaity

def printMyname(name):

    print("i lobe my pagala swamiiiiiiiii", name)


printMyname("jina")


def add(x=1, y=3):
    return x+y


print(add(4, 8))
print(add(y=9, x=8))  # variable suffle possible if mentioningbthe var name

# if not passing any value it will take default argument and perform the func
print(add())


def printSahufamilyNames(names, title="Sahu"):
    print("Family member : ", names, title)


printSahufamilyNames("Pramod Kumar")
printSahufamilyNames("Bijyalaxmi", "Mahapatra")
printSahufamilyNames("Sanket")
printSahufamilyNames("Narayan")
printSahufamilyNames("Pallavi")


tuple = (12, 34, 78)
dict = {"name": "jina", "age": 28, "marital status": "married"}

"""
* ---> used for passing tuple as a parameter
** --->used for passing dictioary as a parameter

"""


def printTupleorDictionary(*t, **d):
    for x in t:
        print("printing tuple:", x)
    print("------------------------------------------")
    for x in d:
        print("printing dictionary :", d[x])


printTupleorDictionary("56", "thirtyfour", "78",
                       one="hello", two="bye", third="get lost")

# func wiithin fun

print("-----fun within fun----------")


def fun1():
    print("inside function one")

    def fun2():
        print("inside function two")
    fun2()


fun1()




#pass by reference and value
print("----------------------------------")
#immutable
def funone(x):
    x=10

y=30
funone(y)
print(y)


###listtt--->mutable
def funList(l):
    l[0]=43

list_type=[12,56,89,45,90]
print(list_type)
funList(list_type)
print(list_type)


print("------------------------")
def sq_value(num):
    return num**2

print(sq_value(-4))