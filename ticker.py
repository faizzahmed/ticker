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
    finalURL = pathVar + symbol
    page = requests.get(finalURL)
    return page

# # abstract Scraping logic here


def scrapeData(ReqSource):
    soup = BeautifulSoup(ReqSource.content, 'html.parser')
    divStruct = soup.find("div", {"id": "responseDiv"})
    divStructStr = str(divStruct)
    jsonStruct = divStructStr.split(
        '<div id="responseDiv" style="display:none">', 2)
    jsonStruct1 = str(jsonStruct[1])
    jsonstruct2 = jsonStruct1.split('</div>', 2)
    finalJSON = str(jsonstruct2[0])
    newDictionary = json.loads(str(finalJSON))['data']
    if bool(newDictionary) == True:
        respcode = 200
        datadict = newDictionary[0]
    else:
        respcode = 404
        datadict = ''
    return datadict, respcode


# __main__


def main():
    fmt = '{:<15} {:<10} {:<7} {:<7} {:<7} {:<7}'
    print(fmt.format('symbol','lastPrice','pChange','change','dayHigh','dayLow'))
    with open('C:\\Projects\\ticker\\configStockNames.txt') as stockListFile:
        for line in stockListFile:
            stock = line.rstrip('\n')
            respSource = callNSE(stock)

            stockData, nseresp = scrapeData(respSource)

            print(
                '------------------------------------------------------------------------------')

            if nseresp == 200:
                print(fmt.format(stockData['symbol'] , stockData['lastPrice'], stockData['pChange'], stockData['change'],stockData['dayHigh'],stockData['dayLow']))

            elif nseresp == 404:
                print(stock + ' --> No data found')
            else:
                print('Call unsuccessful')

        print(
            '------------------------------------------------------------------------------')


# invoke main
main()
