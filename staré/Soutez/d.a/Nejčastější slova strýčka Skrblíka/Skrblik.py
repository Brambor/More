import time

nazev=input("Zadejte nazev knihy (bez pripony)\n")
start=time.time()
kniha=open(nazev+".txt","r")
slova2=kniha.read().split(" ")
kniha.close()
dalsi,slova,Slovo=[],[],None
for i in range(len(slova2)):
    a=slova2[i].split("\n")
    for i in range(len(a)):
        dalsi.append(a.pop(0))
    for i in range(len(dalsi)):
        Slovo="".join(dalsi.pop(0)).lower()
        slova.append(Slovo)
DPslova={}

for i in range(len(slova)):
    slovo=slova.pop(0).lower()
    if slovo in DPslova:
        DPslova[slovo]+=1
    else:
        DPslova[slovo]=1
if "" in DPslova:
    DPslova[""]=0

for i in range(3):
    umisteni=0
    for i in DPslova:
        if DPslova[i] > umisteni:
            umisteni=DPslova[i]
    for i in DPslova:
        if umisteni == DPslova[i]:
            print(i+" "+str(DPslova[i]))
            DPslova[i]=0
b=time.time()
input(str(b-start)+" sec")
