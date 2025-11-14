# File and Exception handling
try:
  with open("/sample.txt","rt") as f1:
    contents=f1.read()
  print(contents)  
except FileNotFoundError:
  print("File doesn't exist")  