import mysql.connector

# Step 1: Connect
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="yourpassword",
  database="test_db"
)

# Step 2: Cursor
cursor = mydb.cursor()

# Step 3: Insert Data (example)
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Pradnya", "pradnya@example.com"))
mydb.commit()

# Step 4: Read Data
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Step 5: Close connection
cursor.close()
mydb.close()
