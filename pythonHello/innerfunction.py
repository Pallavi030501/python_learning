#inner()-function inside function
#usecases- 
##Encapsulation-hiding code
##2.code organization:-Grouping related functionality for cleaner code.
##3.access to outer variables:: inner fun can use variables of outer fun
##4.Closures and Decorators: Supporting advanced features like closures (functions that remember values) and function decorators.


##Examples::::::::::::::::

#acess outer variables

# outer function
def fun1(msg):  
    # inner function
    def fun2():
         # access variable from outer scope
        print(msg) 
    fun2()
fun1("Hello")

#LEGB RULE- local--enclosing--global--builtin
def function1(): 
    sentence = "Geeks for geeks"
    def func(): 
        print(sentence) #scope-inner() can access variables of enclosing/outer()

    func()
function1()


def heyaa(word):
    num=87
    def bye():
        nonlocal num
        #nonlocal keyword --- used for inner function to modify a variable 
        # from the outer function instead of creating a new local copy.
        num=23
        print("number is :",num)
    bye()
    print("fun1 number is: ",num)
heyaa("kiwi")        

#closure()
def fun1(a):  
    def fun2():
        print(a)  
    return fun2 

closure_func = fun1("Hello, Closure!")
closure_func()



def process_data(data):
    def clean_data():
        return [item.strip() for item in data] 
    return clean_data()
print(process_data(["  banglore  ", "         Railway Station "]))



##exxx
def outer():
    def inner():
        return "Hello from inner"
    return inner()
print(outer())