import sqlite3

# Connect to SQLite database (creates library.db if it doesn't exist)
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# 1. Create the Book table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Book (
        BookID INTEGER PRIMARY KEY,
        BookName TEXT NOT NULL,
        Author TEXT NOT NULL,
        Price REAL NOT NULL,
        Category TEXT NOT NULL
    )
''')

# Insert at least 8 book records
books_data = [
    (1, "Python Programming", "Guido van Rossum", 650.0, "Computer"),
    (2, "Database Systems", "Elmasri", 800.0, "Computer"),
    (3, "Organic Chemistry", "Morrison", 450.0, "Science"),
    (4, "Financial Management", "Prasanna Chandra", 950.0, "Management"),
    (5, "Data Structures", "Mark Weiss", 550.0, "Computer"),
    (6, "Physics Vol 1", "Resnick Halliday", 400.0, "Science"),
    (7, "Marketing Management", "Philip Kotler", 1100.0, "Management"),
    (8, "Operating Systems", "Galvin", 480.0, "Computer")
]

# Insert records (using INSERT OR IGNORE to prevent primary key violation if run multiple times)
cursor.executemany('''
    INSERT OR IGNORE INTO Book (BookID, BookName, Author, Price, Category)
    VALUES (?, ?, ?, ?, ?)
''', books_data)
conn.commit()

print("--- Database 'library.db' and 'Book' Table Created with Records ---")

# Operation a: Display details of books whose price > 500 and category is 'Computer'
print("\n--- Books with Price > 500 and Category 'Computer' ---")
cursor.execute("SELECT * FROM Book WHERE Price > 500 AND Category = 'Computer'")
for row in cursor.fetchall():
    print(row)

# Operation b: Display category-wise number of books and average price using GROUP BY and HAVING
print("\n--- Category-wise Book Count and Average Price ---")
cursor.execute('''
    SELECT Category, COUNT(*) AS TotalBooks, AVG(Price) AS AvgPrice 
    FROM Book 
    GROUP BY Category 
    HAVING COUNT(*) >= 1
''')
for row in cursor.fetchall():
    print(f"Category: {row[0]}, Count: {row[1]}, Avg Price: ₹{row[2]:.2f}")

# Operation c: Display books whose category is 'Science', 'Computer', or 'Management' using IN, sorted by price DESC
print("\n--- Books in Science, Computer, or Management Sorted by Price (DESC) ---")
cursor.execute('''
    SELECT * FROM Book 
    WHERE Category IN ('Science', 'Computer', 'Management') 
    ORDER BY Price DESC
''')
for row in cursor.fetchall():
    print(row)

# Close the database connection
conn.close()