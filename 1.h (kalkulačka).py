if input("Něco napiš, jestli chceš komentář.\n") != "":
    def Print(a):
        print(a)
else:
    def Print(a):
        str()

priklad=input("Zadej příklad.\n")
priklad=list(priklad)
Print(priklad)
for i in range(len(priklad)): #("7"," ","+","5"," ","2")->("7","+","5","2")
    if i<len(priklad):
        while priklad[i]==" ":
            del priklad[i]
Print("bez mezer")
Print(priklad)
for i in range(len(priklad)): #("5","+","5",".","3") -> (5,"+",5,".",3)
    if priklad[i].isdigit():
        priklad[i]=int(priklad[i])
Print("str>int")
Print(priklad)
while True: #(7,"+",5,3,5,".",3) ->(7,"+",53,5,".",3)
    a=len(priklad)
    for i in range(len(priklad)):
        if i+1 < len(priklad):
            if type(priklad[i])==type(1) and type(priklad[i+1])==type(1):
                priklad[i]=int(str(priklad[i])+str(priklad[i+1]))
                del priklad[i+1]
                break
    if len(priklad)==a:
        break
Print("spojení čísel")
Print(priklad)
while True: # udělá float
    a=len(priklad)
    for i in range(len(priklad)):
        if i+2 < len(priklad):
            if type(priklad[i])==type(1) and priklad[i+1]=="." and type(priklad[i+2])==type(1):
                priklad[i]=float(str(priklad[i])+"."+str(priklad[i+2]))
                del priklad[i+1]
                del priklad[i+1]
                break
    if len(priklad)==a:
        break
Print("spojení float")
Print(priklad)
Print("")

c=0
if "(" in priklad:
        c=priklad.count("(")
        for i in range(c):
            priklad[priklad.index("(")]=str(c-i)
        for i in range(c):
            priklad[priklad.index(")")]=str(i+1)
Print(priklad)

def vypocet(priklad,c):
#    Print(priklad)
    if c>0:
        u1=priklad.index(str(c))
        del priklad[priklad.index(str(c))]
        u2=priklad.index(str(c))+2
        del priklad[priklad.index(str(c))]
        pzbytek=[]
        zzbytek=[]
        zbytek=[]
        for i in range(len(priklad)):
            if i < u1:
                pzbytek.append(priklad[i])
            elif i < u2-2:
                zbytek.append(priklad[i])
            else:
                zzbytek.append(priklad[i])
        c-=1
        zbytek=vypocet(zbytek,c)
        priklad=[]
        for i in pzbytek:
            priklad.append(i)
        for i in zbytek:
            priklad.append(i)
        for i in zzbytek:
            priklad.append(i)
    if "^" in priklad:
        p=priklad.count("^")
        for i in range(p):
            u=priklad.index("^")
            priklad[u-1]**=priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "/" in priklad:
        p=priklad.count("/")
        for i in range(p):
            u=priklad.index("/")
            priklad[u-1]/=priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "*" in priklad:
        p=priklad.count("*")
        for i in range(p):
            u=priklad.index("*")
            priklad[u-1]*=priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "-" in priklad:
        p=priklad.count("-")
        for i in range(p):
            u=priklad.index("-")
            priklad[u-1]-=priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "+" in priklad:
        p=priklad.count("+")
        for i in range(p):
            u=priklad.index("+")
            priklad[u-1]+=priklad[u+1]
            del priklad[u]
            del priklad[u]
    return(priklad)

priklad=vypocet(priklad,c)
print(priklad[0])
#(22*51+(60   - 25)/6.5)^6
