import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()
cur.execute('SELECT * FROM threads')
print(cur.fetchall()) 
con.close()