import sqlite3

# Connect to database
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    email TEXT UNIQUE
)
""")

def add_user(name, email):
    try:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        print("User added successfully!")

    except sqlite3.IntegrityError:
        print("Duplicate data detected! User not added.")

# Add sample data
add_user("Sathya", "sathya@gmail.com")
add_user("Ravi", "ravi@gmail.com")
add_user("Sathya", "sathya@gmail.com")

# Display stored data
cursor.execute("SELECT * FROM users")
print("\nStored Users:")
for row in cursor.fetchall():
    print(row)

conn.close()
