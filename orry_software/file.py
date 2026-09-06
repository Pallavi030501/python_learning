"""
file=open("data.txt")
print(type(file.read()))
////
print(file.read())
file.close()
///

file_data=file.read()
if "textbook" in file_data:
    print("present")
else:
    print("not present") 
file.close()

"""

#automatic close : no need to close file and if any exception comes it close file
"""
#reading and checking file if str present
with open("data.txt") as file:
    file_data= file.read()
if "python" in file_data:
    print("present")
else:
    print("not present") 

"""
"""
#reading file by each line
with open("data.txt") as file:
    n=0
    for each_line in file:
      n+=1
      #print(each_line) 

      print(n,each_line.rstrip("\n"))
"""

"""

#writing to a file
with open("data.txt",mode ="at") as file:
     #char_added=file.write("hello datas \n")
     char_added=file.write("lets read the file \n")
     print(char_added," character added to the file : ")
"""
     
     