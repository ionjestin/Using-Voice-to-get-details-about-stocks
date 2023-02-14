

import pandas as p


def kuli(a):
    if a=='AUTO':
        df=p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyautolist.csv")
        n=df.count()["Symbol"]
        c=df['Symbol']+'.NS'
        return [c,n]
    elif a=="BANK":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftybanklist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="CONSUMER DURABLES":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyconsumerdurableslist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="FINANCIAL SERVICES":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyfinancelist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="FMCG":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyfmcglist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="HEALTH CARE":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyhealthcarelist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="MEDIA":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftymedialist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="OIL AND GAS":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyoilgaslist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="PRIVATE BANK":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyprivatebanklist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="PSU BANK":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftypsubanklist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="REALTY":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyrealtylist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="METAL":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftymetallist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="PHARMA":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftypharmalist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="IT":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyitlist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="INFRA":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyinfralist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]
    elif a=="ENERGY":
        df = p.read_csv("C:/Users/ion/PycharmProjects/python/nifty indecis/ind_niftyenergylist.csv")
        n = df.count()["Symbol"]
        c = df['Symbol'] + '.NS'
        return [c, n]



