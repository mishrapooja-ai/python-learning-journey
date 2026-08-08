import sqlite3
def add_student():

#Connection to database
    connection=sqlite3.connect("school.db")
    cursor=connection.cursor()

    #Take input from User
    name=input("Enter the name:")
    age=int(input("Enter Age:"))
    course=input("Enter the Course name:")

    #Insert into database
    cursor.execute("""
    INSERT INTO students(name,age,course)
    VALUES(?,?,?)
    """, (name,age,course))


    #Save Changes
    connection.commit()
    print("Student Data Added Successfully")

    #Close Connection
    connection.close()
if __name__=="__main__":
        add_student()

