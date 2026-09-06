#DEcorators:::::::::::::::::
def decorator(func):
    def innerfun():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return innerfun

@decorator
def functionOFdecorator():
    print("Hello, World!")
functionOFdecorator()


#decorators with parameter
def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))