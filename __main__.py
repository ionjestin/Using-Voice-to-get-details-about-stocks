import nsepy as n
def data(sa):
    dl={}
    d=n.get_quote(sa)["data"][0]
    dl[sa.upper()]={
    "High" : float(d['dayHigh'].replace(",","")),
    "Open" : float(d['open'].replace(",","")),
    "Close" : float(d['closePrice'].replace(",","")),
    "Low" : float(d['dayLow'].replace(",","")),
    "Ltp" : float(d['lastPrice'].replace(",","")),
    }
    print(dl[sa.upper()]['Ltp'])
    print(dl)

from time import time, sleep
while True:
    s=input()
    data(s)
#p.pprint((n.get_quote(s)))
