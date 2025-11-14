# Appending contents into file
with open("output.txt","at") as f1:
  fs=input("Enter the text to write to file : ")
  f1.write(fs+"\n")
  fs=input("Any more inputs?")
  f1.write(fs)
with open("output.txt","rt") as f1:
  contents=f1.read()
print(contents)    