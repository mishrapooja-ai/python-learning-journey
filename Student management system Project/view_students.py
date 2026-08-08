import sqlite3
def view_students():
    connection=sqlite3.connect("school.db")
    cursor=connection.cursor()

    #Fetch all Students
    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()
    print("\n============Student Records==============\n")
    if len(students)==0:
        print("No students found.")
    else:
        for student in students:
            print(f"ID     : {student[0]}")
            print(f"Name   : {student[1]}")
            print(f"Age    : {student[2]}")
            print(f"Course : {student[3]}")
            print("-" * 35)
            connection.close()
if __name__ =="__main__":
    view_students()            