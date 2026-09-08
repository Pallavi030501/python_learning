# non-sequence
# mutable

#define a dict

employee={"emp_name":"Pallavi",
          "emp_id":123567,
          "emp_age":24,
          "gender":"female"}
#update dict
employee["emp_age"]=25
print(employee["emp_age"])

#adding new element-using key indexing
employee["salary"]=100000

print(employee)
#finding an item exit in a dict

print("emp_name" in employee) #True

def printdict(dict):
    for x in dict:
        print(x,dict[x])

printdict(employee)

#delete an item in dict

del employee["emp_age"]
print(employee)

#delete-pop()
deleted_item=employee.pop("gender")
print(deleted_item)
print(type(deleted_item))
print(employee)
