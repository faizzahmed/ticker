# ______________________________________________________________________________________________________
#                                      Stock ticker
# shell script to display realtime stock data 
# $ python ticker.py 
# ______________________________________________________________________________________________________
from bs4 import BeautifulSoup
import requests
import json
import config

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


def readfile(filepath=None):
    if filepath is None:
        filepath = config.CONFIGFILE
    stocklist = open(filepath).read().splitlines()
    return stocklist


def callNSE(symbol):
    page = requests.get(config.NSEURL + symbol)
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
    stocklist = readfile(filepath=None)

    print(config.dashes)
    # bashcolors
    # print (bcolors.WARNING + "warning coloured text here" + bcolors.ENDC)
    print(config.fmt.format('symbol', 'lastPrice',
                     'pChange', 'change', 'dayHigh', 'dayLow'))
    for stock in stocklist:
        stockData, nseresp = scrapense(stock)

        print(config.dashes)

        if nseresp == 200:
            print(config.fmt.format(stockData['symbol'], stockData['lastPrice'], stockData['pChange'] +
                             '%', stockData['change'], stockData['dayHigh'], stockData['dayLow']))

        elif nseresp == 404:
            print(stock + ' --> No data found')
        else:
            print('Call unsuccessful')

    print(config.dashes)


# invoke main
if __name__ == "__main__":
    main()
