n = [2, 3, 4, 5]
res = [val ** 2 for val in n]
print("square of numbers",res)

#using conditional statement in list
num=[2,8,45,10,34,75,67]
even_num=[value for value in num
          if value%2==0]
print("the even numbers are : ",even_num)

#Creating a list from a range:

List_1 = [i for i in range(10)]
print(List_1)

#nested loop
pairs = [(i, j) for i in range(2) for j in range(2)]
print(pairs)
