import sqlite3

# 1. Database se connect karein
conn = sqlite3.connect(r"C:\sqlite\student_data.db")
cursor = conn.cursor()

# 2. Query chalayein
cursor.execute("SELECT * FROM tbldept")
records = cursor.fetchall()

# 3. Heading aur Data Display Karein
print(f"{'Dept ID':<10} {'Dept Name':<15} {'Location':<15}")
print("-" * 40)

for row in records:
    print(f"{row[0]:<10} {row[1]:<15} {row[2]:<15}")

# 4. Connection Close
conn.close()
