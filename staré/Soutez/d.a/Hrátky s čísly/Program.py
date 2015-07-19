soubor=open("zadani.txt","r")
zadani=soubor.read().split("\n")
soubor.close()
while len(zadani) > 0:
    a=int(zadani.pop(0))
    print("1/"+str(a)+"="+str(1/a)+"\npředperioda: "+"\nperioda: ")
    
    cislo=list(str(1/a))
