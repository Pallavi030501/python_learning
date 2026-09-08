#print 1 to 10 using range

for x in range(0,11):
    print(x)

for evennos in range(0,11,2):
    print("even numbers :" ,evennos)

for oddnos in range(1,11,2):
    print("odd numbers:",oddnos)

print("-------------")
for x in range(11,0,-1):
     print("reverseno : ",x)

msg="Python is a stastical language" 
print(msg[0:4:2])    #slicing

print(list(range(5,15,3))) #range is return value to list

#enumerate

print("enumerate ::::::::::::   ")

family=["father","mother","brother","sister"]

#using count
for member in range(len(family)):
    print(member+1,family[member])

#enumerator create tuples as per count and returns back it as tuple
for member in enumerate(family):
    print(member)    
    count ,member=member
    print(count+1,member)
print("*******---")
#enumerate is being used to provide count of given data or list
for count,member in enumerate(family,start=9):
    print(count+1,member)    