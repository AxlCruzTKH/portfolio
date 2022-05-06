import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS threads')
cur.execute('''CREATE TABLE  politics_and_continuing_crises(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    thread_title text, 
    link text, 
    thread_creator text, 
    date_time_of_last_post text,
    number_of_replies int,
    number_of_views int
    )''')