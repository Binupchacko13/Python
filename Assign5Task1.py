# Dictionary search
student={'Anjana':76,'Vyshnav':85,'Sooryadev':80,'Akhil':71,'Faheem':65}
name=input("Name of student : ")
if student.get(name):
  print(f"Marks : {student[name]}")
else:
  print("Not found")  