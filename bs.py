import requests
from bs4 import BeautifulSoup


url = 'https://www.db.yugioh-card.com/yugiohdb/member_deck.action?ope=1&cgid=c8525f77e0268f9b1ba9110a8a05bc35&dno=47' + '&request_locale=ja'
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")

with open('text.txt', 'w', encoding='UTF-8') as f:
    print(soup, file=f)