import browserTitle
import threading
import time
from scraping import Search
from ctypes import windll

def browsing():
    titles = ""
    windll.user32.MessageBoxW(
    0, "Browsing is started...", "GPT-3 BROWSING", 1
)
    #print('GPT-3 Browsing start...')
    while titles == "":
        search = []
        titles = browserTitle.BrowserTitle()
        titles = titles.title()
        if titles == 'stop':
            windll.user32.MessageBoxW(
    0, "Browsing is stoped...", "GPT-3 BROWSING", 1
)
            break
        if titles != "":
            titles = titles.splitlines()
            for i in titles:
                cleaner = i.split(".")
                titles = cleaner[1:]
                search.append(titles)
            for i in search:
                Search(i).scraping()
            
            titles = ""

browsing()
