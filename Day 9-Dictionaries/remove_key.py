#remove key from dictionary
student={
    "name":"Pooja",
    "age":"26",
    "City":"Mumbai"
}
print(student)
student.pop("age")
print("After removing Age")
print(student)
#delete name 
del student["name"]
print(student)