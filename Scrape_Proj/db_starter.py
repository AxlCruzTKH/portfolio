import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()

cur.execute('''CREATE TABLE threads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subforum text, 
    link text, 
    thread_creator text, 
    last_post_date text, 
    last_post_time text,
    number_of_replies int,
    number_of_views int
    )''')