import sqlite3

conn=sqlite3.connect("teacher.db")
cur=conn.cursor()

cur.execute("""
create table if not exists teacher(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    subject TEXT NOT NULL
)
""")

cur.execute("delete from teacher")

cur.execute("insert into teacher values(1,'John Doe','Mathematics')")
cur.execute("insert into teacher values(2,'Jane Smith','Science')")
cur.execute("insert into teacher values(3,'Emily Johnson','English')")
cur.execute("insert into teacher values(4,'Michael Brown','History')")
cur.execute("insert into teacher values(5,'Sarah Davis','Art')")

conn.commit()

print("Teacher table created successfully")

print("5 records inserted successfully")

print("\nTeacher Records:")

cur.execute("select * from teacher")

for row in cur.fetchall():
    print(row)

conn.close()