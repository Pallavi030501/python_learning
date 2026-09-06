#fliter::::: used to extract the elements from a iterable(list,tuple,set)
#  which statsisfy the given condition ,which returns true only

#ex-1:----- findout the words stat with a
#syntax:: fliter(function,iterable)

fruits=["apple","banana","cherry","avocado","orange","almond"]

def starts_with_a(char):
    return  char.startswith("a")

result=filter(starts_with_a,fruits)
print(result) #fliter object
print(list(result)) #--convert fliter object to list

#using lambda
num=[12,54,90,45,23,76,43,11,32]
teentigda=filter(lambda x:x%3==0,num)
print(list(teentigda))

#fliter() with None----remove falsy value like empty string,None,0
list_type=["apple","berry"," ",0,23,"Aman","","None",None,98]
newlist=filter(None,list_type)
print(list(newlist))

#ques
words = ["apple", "", "banana", "", "cherry"]
non_empty = filter(None, words)
print(list(non_empty))