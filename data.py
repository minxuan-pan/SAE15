import requests
from lxml import etree
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT','FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_SABL','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']
Toville=0 #Total parkings of the city
FrVille=0 #Total free parkings of the city
for x in parkings:
    data=requests.get(f"https://data.montpellier3m.fr/sites/default/files/ressources/{x}.xml")
    f1=open(f"{x}.txt","w",encoding='utf8')
    f1.write(data.text)
    f1.close()
    tree=etree.parse(f"{x}.txt")
    for user in tree.xpath("Name"):
        nom=user.text
    for user in tree.xpath("Total"):
        total=user.text
        a=int(total)
    for user in tree.xpath("Free"):
        libre=user.text
        b=int(libre)
    pourcentage=b/a
    f2=open("placelibre.txt","a",encoding='utf8')
    f2.write(f"Name:{nom} Total:{total} Free:{libre} Percentage:{pourcentage*100}%")
    f2.write("\n")
    f2.close()
    Toville=Toville+a
    FrVille=FrVille+b
f2=open("placelibre.txt","a",encoding='utf8')
f2.write(f"Percentage of the city:{FrVille/Toville}")
f2.close()