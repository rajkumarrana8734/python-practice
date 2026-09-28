import sqlite3

con = sqlite3.connect("company.db")
cur = con.cursor()

cur.execute("""
    create table if not exists employee(
       id integer primary key,
       name text,
       salary real,
       department text
)
""")
cur.execute("DELETE FROM employee")

cur.execute("insert into employee values(1,'rahul',20000,'it')")
cur.execute("insert into employee values(2,'raj',200000,'ceo')")
cur.execute("insert into employee values(3,'narayan',45000,'banking')")
cur.execute("insert into employee values(4,'rohon',80000,'hr')")
cur.execute("insert into employee values(5,'babu',20000,'it')")

con.commit()
print("employee table crated successfully")
print("2 record insert successfully")

cur.execute("select * from employee")
for i in cur.fetchall():
    print(i)

con.close()




