#reduce()-combining  elements of an iterable and give one single value
#reduce(function,iterable[,initializer])

#from list make a sentence
from functools import reduce
list1=["Hello","Janeman","How","do","you","do","?"]
sentence=reduce(lambda x,y:x+" "+y,list1)
print(sentence)


print("-------------------------------")

#using intializer



num=[23,7,5,1,3,5,6]
def add(x,y):
    return x+y
result=reduce(add,num,20) 
#20-intializer(the reduction starts with 20 intial value so, result 20+50)
print(result)

#find out largest num

n=[67,54,32,90,12]
largestnum=reduce(lambda x,y:x if x>y else y,n)
print(largestnum)


import operator

n1=[1,4,7,9]
print(reduce(operator.add,n1))
"""
import functools
print(functools.reduce(operator.add,n1))
"""
print(reduce(operator.sub,n1))
print(reduce(operator.mul,n1))
print(reduce(operator.add,["hi","beautiful","!"]))#--concatination

#accumulate()-used for sequence it returns intermediate
#  results of iterable in a list format
#  while reduce() returns final result a single value

#difference
#reduce()-import functools --single value as final result--returns single value
#accumulate()-import itertools-intermediate results-returns ierator

from itertools import accumulate
from operator import add
number=[12,34,6,9,10]
result1=accumulate(number,add)
print(list(result1))


#ques
#from functools import reduce
nums = [2, 3, 4]
result = reduce(lambda x, y: x * y, nums)
print(result)