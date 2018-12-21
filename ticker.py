# # Stock ticker
from bs4 import BeautifulSoup
import requests
import json
# import selenium

# TODO - clean code someday

# read file

# GET NSE page

# bashcolors
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

def callNSE(symbol):
    pathVar = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
    page = requests.get(pathVar + symbol)
    return page

# # abstract Scraping logic here


def scrapeData(ReqSource):
    jsonStruct = str(BeautifulSoup(ReqSource.content,'html.parser').find("div", {"id": "responseDiv"})).split(
        '<div id="responseDiv" style="display:none">', 2)
    newDictionary = json.loads(str(str(jsonStruct[1]).split('</div>', 2)[0]))['data']
    if bool(newDictionary) == True:
        respcode = 200
        datadict = newDictionary[0]
    else:
        respcode = 404
        datadict = ""
    return datadict, respcode


# __main__


def main():
    print(
        '------------------------------------------------------------------------------')
    # bashcolors
    # print (bcolors.WARNING + "warning coloured text here" + bcolors.ENDC)
    fmt = '{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}'
    print(fmt.format('symbol','lastPrice','pChange','change','dayHigh','dayLow'))
    with open('C:\\Projects\\ticker\\configStockNames.txt') as stockListFile:
        for line in stockListFile:
            stock = line.rstrip('\n')
            respSource = callNSE(stock)

            # check all data items in this  print 
            # print(respSource)
            
            stockData, nseresp = scrapeData(respSource)

            print(
                '------------------------------------------------------------------------------')

            if nseresp == 200:
                print(fmt.format(stockData['symbol'], stockData['lastPrice'], stockData['pChange'] +
                                 '%', stockData['change'], stockData['dayHigh'], stockData['dayLow']))

            elif nseresp == 404:
                print(stock + ' --> No data found')
            else:
                print('Call unsuccessful')

        print(
            '------------------------------------------------------------------------------')


# invoke main
main()
