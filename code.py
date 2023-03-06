import time
import requests
from bs4 import BeautifulSoup

href = "https:"

dailyStar = "https://www.thedailystar.net"

prothomeAloUrls =[
    "https://www.prothomalo.com",
    "https://www.prothomalo.com/collection/latest",
    "https://www.prothomalo.com/collection/special-news"
]

dailyStarUrls=[
    "https://www.thedailystar.net",
    "https://www.thedailystar.net/news",
    "https://www.thedailystar.net/opinion",
]

banglaTribuneUrls =[
    "https://www.banglatribune.com",
    "https://www.banglatribune.com/national",
    "https://www.banglatribune.com/business",
]

ittefaqUrls =[
    "https://www.ittefaq.com.bd",
    "https://www.ittefaq.com.bd/politics",
    "https://www.ittefaq.com.bd/video"
]

def scrape_prothomeAlo():
    for url in prothomeAloUrls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        prothomeList = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        data = []
        for news in prothomeList:
            if news.parent.parent.get('href') or news.parent.get('href'):
                link = news.parent.parent.get('href') or news.parent.get('href')
                title = news.find('span', class_ = 'tilte-no-link-parent')
                if title and link:
                    data.append((link, title))
        return data



def scrape_dailyStar():
    for url in dailyStarUrls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        dailyStarList = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
        data = []
        for news in dailyStarList:
            if news.a['href']:
                link = dailyStar + news.a['href']
                title = news.a.text
                if title and link:
                    data.append((link, title))
        return data
    

def scrape_banglaTribune():
    for url in banglaTribuneUrls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        banglaTribuneList = soup.find_all("div", class_ = 'each')
        data = []
        for news in banglaTribuneList:
            if news.a['href']:
                link = href + news.a['href']
                title = news.a.text
                if title and link:
                    data.append((link, title))
        return data
    

def scrape_itteFaq():
    for url in ittefaqUrls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        ittefaqList = soup.find_all("div", class_ = 'each')
        data = []
        for news in ittefaqList:
            if news.a['href']:
                link =href + news.a['href']
                title = news.a.text
                if title and link:
                    data.append((link, title))
        return data



data = []
data.extend(scrape_prothomeAlo())
data.extend(scrape_dailyStar())
data.extend(scrape_banglaTribune())
data.extend(scrape_itteFaq())


#collect data after every 15 minutes
while True:
    with open("code.html", "w", encoding="utf-8") as f:
        f.write("<html><head><title>News Sites Scrapping</title></head><body><h1 style = 'color:blue; text-align:center'>News Sites Scrapping</h1>")
        for (link, title) in data:
            f.write(f'<p><a href="{link}">{title}</a></p>')
        f.write("</body></html>")
    print("file written successfully !!!")
    time.sleep(900)