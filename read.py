f4=open('Data3.txt','r', encoding="utf8")
lines=f4.readlines()
f4.close()
Lvoiture=[]
Lvelo=[]

for do in lines:
    L=do.split('   ')
    x=float(L[1].strip('%'))
    y=float(L[2].strip('%\n'))
    Lvoiture.append(x)
    Lvelo.append(y)
print(Lvoiture,Lvelo)
    

