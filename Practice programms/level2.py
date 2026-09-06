# WAP to read a number and check whether it is even or odd
"""
n1 = int(input("enter a number :: "))

if (n1 % 2 == 0):
    print("even num")
else:
    print("odd num")
"""
# WAP to read a num and check wheather it is +ve,-ve or 0
"""
n = int(input("enter a number :: "))

if (n > 0):
    print("positive num")
elif (n < 0):
    print("negative num")
else:
    print("zero")
"""

# wAP to read three num and find the largest
"""

n1 = int(input("Enter first num : "))
n2 = int(input("Enter second num: "))
n3 = int(input("Enter third num: "))


if (n1 >= n2):
    if (n1 > n3):
        print(" largest num ::: ", n1) 
    elif(n1<n3):
        print("largest num::",n3) 
    else:
        print("n1 and n3 are same")   
elif (n2 >= n1):
    if (n2 > n3):
        print("largest num::", n2)
    elif(n3>n2):
        print("largest num::",n3)
    else:
        print("n3 and n2 are same")
else:
    print("n1 and n2 are same")
"""

# wAP to read three num and find the smallest
"""
n1 = int(input("Enter first num : "))
n2 = int(input("Enter second num: "))
n3 = int(input("Enter third num: "))

if(n1<=n2 and n1<=n3):
    print("smallest num ::",n1)
elif(n2<=n1 and n2<=n3):
    print("smallest num ::",n2)
else:
    print("smallest num ::",n3)       

if(n1>=n2 and n1>=n3):
    print("largest num ::",n1)
elif(n2>=n1 and n2>=n3):
    print("largest num ::",n2)
else:
    print("largest num ::",n3)  
"""
# leap year
"""
year = int(input("enter a year"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year", year)
else:
    print("not a leap year")

"""
# vowel or a cosonant
"""
char=input("enter a charcater :: ")

str="aeiouAEIOU"

if char in str:
    print("vowel")
else:
    print("consonant")    
"""

# read char aqnd check alphabet,digit and symbol
"""
char = input("enter a charcater :: ")

if char.isdigit():
    print("digit")
elif char.isalpha():
    print("alphabet")
else:
    print("symbol")
"""

# marks of the student and print grade A/B/C/D/fail
"""
marks=int(input("enter the marks"))

if(marks>=90):
    print("Grade A")
elif(marks<=90 and marks>80):
    print("Grade B")
elif(marks<=80 and marks>60):
    print("Grade C")
elif(marks<=60 and marks>=30):
    print("Grade D")
else:
    print("Fail")               
"""

# divisible by both 3& 5
"""
num = int(input("enter a number :: "))

if (num % 3 == 0 and num % 5 == 0):
    print("divisible")
else:
    print("not divisible")
"""

#age and eligible or not

age=int(input("Enter age :: "))

if(age>=18):
    print("eligible for vote")
else:
    print("not eligible")    