import re, os
import requests
from Prompt import prompt
from bs4 import BeautifulSoup

def title(titles):
    buffer = ""
    count = 0
    titles = titles.split(" , ")
    search = []
    new_titles = []
    
    for i in titles:
        count += 1
        buffer += f"{str(count)}.{i}\n"
        
    buffer = f"""Create titles to search the web\n{buffer}"""
    print(f"\nPROMPT:::\n{buffer}\n\n")
    completion = prompt.Prompt(buffer)
    completion.insertMongo()
    completion = completion.filtered()
    completion = completion.splitlines()
    print("COMPLETION = ", completion)
    for i in completion:
        cleaner = i.split(".")
        title = cleaner[1:]
        print("TITLE = ", title)
        if title != []:
            search.append(' '.join(title))

    print("SEARCH = ", search)

    for title in search:
        count = 0

        try:
            while True:
                count += 1
                res = requests.get(
                    f"https://www.bing.com/search?q={title}"
                )
                
                soup = BeautifulSoup(res.text, "lxml")
                if soup.find_all('h2') != []:
                    break
                if count == 1000:
                    break

        except Exception as error:
            print("CRASH > ", str(error))
            raise error
        
        for i in soup.find_all('h2'):
            print("TESTE = ", i)
            try:
                href = re.findall("\w*://\w*.\w*.*", str(i))
                href = href[0].split("""">""")
                if href != []:
                    new_titles.append(href[0])
                    print("NEW TITLES", ' , '.join(new_titles))
                    break
            except Exception as error:
                print("CRASH > ", str(error))
                raise error

    return new_titles         