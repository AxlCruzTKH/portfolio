from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import re
from datetime import date
from datetime import timedelta
import sqlite3
import datetime




def run(playwright,starting_i,ending_i,cur,subforum):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    for i in range(starting_i,ending_i+1):
        if i == 1:
            page.goto('https://www.stormfront.org/forum/f191')
            time.sleep(10)
        else:
            page.goto(f'https://www.stormfront.org/forum/f191-{i}')
            time.sleep(10)
        
        zed = page.inner_html('tbody#threadbits_forum_191')
    
        soup = BeautifulSoup(zed, 'html.parser')

        list_of_posts = soup.find_all('tr')

        for post in list_of_posts:
            list_of_data = post.find_all('td')
            
            title_container,last_post_container,replies_container,views_container = list_of_data[2],list_of_data[3],list_of_data[4],list_of_data[5]

            #Extract the title of the thread
            title = title_container.find_all('a',id = re.compile(r'thread_title'))[0].text
            link_to_thread = title_container.find_all('a',id = re.compile(r'thread_title'))[0]['href']


            #extract the poster
            poster = title_container.find_all('div',class_='smallfont')[0].text

            #Extract the time of last post
            try:   
                last_post_time = last_post_container.find_all('div',class_ ='smallfont')[0].text
                last_post_time = re.search(r'([0-9]{2}):([0-9]{2})\s\w{2}',last_post_time)
                last_post_time = last_post_time.group(0)
            except:
                continue
            #Extract the date of the last post
            
            try:
                last_post_date = last_post_container.find_all('div',class_ ='smallfont')[0].text
                last_post_date = re.search(r'.+?(?=\s)',last_post_date)
                last_post_date = last_post_date.group(0)
            except:
                continue


            #Case Statement to standardize date
            if last_post_date=='Today':
                last_post_date = date.today()
                last_post_date = date.today().strftime('%m-%d-%Y')
            elif last_post_date=="Yesterday":
                last_post_date= (date.today() - timedelta(days=1))
                last_post_date = last_post_date.strftime('%m-%d-%Y')
                
            else:
                pass

            #get the amount of replies
            number_of_replies = replies_container.find_all('a',rel='nofollow')[0].text

            #get the amount of views
            number_of_views = views_container.text

            #fix date_time
            date_time_of_last_post = datetime.datetime.strptime(last_post_date + " " + last_post_time,'%m-%d-%Y %I:%M %p')

            cur.execute('INSERT INTO politics_and_continuing_crises(thread_title,link,thread_creator,date_time_of_last_post,number_of_replies,number_of_views) VALUES (?,?,?,?,?,?)',(title.strip(),link_to_thread,poster.strip(),date_time_of_last_post,number_of_replies,number_of_views))
            con.commit()
    browser.close()
        
        
            

with sync_playwright() as playwright:
    con = sqlite3.connect('main.db')
    cur = con.cursor()
    run(playwright,1,5,cur,'Politics & Continuing Crises')
    con.close()
    

