# pass keyword---->
# if dont want to implement function can use pass  keyword for not interputting on further programme

def function():
    pass


function()

print("heyaaaaaaaaa program going on")


# pass keyword in condition
"""  
day = input("Enter the day : ")
if day == "saturday":
    print("my turn")
elif day == "sunday":
    pass
else:
    print("working day")

"""

# pass keyword in loops

# _---print even numbers in single digit
singledigit = range(0, 10)
# x = input("enter num")
for x in singledigit:
    if x % 2 == 0:
        print("even num: ", x)

    else:
        # print("odd num: ", x)
        pass
