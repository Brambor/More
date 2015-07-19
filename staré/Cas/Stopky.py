import time
soubor=open("cas.txt","r")
radek1,radek2=soubor.read().split("\n")
Tonda,cas=radek1.split(" ")
hodiny,minuty,sekundy=cas.split(":")
Janek,Jcas=radek2.split(" ")
Jhodiny,Jminuty,Jsekundy=Jcas.split(":")
input("Start?")
start=time.time()
input("Running...")
stop=time.time()-start
Shodiny,Ssekundy=int(2/3*stop/3600),int(2/3*stop)
Ssekundy=Ssekundy-(3600*Shodiny)
Sminuty=int(Ssekundy/60)
Ssekundy=Ssekundy-60*Sminuty
if Shodiny > 0:
    print(str(Shodiny)+" h")
if Sminuty > 0:
    print(str(Sminuty)+" min")
if Ssekundy > 0:
    print(str(Ssekundy)+" sec")
sekundy,minuty,hodiny,Jsekundy,Jminuty,Jhodiny=int(sekundy),int(minuty),int(hodiny),int(Jsekundy),int(Jminuty),int(Jhodiny)
sekundy+=3600*hodiny+60*minuty+2/3*stop
Jsekundy+=3600*Jhodiny+60*Jminuty
if Jsekundy>sekundy:
    Jsekundy,sekundy=Jsekundy-sekundy,0
else:
    sekundy,Jsekundy=sekundy-Jsekundy,0
Jhodiny=int(Jsekundy/3600)
Jsekundy=Jsekundy-(3600*Jhodiny)
Jminuty=int(Jsekundy/60)
Jsekundy=int(Jsekundy-60*Jminuty)
Js,Jm,Jh=[""]*3
if Jhodiny<10:
    Jh="0"
if Jminuty<10:
    Jm="0"
if Jsekundy<10:
    Js="0"
hodiny=int(sekundy/3600)
sekundy=sekundy-(3600*hodiny)
minuty=int(sekundy/60)
sekundy=int(sekundy-60*minuty)
s,m,h=[""]*3
if hodiny<10:
    h="0"
if minuty<10:
    m="0"
if sekundy<10:
    s="0"
print("Tonda "+h+str(hodiny)+":"+m+str(minuty)+":"+s+str(sekundy)+"\nJanek "+Jh+str(Jhodiny)+":"+Jm+str(Jminuty)+":"+Js+str(Jsekundy))
soubor.close()
soubor=open("cas.txt","w")
soubor.write("Tonda "+h+str(hodiny)+":"+m+str(minuty)+":"+s+str(sekundy)+"\nJanek "+Jh+str(Jhodiny)+":"+Jm+str(Jminuty)+":"+Js+str(Jsekundy))
soubor.close()
input()
