import sqlite3


conn = sqlite3.connect(r"C:\sqlite\student_data.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM students")
row1 = cursor.fetchone()
print("First Record:", row1)

row2 = cursor.fetchone()
print("Second Record:", row2)

print("\n--- Remaining Records---")
row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()
conn.close()


