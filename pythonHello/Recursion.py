# recursion calling the same function in such way which reduces code complexicity
# fuctions call itself either directly or indirectly


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(5))

#fibonacci::: 0,1,2,3,5,8,13

