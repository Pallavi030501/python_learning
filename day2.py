  
students_count=1500
print(students_count)
is_readable=True
#to store paragraph use 3 double coats
message="""                           
      Hii Smith,
      How are you?
"""
print(message)
course_Name='Python'
print(len(course_Name))  # find the length of element
name="Narayan Sahu " 
print("The length of name is",len(name))
print("the first charcter of name is",name[0]) # get the first element as per first index
print("The last charcter of name is",name[-1])  #get the last element as per last index 
print("The surnmae of the charcter is",name[8 :len(name)]) #to find the specified element mentioned in the ratio as per requirement
print("The surnmae of the charcter is",name[8:])  
print("The surnmae of the charcter is",name[:7]) # default starting index is 0
print("The surnmae of the charcter is",name[:]) #if dont mention any index value it will give entire element
course ="Python \" Programming" # \" it is escape charactor sequence
print(course)
course ="Python \ Programming"
print(course)

course ='Python " Programming' # " it is used to continue the string
print(course)
course = "python \\programming"; #if you want to print on backslace
course = "python \n programming"; # if you want to print progemming in the next line

#------------------CODE FORMATTING-----------------------
first="Pallavi"
last=" Narayan Sahu"
fullname= first +" "+ last
print(fullname)

#__________String Formatting_________________________
print("==========Details===============")
my_name="Narayan"
address=f"{my_name} is living in Bangalore." 
office=f"{my_name} is working in IT industry"
details= address+ office
print(details)
details_intotal=f"  {address} and {"the length of office is"} {len(office)})"
print(details_intotal)

#-------------All string methods in python-------------
name="Richa  "
print(name.upper()) # convert in uppercase
print(name.lower()) # convert in lowercase
print(name.title()) # convert in title
print(name.strip()) # remove the whitespace in beginning and end
print(name.rstrip()) # convert in uppercase
print(name.find("ch")) # find the required charcter value
print(name.replace("c","z")) # replace the charcter
print("chass" in name) #it will return the value in boolean wheather it present
print("pallu" not in name) #it will return the value in boolean wheather it is not prsent









