lidi={}
def ucastnici():
    global lidi
    a=input()
    while a!="":
        lidi[a]="0 0 0"
        a=input()

def vyber2():
    global lidi
    Hry=10**6
    for i in lidi:
        hry,vyhry,prohry=lidi[i].split()
        hry=int(hry)
        if hry<Hry:
            Hry=hry
            index=i
    hry,vyhry,prohry=lidi[index].split()
    vyhry,prohry=int(vyhry),int(prohry)
    if prohry>0:
        Ratio=vyhry/prohry
    else:
        Ratio=1
    Dif=2
    for i in lidi:
        if i !=index:
            hry,vyhry,prohry=lidi[i].split()
            vyhry,prohry=int(vyhry),int(prohry)
            if prohry>0:
                dif=Ratio-vyhry/prohry
            else:
                dif=Ratio-1
            if dif<0:
                dif=-dif
            if dif<Dif:
                Dif=dif
                index2=i
    return(index,index2)

def vyherce(a,b):
    import random
    return(random.choice([a,b]))
