


import sqlite3


def filter_by_date(starting_date,ending_date):
    #has to be in the format %Y-%m-%d
    con = sqlite3.connect('main.db')
    cur = con.cursor()  
    cur.execute('Select * from threads where date_time_of_last_post between strftime("%Y-%m-%d",?) and strftime("%Y-%m-%d",?)',(starting_date,ending_date))
    x = cur.fetchall()
    cur.close()
    return x


print(filter_by_date('2022-05-04','2022-05-05'))



