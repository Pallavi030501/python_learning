

# example-1
# swap two numbers
x = 10
y = 20


print(x, y)
"""

####
z = x
x = y
y = z
print(x, y)
"""
# easy way
x, y = y, x
print(x, y)

print("========================")

arr=[1,8,8,6,7,5,4]

biggest=arr[0]
secondbiggest=0

for i in range(1,len(arr)):
        if arr[i]>biggest:
            secondbiggest=biggest
            biggest=arr[i]
        elif arr[i]>secondbiggest and arr[i]!=biggest:
              secondbiggest=arr[i]

print("biggest :" ,biggest)      

print("secondbiggest :" ,secondbiggest)      
           