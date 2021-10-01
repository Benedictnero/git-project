import requests
import bs4

def getdata(url):
    r = requests.get(url)
    return r.text


http_url = input("Enter web URL:  ")

htmldata  = getdata(http_url)

soup = bs4.BeautifulSoup(htmldata, 'html.parser')

for item in soup.find_all('img'):
    print(item['src'])
