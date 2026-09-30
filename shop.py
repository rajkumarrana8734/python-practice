import sqlite3

con = sqlite3.connect("shop.db")
cur = con.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    quantity INTEGER,
    category TEXT
)
""")


cur.execute("DELETE FROM product")


cur.execute("INSERT INTO product VALUES(1,'Laptop',45000,5,'Electronics')")
cur.execute("INSERT INTO product VALUES(2,'Mobile',20000,10,'Electronics')")
cur.execute("INSERT INTO product VALUES(3,'Keyboard',1200,20,'Computer')")
cur.execute("INSERT INTO product VALUES(4,'Mouse',600,25,'Computer')")
cur.execute("INSERT INTO product VALUES(5,'Headphone',1500,15,'Electronics')")
cur.execute("INSERT INTO product VALUES(6,'Monitor',12000,8,'Computer')")
cur.execute("INSERT INTO product VALUES(7,'Printer',9000,6,'Office')")
cur.execute("INSERT INTO product VALUES(8,'Speaker',2500,12,'Electronics')")
cur.execute("INSERT INTO product VALUES(9,'Webcam',1800,10,'Computer')")
cur.execute("INSERT INTO product VALUES(10,'Tablet',18000,7,'Electronics')")

con.commit()

print("Product table created successfully")
print("10 records inserted successfully")


print("\nProduct Records:")

cur.execute("SELECT * FROM product")

for row in cur.fetchall():
    print(row)

con.close()
