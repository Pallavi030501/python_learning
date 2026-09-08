"""
def world(Str):
    print("Hello world")
    return str
world("abc")

def add(a,b):
    return a+b


print(add(3,4))

def name(name):
    print("your name : ",name)
    age=24
    return age

age=name("Pallavi")  
print(age)


#function:::::::::
def function(args):
    #body
    print(args)
    return args
function("hello world")    
"""

"""

def ask(message):
    #if message is not a string throw error message
    if type(message) !=str:
        print("Error message : Please enter a valid string")
        return #none
    return message+"?"
message="Python is good"
#new_msg=ask(message) 
new_msg=ask(5)
print(new_msg)
"""

def expiry_date(day,month,year="2029"):
    print("Day :  " + day +"\n"+"Month : "+ month +"\n"+"Year : "+year)
#expiry_date("02","jan")    #def arg
#expiry_date("02","jan","2040") 
expiry_date("02","jan",year="2040")    #also call along with the variable name



