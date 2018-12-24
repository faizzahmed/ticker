# ______________________________________________________________________________________________________
#                               Stock Ticker Tkinter GUI
# WIP - use ticker script to expose same data via tkinter GUI  
# ______________________________________________________________________________________________________
from tkinter import *
from ticker import scrapense
from ticker import readfile

# ______________________________________________________________________________________________________
# CONFIGRATIONS
# ______________________________________________________________________________________________________
ICOFILE = 'C:\\Projects\\ticker\\ticker.ico'
#  _____________________________________________________________________________________________________
# CONFIGRATIONS
# ______________________________________________________________________________________________________


def showlabel(rownumber,columnnumber,value):
    
    dispcolor = "black"
    backgroundcolor = "white"

    # heading is blue
    if (rownumber == 0) :
        backgroundcolor = "blue"
    else:
    #   stock name is blue 
        if columnnumber == 0:
            backgroundcolor = "blue"
    #   change is red or green
        elif (columnnumber == 2) or (columnnumber == 3):
            if value[0] == '-':
                dispcolor = 'red'
            else:
                dispcolor = 'green'
        else:
            backgroundcolor = "white"

    Label(window, text=value,relief=RIDGE,bg=backgroundcolor,fg=dispcolor,width=15).grid(row=rownumber, column=columnnumber)

def getstockdata():
    # get stock data from ticker.py
    stockcounter=1
    stocklist = readfile()
    for stock in stocklist:
        stockData, nseresp = scrapense(stock)

        if nseresp == 200:
            stockdatalist = [stockData['symbol'],stockData['lastPrice'],(stockData['pChange']+'%'),stockData['change'],stockData['dayHigh'],stockData['dayLow']]
        elif nseresp == 404:
            stockdatalist = [stock + ' --> No data found']
        else:
            stockdatalist = ['Call unsuccessful']

        counter = 0
        for stockdatalistelement in stockdatalist:
            showlabel(stockcounter,counter,stockdatalistelement)
            counter+=1

        stockcounter+=1
    return stockcounter

if __name__ == "__main__":
    # create window
    window = Tk()
    window.title("NSE stock ticker")
    window.configure()

    # create heading
    heading = ['symbol','lastPrice','pChange ','change','dayHigh','dayLow']
    counter = 0
    for Iheading in heading:
        showlabel(0,counter,Iheading)
        counter+=1

    stockcounter = getstockdata()

    # refresh button
    refreshbutton = Button(window,text="Refresh",width=15,command=getstockdata)
    refreshbutton.grid(row=stockcounter)

    window.iconbitmap(ICOFILE)
    window.mainloop()
