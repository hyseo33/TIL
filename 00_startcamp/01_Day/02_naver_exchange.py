# import requests
# from bs4 import BeautifulSoup

# url = 'https://finance.naver.com/marketindex/'

# html = requests.get(url).text
# soup = BeautifulSoup(html, 'html.parser')
# exchange = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# print(f'현재의 원/달러 환율은 {exchange.text}입니다.')



import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
ex_eu = soup.select_one('#exchangeList > li:nth-child(3) > a.head.eur > div > span.value')
print(f'현재 원/유로 환율은 {ex_eu.text}입니다.')