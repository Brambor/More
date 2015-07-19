soubor=open("cas.txt","r")
radek1,radek2=soubor.read().split("\n")
Tonda,cas=radek1.split(" ")
hodiny,minuty,sekundy=cas.split(":")
Janek,Jcas=radek2.split(" ")
Jhodiny,Jminuty,Jsekundy=Jcas.split(":")
Inhodiny,Inminuty,Insekundy,Mminuty=input("hodiny: "),input("minuty: "),input("sekundy: "),input()
if Inhodiny == "":
    Inhodiny=0
if Inminuty == "":
    Inminuty=0
if Insekundy == "":
    Insekundy=0
if Mminuty == "":
    Mminuty=0
sekundy,minuty,hodiny,Insekundy,Inminuty,Inhodiny,Jsekundy,Jminuty,Jhodiny,Mminuty=int(sekundy),int(minuty),int(hodiny),int(Insekundy),int(Inminuty),int(Inhodiny),int(Jsekundy),int(Jminuty),int(Jhodiny),int(Mminuty)
Insekundy=2/3*(3600*Inhodiny+60*Inminuty+Insekundy)
sekundy+=3600*hodiny+60*minuty+Insekundy-60*Mminuty
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
sekundy,minuty,hodiny,Jsekundy,Jminuty,Jhodiny=str(sekundy),str(minuty),str(hodiny),str(Jsekundy),str(Jminuty),str(Jhodiny)
print("Tonda "+h+hodiny+":"+m+minuty+":"+s+sekundy)
print("Janek "+Jh+Jhodiny+":"+Jm+Jminuty+":"+Js+Jsekundy)
soubor.close()
soubor=open("cas.txt","w")
soubor.write(Tonda+" "+h+hodiny+":"+m+minuty+":"+s+sekundy+"\n"+Janek+" "+Jh+Jhodiny+":"+Jm+Jminuty+":"+Js+Jsekundy)
soubor.close()
input()
