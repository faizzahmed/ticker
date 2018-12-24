from tkinter import *
from ticker import scrapense
from ticker import readfile

# ______________________________________________________________________________________________________
# CONFIGRATIONS
# ______________________________________________________________________________________________________
CONFIGFILE = 'C:\\Projects\\ticker\\configStockNames.txt'
NSEURL = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="
fmt = '{:<20} {:<10} {:<10} {:<10} {:<10} {:<10}'  # globalformat
dashes = '------------------------------------------------------------------------------'
#  _____________________________________________________________________________________________________
# CONFIGRATIONS
# ______________________________________________________________________________________________________


def showlabel(rownumber, stockstring):
    Label(window, text=stockstring, bg="black",
          fg="green", justify=LEFT).grid(row=rownumber, column=0, sticky=W)


if __name__ == "__main__":
    # create window
    window = Tk()
    window.title("NSE stock ticker")
    window.configure(background="black")
    stockstring = fmt.format('symbol', 'lastPrice',
                             'pChange ', 'change', 'dayHigh', 'dayLow')

    i = 0
    showlabel(i, dashes)
    i += 1
    showlabel(i, stockstring)
    i += 1

    stocklist = readfile()
    for stock in stocklist:
        stockData, nseresp = scrapense(stock)
        showlabel(i, dashes)
        i += 1

        if nseresp == 200:
            stockstring = fmt.format(stockData['symbol'], stockData['lastPrice'], (stockData['pChange'] +
                                                                                   '%'), stockData['change'], stockData['dayHigh'], stockData['dayLow'])

        elif nseresp == 404:
            stockstring = stock + ' --> No data found'
        else:
            stockstring = 'Call unsuccessful'

        showlabel(i, stockstring)
        i += 1

    window.mainloop()
