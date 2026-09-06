# local variable
"""
def print():
    name="jinaa" #local var only access in block
    print(name)
#print() #notpossible
"""

# global
name = "Jinaa"


def printname():
    name = "richaa"
    print(name)


printname()  # priority goes to local var
print(name)  # local var cant use out of block


# global declare
name = "tiger"


def hello():
    global name
    name = "alok"
    print(name)


hello()
print(name)

#assignment
for i in range(5):
    if i == 2:
        pass
        print(i)
    print(i)

def check_even_or_odd(num):
    if num % 2 == 0:
        pass
    else:
        print("Odd")
    print("Done")
check_even_or_odd(5)