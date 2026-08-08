from add_student import add_student
from view_students import view_students
from update_student import update_student
from delete_student import delete_student
print("\n =============STUDENT MANAGEMENT SYSTEM==================\n")
print("1. Add Student")
print("2. View Student")
print("3.Update Student")
print("4. Delete Student")
print("5.Exit")
choice=input("Select your choice(1-5):")
print("Your entered choice:",choice)
if choice == "1":
    add_student()

elif choice == "2":
    view_students()

elif choice == "3":
    update_student()

elif choice == "4":
    delete_student()

elif choice == "5":
    print("Thank you for using Student Management System.")

else:
    print("Invalid Choice")