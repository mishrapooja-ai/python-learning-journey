import sqlite3
#Connect to database
connection=sqlite3.connect("school.db")
#create cursor
cursor=connection.cursor()
#create Student table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")
#Save Changes
connection.commit()
print("Database and Students Table created Successfully")
connection.close()