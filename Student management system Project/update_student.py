import sqlite3
def update_student():
    connection=sqlite3.connect("school.db")
    cursor=connection.cursor()

    #Take input
    student_id=int(input("Enter Student ID to Update"))
    new_course=input("Enter New Course:")

    #Update Query
    cursor.execute("""
    UPDATE students
    SET course=?
    WHERE id=?
    """,(new_course,student_id))
    #save changes
    connection.commit()

    if cursor.rowcount==0:
        print("No student found with that Id.")
    else:
        print("Student Data Updated Successfully")
    connection.close()    
if __name__=="__main__":
    update_student()