# ______________________________________________________________________________________________________
#                               Stock Ticker Tkinter GUI
# WIP - use ticker script to expose same data via tkinter GUI  
# ______________________________________________________________________________________________________
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from ticker import scrapense
from ticker import readfile
import config


def showlabel(rownumber,columnnumber,value):
    
    dispcolor = "black"
    backgroundcolor = "white"

    # heading is blue
    if (rownumber == 0) :
        backgroundcolor = "blue"
    else:
    #   stock name is white 
        if columnnumber == 0:
            backgroundcolor = "white"
    #   change is red or green
        elif (columnnumber == 2) or (columnnumber == 3):
            if value[0] == '-':
                dispcolor = 'red'
            else:
                dispcolor = 'green'
        else:
            backgroundcolor = "white"

    Label(window, text=value,relief=RIDGE,bg=backgroundcolor,fg=dispcolor,width=15).grid(row=rownumber, column=columnnumber)

def getstockdata(filepath=None):
    # get stock data from ticker.py
    stockcounter=1
    stocklist = readfile(filepath)
    for stock in stocklist:
        stockData, nseresp = scrapense(stock)

        if nseresp == 200:
            stockdatalist = [stockData['symbol'],stockData['lastPrice'],(stockData['pChange']+'%'),stockData['change'],stockData['dayHigh'],stockData['dayLow']]
        elif nseresp == 404:
            stockdatalist = [stock,'No data']
        else:
            stockdatalist = [stock,'Call unsuccessful']

        counter = 0
        for stockdatalistelement in stockdatalist:
            showlabel(stockcounter,counter,stockdatalistelement)
            counter+=1

        stockcounter+=1
    return stockcounter

def loadfile():
        fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("All files", "*.*") ))
        return fname


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

    # browse file button
    browsebutton = Button(window,text="Browse file",width=15,command=loadfile)
    browsebutton.grid(row=stockcounter, column=1)

    # refresh button
    refreshbutton = Button(window,text="Refresh",width=15,command=getstockdata)
    refreshbutton.grid(row=stockcounter)

    window.iconbitmap(config.ICOFILE)
    window.mainloop()
