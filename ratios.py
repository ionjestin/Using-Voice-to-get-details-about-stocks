import datetime as dt
import dateutil.relativedelta as dr
End=dt.date.today()
Start=End-dr.relativedelta(days=2)

import nsepy as nse
def pedate(poi):
    qwe=nse.get_index_pe_history(symbol=poi,start=Start,end=End)
    return qwe.iloc[0][0]
