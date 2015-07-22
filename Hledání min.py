import random

#Vlastní hra
for p in range(1):
    while True:
        x=input("Zvolte šířku.\n")
        if x.isdigit():
            x=int(x)
            if x > 0:
                break
            else:
                print("Šířka musí být větší, než 0.")
        else:
            print("Šířka musí být vyjádřena celým číslem.")
    while True:
        y=input("Zvolte výšku.\n")
        if y.isdigit():
            y=int(y)
            if y > 0:
                break
            else:
                print("Výška musí být větší, než 0.")
        else:
            print("Výška musí být vyjádřena celým číslem.")
    while True:
        miny=input("Zvolte počet min.\n")
        if miny.isdigit():
            miny=int(miny)
            if miny > 0 and miny < (x*y):
                break
            elif miny < 0:
                print("Počet min musí být větší, než 0.")
            else:
                print("Tolik min se do pole ("+str(x)+" x "+str(y)+") nevejde.")
        else:
            print("Počet min musí být vyjádřen celým číslem.")
#Systém
for p in range(1):
    pole=[["#"] * x for i in range(y)]
    cisla=[]
    for q in range(x*y):
        cisla.append(q)
    for i in range(miny):
        minaY=random.choice(cisla)
        cisla.remove(minaY)
        minaX=0
        while minaY > x:
            minaY-=x
            minaX+=1
        minaY-=1
        pole[minaX][minaY] = "M"
#Zobrazení
for p in range(1):
    pole_hra=[]
    for i in range(y):
        pole_hra.append("".join(pole[i]))
    pole_replace=0
    for i in pole_hra:
        pole_hra[pole_replace]=i.replace("M","#")
        pole_replace+=1
#Hra
for p in range(1):
    print("\n".join(pole_hra))
