
import sqlite3
import csv


con = sqlite3.connect("medicine.db")
cur = con.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS Medicine(
    Med_Id INTEGER PRIMARY KEY,
    Med_Name TEXT,
    Qty INTEGER,
    Rate REAL
)
""")


medicines = [
    (1, 'Crocin', 10, 20),
    (2, 'Calpol', 15, 25),
    (3, 'Combiflam', 12, 30),
    (4, 'Dolo', 20, 15),
    (5, 'Paracetamol', 25, 10),
    (6, 'Cetrizine', 10, 12),
    (7, 'Amoxicillin', 8, 50),
    (8, 'Cough Syrup', 5, 80),
    (9, 'Vitamin C', 10, 40),
    (10, 'Aspirin', 15, 20)
]

cur.executemany("""
INSERT OR IGNORE INTO Medicine
(Med_Id, Med_Name, Qty, Rate)
VALUES (?, ?, ?, ?)
""", medicines)

con.commit()


try:
    cur.execute("ALTER TABLE Medicine ADD COLUMN Total REAL")
except sqlite3.OperationalError:
    pass


cur.execute("UPDATE Medicine SET Total = Qty * Rate")
con.commit()


print("Medicines Starting with C:")

cur.execute("""
SELECT * FROM Medicine
WHERE Med_Name LIKE 'C%'
""")

for row in cur.fetchall():
    print(row)


cur.execute("SELECT * FROM Medicine")
records = cur.fetchall()

cur.execute("PRAGMA table_info(Medicine)")
columns = [col[1] for col in cur.fetchall()]

with open("medicines.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(columns)
    writer.writerows(records)

print("Data exported to medicines.csv")

con.close()
