
import sqlite3

# Connect to database
con = sqlite3.connect("student.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

# Insert student data
name = input("Enter student name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

cur.execute(
    "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
    (name, age, course)
)

con.commit()

# Display all students
cur.execute("SELECT * FROM students")
students = cur.fetchall()

print("\nStudent Records:")
for student in students:
    print(student)

# Close database
con.close()
