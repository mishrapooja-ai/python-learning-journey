#Loop through Dictionary
student={
    "name":"Pooja",
    "age":26,
    "city":"Mumbai",
    "course":"Python"

}
print("Dictionaries Keys:")
for key in student:
    print(key)
    print("Dictionary Values:")
    for value in student.values():
        print(value)
print("\n Keys and Values:")
for key,value in student.items():
    print(key ,":", value)