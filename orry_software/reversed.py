#reverse 

num=[1,2,3,4,5,6]
print(num[::-1]) #sequence -list and tuple

employee={"emp_name":"Pallavi",
          "emp_id":123567,
          "emp_age":24,
          "gender":"female"}

for x in reversed(employee):
    print(x,employee[x])


##while loop:::: looping over a condition

count=1
name="Narayan"
while  count <=5:
    print(name)
    count+=1
