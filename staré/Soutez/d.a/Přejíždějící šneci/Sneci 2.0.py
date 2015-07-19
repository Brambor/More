while True:
    breakit=False
    soubor=open("sneci.txt","r")
    radky=soubor.read().split("\n")
    cas=radky.pop(0)
    if cas.isdigit():
        cas=int(cas)
    else:
        input("Zadal jsi špatný input.")
        break
    Sneci={}
    for i in range(len(radky)):
        Sneci[str(i+1)]=radky.pop(0)
    Vysledky={}
    for i in range(len(Sneci)):
        priklad=Sneci[str(i+1)]
        naskok,rychlost=priklad.split(" ")
        if naskok.isdigit() and rychlost.isdigit():
            naskok,rychlost=int(naskok),int(rychlost)
        else:
            input("Zadal jsi špatný input.")
            breakit=True
            break
        vzdalenost=rychlost*cas+naskok
        Vysledky[str(i+1)]=vzdalenost
    if breakit==True:
        break
    Kvysledky=Vysledky
    umisteni=0
    while len(Kvysledky) > 0:
        vzdalenosti=0
        for i in Kvysledky:
            if vzdalenosti < Kvysledky[i]:
                vzdalenosti=Kvysledky[i]
        vyherci=0
        for i in Kvysledky:
            if Kvysledky[i]==vzdalenosti:
                vyherci+=1
            vyhodnoceni=[]
            for i in Kvysledky:
                if Kvysledky[i]==vzdalenosti:
                    vyhodnoceni.append(i)
        for i in range(len(vyhodnoceni)):
            vyhodnocen=vyhodnoceni[i]
            ujel=str(Kvysledky[vyhodnocen])
            Kvysledky.pop(vyhodnocen)
        if vyherci > 1:
            umisteni+=1
            umisteni1=umisteni
            umisteni2=umisteni+vyherci-1
            umisteni=umisteni2
            snekove=" a ".join(vyhodnoceni)
            print(str(umisteni1)+".-"+str(umisteni2)+". místo šneci číslo "+snekove+" ("+ujel+"mm)")
        else:
            umisteni+=1
            print(str(umisteni)+". místo šnek číslo "+vyhodnocen+" ("+ujel+"mm)")
    input()
    break
