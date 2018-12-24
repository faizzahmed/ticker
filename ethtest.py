import webbrowser
from tkinter import *
from bs4 import BeautifulSoup
import json
import requests
import time


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def EthLink(self):
        webbrowser.open("https://coinmarketcap.com/currencies/ethereum/")

    def initUI(self):
        self.parent.title("simple")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="Quit", fg='red', command=self.quit)
        quitButton.place(x=10, y=100)
        EthLink = Button(self, text="ETH Price Chart", command=self.EthLink)
        EthLink.place(x=10, y=50)
        EthPrice = Label(self, text=self.GetPrice, fg='dark green')
        EthPrice.pack()

    def GetPrice(self):
        RetTicker = requests.get(
            'https://poloniex.com/public?command=returnTicker').text
        RetTicker = json.loads(RetTicker)
        price = str(RetTicker['USDT_ETH']['last'])
        return price


def main():
    root = Tk()
    root.geometry('250x150+300+300')
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
