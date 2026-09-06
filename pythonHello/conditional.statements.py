#
# husband="Narayan"
# if else
"""
name = input("please Enter your name")
if name == "pallavi":
    print("i love you")
else:
    print("Who are you?")
"""
##without colon
name = input("please Enter your name\n")
print("i love you pallavi") if name=="pallavi" else print("who are you?")



# eligible for vote also print senior citizen ornot
age = int(input("enter your age\n"))
print(type(age))  # input always give in string format
if age >= 18:
    print("elgible for vote")
    if age >= 60:
        print("senior citizen")
    else:
        print("not senior citizen")
elif age > 16:
    print(" teenage and go apply vote form")
elif age < 0:
    print("invalid age")
else:
    print("not eligible for vote and a kid just go home")
