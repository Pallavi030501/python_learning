tup = ("hi", 12, "narayan", 56)
print(tup)
# tup -immutable and list --mutable
couple = ("Jina", "Richa")
# tuple unpacking
groom, bride = couple
print("Groom : ", groom)
print("Bride : ", bride)
groom = couple  # it assign like a variable
print("Groom : ", groom)


print(couple[0]+" weds "+couple[1])

city = ["bbsr", "kerala", "bangalore"]
city[0] = "bhubaneswar"
print(city)
city_pin = ("bbsr", 751003)

# list of tuples
city_pincode = [("bbsr", 751003), ("bangalore", 560078), ("berhampur", 76121)]
print(city_pincode)
print(city_pincode[1])  # ('bangalore', 560078)

print(city_pincode[0][1])  # 751003

# city[0][0]="bhubaneswar"
# print(city_pincode) #   tuple immutable

state_capital = [("Karnataka", "Bengaluru"), ("Odisha", "Bhubaneswar"), ("Maharashtra	", "Mumbai")]
print(type(state_capital))
print(type(state_capital[0]))

#print each state and its capital using a function
"""
def print_state_capital(list1):
    for details in list1:
        print("state :",details[0])
        print("capital :",details[1])
print_state_capital(state_capital)
"""
#another
def print_state_capital(state_capital):
    for each in state_capital:
        state,capital=each;
        print("-----------------")
        print("state: ",state)
        print("capital: ",capital)
        print("-----------------")
print_state_capital(state_capital)        

def xy():
    return 1, 2  # def-tuple (1,2)


print(xy())
print(type(xy()))

#just like tuple we can also unpack list
state_capital = [("Karnataka", "Bengaluru"), ("Odisha", "Bhubaneswar"), ("Maharashtra	", "Mumbai")]
kannad,odia,marathi=state_capital
print(type(odia)) #<class 'tuple'>

print(kannad[0])
print(kannad[1])
print(odia[0])
print(odia[1])
print(marathi[0])
print(marathi[1])



