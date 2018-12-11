# # Stock ticker
from bs4 import BeautifulSoup
import requests
import json
# import selenium  

# TODO - clean code someday

# read file 

# GET NSE page 
def callNSE(symbol):
    pathVar = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
    finalURL =  pathVar + symbol
    page = requests.get(finalURL)
    return page;

# # abstract Scraping logic here 
def scrapeData(ReqSource):
    soup = BeautifulSoup(ReqSource.content, 'html.parser')
    divStruct = soup.find("div", {"id": "responseDiv"})
    divStructStr = str(divStruct)
    jsonStruct = divStructStr.split('<div id="responseDiv" style="display:none">', 2)
    jsonStruct1 = str(jsonStruct[1])
    jsonstruct2 = jsonStruct1.split('</div>',2)
    finalJSON = str(jsonstruct2[0])
    newDictionary=json.loads(str(finalJSON))['data']
    datadict= newDictionary[0]
    return datadict;

# __main__
def main():   
    stockListFile = open ( 'C:\\Projects\\ticker\\configStockNames.txt', 'r' )
    for line in stockListFile: 
        stock = line.rstrip('\n')
        respSource = callNSE(stock)
        stockData = scrapeData(respSource)
        print('------------------------------------------------------------------------------')
        print(stockData['symbol'] + '  ' + stockData['lastPrice'] +  '  ' + stockData['pChange']+'%'  + '  ' + stockData['change'] + ' High:' + stockData['dayHigh'] + ' Low:' + stockData['dayLow'])

    print('------------------------------------------------------------------------------')
     
# invoke main
main()