import time
def slm(sl,dny,mesice,kontrola):
    if kontrola!=0 and dny > sl:
        dny-=sl
        mesice+=1
        return dny
        return mesice
    else:
        kontrola=0
        return kontrola

while True:
    kontrola=True
    sec=int(time.time())
    roky=int(sec/3600/24/365.25)
    dny=sec/3600/24-int(365.25*roky)+1
    hodiny,dny=24*(dny-int(dny))+1,int(dny)
    if hodiny >= 24:
        hodiny,dny=hodiny-24,dny+1
    minuty,hodiny=60*(hodiny-int(hodiny)),int(hodiny)
    sec,minuty=60*(minuty-int(minuty)),int(minuty)
    sec=int(sec)
    m,s=[""]*2
    if minuty < 10:
        m="0"
    if sec < 10:
        s="0"
    if dny > 31:
        dny-=31
        mesice=1
    else:
        kontrola=False
    if (roky+2)%4 == 0 and (roky+370)%400 != 0 and dny > 29 and kontrola==False:
        dny-=29
        mesice+=1
    elif dny > 28 and kontrola==False:
        dny-=28
        mesice+=1
    else:
        kontrola=False
    slm(31,dny,mesice,kontrola)
    slm(30,dny,mesice,kontrola)
    slm(31,dny,mesice,kontrola)
    slm(30,dny,mesice,kontrola)
    slm(31,dny,mesice,kontrola)
    slm(31,dny,mesice,kontrola)
    slm(30,dny,mesice,kontrola)
    slm(31,dny,mesice,kontrola)
    slm(30,dny,mesice,kontrola)
    slm(31,dny,mesice,kontrola)
    print(str(dny)+"/"+str(mesice)+"/"+ str(roky+1970) +"\n"+str(hodiny)+":"+m+str(minuty)+":"+s+str(sec))
    input()
