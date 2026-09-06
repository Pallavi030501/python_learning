# for loop
'''
List = [1, 13, 45, 67]
for i in List:
    print(i)
'''

# range(first_num,last_num,jump) in python -->excluding last_num
x = range(0, 12, 3)
for i in x:
    print(i)


List = [1, 13, 45, 67]
for i in range(len(List)):
    print(List[i])


# while loop
num = 1
while (num <= 15):
    print(num)
    # num=num+1
    num += 1
print("--------------")
print(num)


print("****************___________*****************")
print("Narayan", end=" ")
print("Sahu Pallavi")


# print pattern

"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print(" ")

for i in range(2):
    print(i)



var = 10
for i in range(10):
    for j in range(2,10,1):
        if var % 2 == 0:
            continue
        else:
            var += 1
print(var)