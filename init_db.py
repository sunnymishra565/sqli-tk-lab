import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cur.execute("INSERT INTO users (username,password) VALUES (?,?)", ("admin","adminpass"))
cur.execute("INSERT INTO users (username,password) VALUES (?,?)", ("sunny","mypassword"))
conn.commit()
conn.close()
print("DB initialized: users.db created with 2 users")
