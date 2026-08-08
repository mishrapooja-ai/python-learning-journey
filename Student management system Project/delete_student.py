import sqlite3
def delete_student():
    connection=sqlite3.connect("school.db")
    cursor=connection.cursor()

    #Take input
    student_id=int(input("Enter student Id to Delete"))

    #Take query
    cursor.execute("""
    DELETE FROM students
    WHERE id=?
    """,(student_id,))
    connection.commit()
    
    if cursor.rowcount==0:
        print("No student with that id found")
    else:
        print("Student data updated successfully")

    connection.close()
    if __name__=="__main__":
        delete_student()