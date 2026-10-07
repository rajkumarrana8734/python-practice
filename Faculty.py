import sqlite3
from datetime import date

con = sqlite3.connect("faculty.db")
cur = con.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS Faculty(
    fac_id INTEGER PRIMARY KEY,
    fac_name TEXT,
    contact_no TEXT,
    course_name TEXT,
    DOJ TEXT
)
""")

# Insert 6 records
cur.execute("INSERT INTO Faculty VALUES(1,'Amit','9876543210','BCA','2026-10-07')")
cur.execute("INSERT INTO Faculty VALUES(2,'Rahul','9876543211','BCA','2026-05-10')")
cur.execute("INSERT INTO Faculty VALUES(3,'Anil','9876543212','BBA','2026-06-15')")
cur.execute("INSERT INTO Faculty VALUES(4,'Rohit','9876543213','MCA','2026-07-20')")
cur.execute("INSERT INTO Faculty VALUES(5,'Ajay','9876543214','BCA','2026-08-12')")
cur.execute("INSERT INTO Faculty VALUES(6,'Neha','9876543215','BBA','2026-09-25')")

con.commit()


print("\nFaculty of BCA course:")
cur.execute("SELECT * FROM Faculty WHERE course_name='BCA'")

for row in cur.fetchall():
    print(row)



print("\nFaculty whose name starts with A:")
cur.execute("SELECT * FROM Faculty WHERE fac_name LIKE 'A%'")

for row in cur.fetchall():
    print(row)



print("\nFaculty whose joining date is today:")

today = date.today().strftime("%Y-%m-%d")

cur.execute("SELECT * FROM Faculty WHERE DOJ=?", (today,))

for row in cur.fetchall():
    print(row)


con.close()