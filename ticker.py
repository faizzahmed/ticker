# ______________________________________________________________________________________________________
#                                      Stock ticker
# shell script to display realtime stock data
# $ python ticker.py
# ______________________________________________________________________________________________________
from bs4 import BeautifulSoup
import requests
import json
import config
from operator import itemgetter
from tabulate import tabulate

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

        # trim the data
        newtrimdict = {}
        for dataitem in config.DATAITEMLIST:
            if dataitem == 'pChange':
                newtrimdict.update({dataitem: datadict[dataitem]+'%'})
            else:
                newtrimdict.update({dataitem: datadict[dataitem]})
    else:
        respcode = 404
        newtrimdict = {}
    return newtrimdict, respcode

def scrapense(symbol):
    respSource = callNSE(symbol)
    stockData, nseresp = scrapeData(respSource)
    return stockData, nseresp

# __main__


def main():
    stocklist = readfile(filepath=None)

    # print(config.dashes)
    # bashcolors
    # print (bcolors.WARNING + "warning coloured text here" + bcolors.ENDC)
    firstprint = 0
    for stock in stocklist:
        stockData, nseresp = scrapense(stock)

        # print(config.dashes)

        if nseresp == 200:

            if firstprint == 0: 
                firstprint = 1
                completelist = []
                completelist.append(list(stockData.keys()))

            completelist.append(list(stockData.values()))

        elif nseresp == 404:
            print(stock + ' --> No data found') 
        else:
            print('Call unsuccessful')
    print (tabulate(completelist))

# invoke main
if __name__ == "__main__":
    main()
