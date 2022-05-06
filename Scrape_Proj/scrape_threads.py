import sqlite3
from playwright.sync_api import sync_playwright
import time


#Structure of a thread
# id = posts ; list of posts
# tr valign = top
# td class = alt2 = user info
# td class = alt1 = post info
# class=hidesig is the signature
# td class al2 in post
# check to see if video linked


con = sqlite3.connect('main.db')


def run(playwright,x):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(x)
    time.sleep(5)

    #stop until there is no next page
    zed = page.inner_html('a')
    browser.close()


with sync_playwright() as playwright:
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    cur.execute('Select * from politics_and_continuing_crises where id=1')
    x = cur.fetchall()
    run(playwright,x[0][2])
    
    con.close()

