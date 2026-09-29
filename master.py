import sqlite3


conn = sqlite3.connect(r"C:\sqlite\StoreDB.db")


cur = conn.cursor()


cur.execute("SELECT * FROM Prod_Master")
rows = cur.fetchall()

print("Pid\tPName\t\tCompany\t\tPrice\tQty")
print("-" * 55)


for row in rows:
    print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}")


conn.close()
