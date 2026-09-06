"""
#notetaking app using open(),write()
from datetime import datetime

notes=input("please take note \n >")

with open("note.txt",mode ="a") as file:
   content=str(datetime.now().date())+"\n"+" "+notes+"\n"
   file.write(content)
"""
"""
#create a file in home dir or in same folder and write it to(no append)
from pathlib import Path
#file=Path.home()/"pallavi.txt" #home dir open file

file=Path("pallavi.txt")
file.write_text("hello  meowwww",encoding="utf-8")

print(file.read())
"""

from pathlib import Path
file_path=Path("pallavi.txt")
with file_path.open("a",encoding="utf-8") as file:
    file.write("hi pallavi! \n")

print(file_path.read_text())
