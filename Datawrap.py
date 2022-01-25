import requests
from lxml import etree
import time
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
Toville=0 #Total parkings of the city
FrVille=0 #Total free parkings of the city
ToVelo=0
AvVelo=0
period=int(input("Période(min):"))
period=period*60
duration=int(input("duration(sec):"))
t=int(period/duration)
for p in range(t):
    for x in parkings:
        data=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{x}.xml")
        f1=open(f"{x}.txt","w",encoding='utf8')
        f1.write(data.text)
        f1.close()
        tree=etree.parse(f"{x}.txt")
        a=0
        b=0
        for user in tree.xpath("Total"):
            total=int(user.text)
            a=a+total
        for user in tree.xpath("Free"):
            libre=int(user.text)
            b=b+libre
        Toville=Toville+a
        FrVille=FrVille+b
    data2=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
    f3=open("VELO.txt","w",encoding='utf8')
    f3.write(data2.text)
    f3.close()
    tree2=etree.parse("VELO.txt")
    for user in tree2.xpath('//si/@av'):
        av=int(user)
        AvVelo=AvVelo+av
    for user in tree2.xpath('//si/@to'):
        to=int(user)
        ToVelo=ToVelo+to
    PourcentVelo=AvVelo/ToVelo
    PercentVoiture=FrVille/Toville
    PercentVoiture=1-PercentVoiture
    temps=time.time()
    temps=time.ctime(temps)
    t=temps.split(' ')
    f2=open("Data.txt","a",encoding='utf8')
    f2.write(f"{t[3]}    {round(PercentVoiture*100, 2)}%    {round(PourcentVelo*100, 2)}%")
    f2.write('\n')
    f2.close()
    time.sleep(duration)