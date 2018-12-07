# # Stock ticker
from bs4 import BeautifulSoup
import requests

pathVar = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
symbol = "TATAMOTORS"

url1 =  pathVar + symbol

print (pathVar + symbol)

page = requests.get(url1)
print (page.status_code)
# print (page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
