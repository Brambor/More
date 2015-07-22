import time

Dcas,Hcas=input("Čas:\n").split(" ")
Ddrevo,Dhlina,Dzelezo=input("Doly:\n").split("\n")
drevo,hlina,zelezo=input("Suroviny:\n").split(" ")
dny,mesice,roky=Dcas.split(".")
hodiny,minuty,sekundy=Hcas.split(":")
roky,mesice,dny,hodiny,minuty,sekundy=int(roky)+30,int(mesice),int(dny),int(hodiny),int(minuty),int(sekundy)
for i in range(mesice):
    if mesice==1 or mesice==3 or mesice==5 or mesice==7 or mesice==8 or mesice==10 or mesice==12:
        dny+=31
    if mesice==4 or mesice==6 or mesice==9 or mesice==11:
        dny+=30
    if mesice==2 and (roky+2)%4==0:
        dny+=29
    elif mesice==2:
        dny+=28
dny+=int(roky*0.25)
sekundy+=((((roky*365+dny)*24+hodiny)*60)+minuty)*60
cas=time.time()-sekundy
print(cas)
