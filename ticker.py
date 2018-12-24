# ______________________________________________________________________________________________________
#                                      Stock ticker
# ______________________________________________________________________________________________________
from bs4 import BeautifulSoup
import requests
import json
# ______________________________________________________________________________________________________
# CONFIGRATIONS
# ______________________________________________________________________________________________________
CONFIGFILE = 'C:\\Projects\\ticker\\configStockNames.txt'
NSEURL = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
fmt = '{:<15} {:<10} {:<10} {:<10} {:<10} {:<10}'  # globalformat
dashes = '------------------------------------------------------------------------------'
#  _____________________________________________________________________________________________________
# CONFIGRATIONS
# ______________________________________________________________________________________________________

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


def readfile():
    stocklist = open(CONFIGFILE).read().splitlines()
    return stocklist


def callNSE(symbol):
    page = requests.get(NSEURL + symbol)
    return page

# # abstract Scraping logic here


def scrapeData(ReqSource):
    jsonStruct = str(BeautifulSoup(ReqSource.content, 'html.parser').find("div", {"id": "responseDiv"})).split(
        '<div id="responseDiv" style="display:none">', 2)
    newDictionary = json.loads(
        str(str(jsonStruct[1]).split('</div>', 2)[0]))['data']
    # check all data items in this  print
    # print(datadict)
    if bool(newDictionary) == True:
        respcode = 200
        datadict = newDictionary[0]
    else:
        respcode = 404
        datadict = ""
    return datadict, respcode


def scrapense(symbol):
    respSource = callNSE(symbol)
    stockData, nseresp = scrapeData(respSource)
    return stockData, nseresp


# __main__


def main():
    stocklist = readfile()

    print(dashes)
    # bashcolors
    # print (bcolors.WARNING + "warning coloured text here" + bcolors.ENDC)
    print(fmt.format('symbol', 'lastPrice',
                     'pChange', 'change', 'dayHigh', 'dayLow'))
    for stock in stocklist:
        stockData, nseresp = scrapense(stock)

        print(dashes)

        if nseresp == 200:
            print(fmt.format(stockData['symbol'], stockData['lastPrice'], stockData['pChange'] +
                             '%', stockData['change'], stockData['dayHigh'], stockData['dayLow']))

        elif nseresp == 404:
            print(stock + ' --> No data found')
        else:
            print('Call unsuccessful')

    print(dashes)


# invoke main
if __name__ == "__main__":
    main()
