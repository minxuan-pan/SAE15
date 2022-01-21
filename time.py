import requests
from lxml import etree
import time
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
Toville=0 #Total parkings of the city
FrVille=0 #Total free parkings of the city
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
        for user in tree.xpath("Total"):
            total=user.text
            a=int(total)
        for user in tree.xpath("Free"):
            libre=user.text
            b=int(libre)
        Toville=Toville+a
        FrVille=FrVille+b
    Percentage=FrVille/Toville
    temps=time.time()
    temps=time.ctime(temps)
    Nom=temps.replace(':','')
    print(Nom)
    f2=open(f"{Nom}.txt","w",encoding='utf8')
    f2.write(f"The percentage of Free parkings of the whole city:{Percentage*100}%")
    f2.close()
    time.sleep(duration)