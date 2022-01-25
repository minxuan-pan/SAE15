import requests
from lxml import etree
data2=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
f3=open("test1.txt","w",encoding='utf8')
f3.write(data2.text)
f3.close()
tree2=etree.parse("test1.txt")
for user in tree2.xpath('//si/@na'):
    for x in tree2.xpath(f'//si[@na="{user}"]/@av'):
        print(user)
        print('places occupees:',x)
    for y in tree2.xpath(f'//si[@na="{user}"]/@fr'):
        print('nombre de place libre :', y)
    for v in tree2.xpath(f'//si[@na="{user}"]/@to'):
        print('nombre total de place:', v)