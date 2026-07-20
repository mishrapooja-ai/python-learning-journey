contacts={
"Pooja":"1234567890",
"Ankita":"0987654321",
"Leena":"5674376767",
"Kriti":"3543273674",

}
print("Welcome to Contact Book")
print(contacts)
print("All Contacts")
for name,number in contacts.items():
    print(name,":",number)

#Search Contacts
print("Searching Contacts")
print("Leena's  Contact NUmber is:")
print(contacts["Leena"])
#Adding Contact Number
print("Adding Muskan's Number")
contacts["7767637677"]="Muskan"
print(contacts)

#Removing Contacts
print("Removing kriti's contact number")
contacts.pop("Kriti")
print(contacts)

#Final Contact Book
print("\n Final Contact Book")
for name,number in contacts.items():
    print(name,":",contacts)
