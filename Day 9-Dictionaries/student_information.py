#Student Information System
student={
    "name":"Pooja",
    "age":26,
    "city":"Mumbai",
    "Course":"Python",
    "Country":"India"
}
print("\n Student Information:")
print(student)

#Access Individual values
print("Student Name:",student["name"])
print("Student Age:",student["age"])
print("Student City:",student["city"])
print("Student Course:",student["Course"])
print("Student Country:",student["Country"])

#Update Information
print("Updated Informaation:" )
student["Course"]="Artificial Intelligence"
print(student)


#Add new Information
print("Added Information:")
student["Dream Job"]="AI Engineer"
student["Github"]="Pooja Mishra"
print(student)

#Removing Information

student.pop("city")

print("\nAfter Removing City")
print(student)