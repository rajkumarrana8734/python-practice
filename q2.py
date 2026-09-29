import sqlite3
import csv


conn = sqlite3.connect(r"C:\sqlite\StoreDB.db")
cur = conn.cursor()


try:
    cur.execute("ALTER TABLE Cust_Master ADD COLUMN email_id TEXT")
    conn.commit()
    print(" 'email_id' column successfully added to Cust_Master table.")
except sqlite3.OperationalError as e:

    print(" Note:", e)

cur.execute("UPDATE Cust_Master SET email_id = 'rahul@gmail.com' WHERE Cid = 1")
cur.execute("UPDATE Cust_Master SET email_id = 'priya@yahoo.com' WHERE Cid = 2")
conn.commit()

cur.execute("SELECT * FROM Cust_Master")
rows = cur.fetchall()

col_names = [description[0] for description in cur.description]


with open("customers.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(col_names)  
    writer.writerows(rows)      

print("All customer data exported to 'customers.csv' successfully.")


conn.close()
