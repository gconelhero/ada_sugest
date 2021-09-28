import re, os
import requests
from bs4 import BeautifulSoup

class Search():
    def __init__(self, query):
        self.query = query

    def scraping(self):

        res = requests.get(
            f"https://www.bing.com/search?q={self.query}"
        )

        soup = BeautifulSoup(res.text, "lxml")

        for i in soup.find_all('h2'):
            try:
                href = re.findall("\w*://\w*.\w*.*", str(i))
                href = href[0].split("""">""") 
                if href != []:
                    os.system(f"start {href[0]}")
                    break

            except:
                pass