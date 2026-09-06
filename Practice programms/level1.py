#WAp to print " Hello World! " on the screen

print("Hello,World!")

#WAp to read two numbers and print theirsum
"""

num=int(input("Enter first num ::"))
num2=int(input("Enter second num ::"))
sum=num+num2
print(sum)


#difference
diff=num-num2
print(diff)
#product
prod=num*num2
print(prod)
#quotient
quo=num/num2
print(quo)
rem=num%num2
print(rem)

"""

#Wap to print area,radius,circumferenece of a circle

"""
radius=int(input("Enter the radius of circle ::"))
Area= 22/7*(radius*radius)
print("Area of the circle" ,Area)
circumference=2*22/7*radius
print("circumfrence of circle",circumference)
"""
#WAP to read length and bredth of a rectangele and prints its area & perimeteer
"""

length=int(input("enter rectangle length ::"))
breadth=int(input("enter rectangle breadth ::"))

area=length*breadth
print("Area of the recatangle ::",area)

peri=(length+breadth)/2
print("Perimeter of the recatangle ::",peri)
"""

#WAP  to swap two numbers using third variable
"""

x=int(input("Enter 1st number::"))
y=int(input("Enter 2nd number::"))


z=x
x=y
y=z

print(x)
print(y)
print(z)
"""
#withoujt using third variable

"""
x,y=y,x


print(x)
print(y)

"""

#wAP to read a temp  in celsisus and convert it to fahrenite
"""

temp=int(input("Enter a temp ::"))
farh=temp*1.8+32
print(farh)

"""
#Wap to read the marks of 5 sub and print total and average
"""

math=int(input("enter mark of math ::"))
phy=int(input("enter mark of phy ::"))
bio=int(input("enter mark of biology ::"))
eng=int(input("enter mark of english ::"))
chem=int(input("enter mark of chemestry::"))

Total=math+phy+bio+eng+chem
print("total marks ::",Total)

average=Total/5
print("Average of marks ",average)
"""

#WAP to read seconds and coverts them into hours,minute,seconds

seconds=int(input("Enter in Seconds :::")) 

minutes=seconds/60
letseconds=seconds%60

hours=minutes/60
letminutes=minutes%60

print("hours",int(hours))
print("minutes",int(letminutes))
print("seconds",int(letseconds))
