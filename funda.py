import pandas as pd
import yahoo_fin.stock_info as si
from ns import kuli
from ratios import pedate
import speech_recognition as sr

r= sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    audio=r.listen(source)

    try:
        ip=r.recognize_google(audio)
        print("You said : {}".format(ip))
    except:
        print("Sorry bro")
print("Specify sector from the following \n1.AUTO\n"
         "2.BANK\n3.CONSUMER DURABLES\n4.FINANCIAL SERVICES\n5.FMCG\n6.HEALTH CARE\n"
         "7.IT\n8.MEDIA\n9.METAL\n10.OIL AND GAS\n11.PHARMA\n12.PRIVATE BANK\n13.PSU BANK\n14.REALTY\n15.INFRA\n16.ENERGY\n ")
c=kuli(ip.upper())
sd='NIFTY '+ip.upper()
peda=pedate(sd)
print(peda)
df=pd.DataFrame(columns=['Name','Beta (5Y Monthly)','PE Ratio (TTM)','EPS (TTM)'])
t=c[0]
n=c[1]
for i in range(0,n):
    x=t[i]
    # print(x)
    v=si.get_quote_table(x)
    be=v['Beta (5Y Monthly)']
    pe=v['PE Ratio (TTM)']
    eps=v['EPS (TTM)']
    df=df.append({'Name':x,'Beta (5Y Monthly)':be,'PE Ratio (TTM)':pe,'EPS (TTM)':eps},ignore_index=True)
print(df)
print("Now for the filtering with beta < 1 and eps > 5")
for i in range(0,n):
    jhg=0
    if df.iloc[i][1]<1 and df.iloc[i][3]>5 and df.iloc[i][2] < peda:
        jhg=1
    if jhg==1:
        print(df.iloc[i])