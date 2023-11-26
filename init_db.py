import sqlite3

# Essentially just migrates and seeds db.
connection = sqlite3.connect('database.db')

cur = connection.cursor()

with open('schema.sql') as f:
    cur.executescript(f.read())

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for first post'))

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for second post'))

connection.commit()
connection.close()
