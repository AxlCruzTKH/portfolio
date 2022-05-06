import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS threads_test')
cur.execute('CREATE TABLE threads_test AS SELECT * FROM threads')
con.close()