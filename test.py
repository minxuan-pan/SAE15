import requests
from lxml import etree
ToVelo=0
FrVelo=0
data2=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
f3=open("VELO.txt","w",encoding='utf8')
f3.write(data2.text)
f3.close()
tree2=etree.parse("VELO.txt")
for user in tree2.xpath('//si/@fr'):
    free=int(user)
    FrVelo=FrVelo+free
for user in tree2.xpath('//si/@to'):
    total=int(user)
    ToVelo=ToVelo+total
PourcentVelo=FrVelo/ToVelo


