import sqlite3

conn = sqlite3.connect("urls.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()

# for loop to iterate over the data
for row in rows:
    print(row)

conn.close()

