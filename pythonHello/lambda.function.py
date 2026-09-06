# lambda does not have a name
def result(num): return print(num+8)
# result=fun name,lambda-keyword, num -argument,
# num+8--expression


result(40)

# usecase------------>
# 1.condition checking:::::::::::::


def checkresult(
    num): return "positive" if num > 0 else "negative" if num < 0 else "zero"


print(checkresult(-56))


# 2.list comprehension::::::::::::
list = [lambda num=x: num*20 for x in range(1, 7)]

for i in list:
    print(i())
