from tkinter import *
from ticker import scrapense

def showlabel(rownumber,stockstring):
        Label(window, text=stockstring, bg="black",
          fg="green", justify=LEFT).grid(row=rownumber, column=0,sticky=W)

if __name__ == "__main__":
    # create window
    window = Tk()
    window.title("NSE stock ticker")
    window.configure(background="black")

    fmt = '{:<15}''| '' {:<10}''| '' {:<10}''| '' {:<10}''| '' {:<10}''| '' {:<10}'
    dashes = '------------------------------------------------------------------------------'
    stockstring = fmt.format('symbol', 'lastPrice','pChange ', 'change', 'dayHigh', 'dayLow')

    showlabel(0,dashes)
    showlabel(1,stockstring)

    stock = 'WELENT'
    stockData, nseresp = scrapense(stock)

    stockstring = dashes
    showlabel(2,stockstring)

    if nseresp == 200:
        stockstring = fmt.format(stockData['symbol'], stockData['lastPrice'], (stockData['pChange'] +
                                                                               '%'), stockData['change'], stockData['dayHigh'], stockData['dayLow'])

    elif nseresp == 404:
        stockstring = stock + ' --> No data found'
    else:
        stockstring = 'Call unsuccessful'

    showlabel(3,stockstring)

    window.mainloop()
