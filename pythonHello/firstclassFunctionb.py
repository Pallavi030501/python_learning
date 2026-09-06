def add(x,y): ###add-object
    print("addition :",x+y)
fun=add

fun(5,7)
print(type(fun))

#function are treated   as first class objects
"""
def mix(function1):
    #function1=add
    function1(23,45)

mix(add) #---> used as parameter

"""
"""
def mix(a,b,function2):
    #function1=add
    #function1(23,45)
    return function2(a,b)


mix(7,8,add) #---> used as return value
"""

#create a dictionary of math function

def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multi(x,y):
    return x*y

def div(x,y):
    return x/y


dict_math={
     "add":add,
     "sub":substract,
     "product":multi,
     "divison":div

}

print(dict_math["add"](4,5))
print(dict_math["sub"](10,8))
print(dict_math["product"](4,5))
print(dict_math["divison"](20,10))