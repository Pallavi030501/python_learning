list=["hello","narayan"]
vegetables=["papaya","cucumber","onion","patato","green chilly",23]
print(vegetables)
print(vegetables[2])

#list checking : in keyword
print ("onion" in vegetables) #true
print("bringal" in vegetables) #false

print(len(vegetables))

vegetables.append("Bringal")
print(vegetables)
print("Bringal" in vegetables) #true
vegetables.pop() #remove last element
print("Bringal" in vegetables) #false
vegetables.pop()
print(vegetables)


print(vegetables[0:3]) #[start:end+1] def-[0:len-1]
print(vegetables[:3]) 
print(vegetables[0:]) 
print(vegetables[2:5])
print(vegetables[::1])  #::1-def for skip
print(vegetables[::2]) 
print(vegetables[-1:]) #last eleemnt
print(vegetables[-3:])
print(vegetables[1:-1]) 

#reverse a list
print(vegetables[::-1])

print("-----------------------")
for items in vegetables:
    print(items)

my_name="Narayan"
print(my_name[0]) 
#wap to check if a character present in a string
for character in my_name:
    print(character)
    if character=="r":
        print("present")
        break
    """
    else:
        print("not present")    
    """

print("r" in my_name)

#optimize code
def check_char(name,alpha):
    if alpha in name:
        print(alpha," present")
    else:
        print(alpha,"not present")    


check_char(my_name,"n")
check_char(vegetables,"patato")
check_char(vegetables,"carrot")


 


