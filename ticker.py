# # Stock ticker
from bs4 import BeautifulSoup
import requests
import json
# import selenium  

# TODO - clean code someday

# GET NSE page 
def callNSE():
    pathVar = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
    symbol = "TATAMOTORS"
    finalURL =  pathVar + symbol
    page = requests.get(finalURL)
    return page;

# # abstract Scraping logic here 
# def scrapeData();
#     return dataDictionary;

respSource = callNSE()
soup = BeautifulSoup(respSource.content, 'html.parser')
divStruct = soup.find("div", {"id": "responseDiv"})
divStructStr = str(divStruct)
jsonStruct = divStructStr.split('<div id="responseDiv" style="display:none">', 2)
jsonStruct1 = str(jsonStruct[1])
jsonstruct2 = jsonStruct1.split('</div>',2)
finalJSON = str(jsonstruct2[0])
newDictionary=json.loads(str(finalJSON))['data']
datadict= newDictionary[0]
print(datadict['symbol'] + '  ' + datadict['lastPrice'] + ' ' + datadict['change'] + ' High:' + datadict['dayHigh'] + ' Low:' + datadict['dayLow'])


