if input("Něco napiš, jestli chceš komentář.\n") != "":
    def Print(a = ""):
        print(a)
else:
    def Print(a = ""):
        pass

priklad = input("Zadej příklad.\n")
priklad = list(priklad)
Print(priklad)

while " " in priklad:
    del priklad[priklad.index(" ")]
Print("\nbez mezer")
Print(priklad)

for i in range(len(priklad)): #("5","+","5",".","3") -> (5,"+",5,".",3)
    if priklad[i].isdigit():
        priklad[i] = int(priklad[i])
Print("\nstr->int")
Print(priklad)

Len = len(priklad)
i = 0
while i+1 < Len: #(7,"+",5,3,5,".",3) ->(7,"+",53,5,".",3)
    while i+1 < Len and (type(priklad[i]) == type(0) == type(priklad[i+1])):
        priklad[i] = int(str(priklad[i]) + str(priklad[i+1]))
        del priklad[i+1]
        Len -= 1
    i += 1
Print("\nspojení čísel")
Print(priklad)

Len = len(priklad)
i = 0
while i+3 < Len: # udělá float
    if type(priklad[i]) == type(0) and priklad[i+1] in [".", ","] and type(priklad[i+2]) == type(0):
        priklad[i] = float(str(priklad[i]) + "." + str(priklad[i+2]))
        del priklad[i+1]
        del priklad[i+1]
    i += 1
Print("\nspojení float")
Print(priklad)
Print()

c = 0
if "(" in priklad:
        c = priklad.count("(")
        for i in range(c):
            priklad[priklad.index("(")] = str(c-i)
            priklad[priklad.index(")")] = str(i+1)
Print(priklad)

def vypocet(priklad, c):
#    Print(priklad)
    if c > 0:
        u1 = priklad.index(str(c))
        del priklad[u1]
        u2 = priklad.index(str(c)) + 2
        del priklad[u2 - 2]
        pzbytek, zzbytek, zbytek = [], [], []
        for i in range(len(priklad)):
            if i < u1:
                pzbytek.append(priklad[i])
            elif i < u2-2:
                zbytek.append(priklad[i])
            else:
                zzbytek.append(priklad[i])
        c -= 1
        zbytek = vypocet(zbytek, c)
        priklad = []
        priklad.extend(pzbytek)
        priklad.extend(zbytek)
        priklad.extend(zzbytek)
    if "^" in priklad:
        p = priklad.count("^")
        for i in range(p):
            u = priklad.index("^")
            priklad[u-1] **= priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "/" in priklad:
        p = priklad.count("/")
        for i in range(p):
            u = priklad.index("/")
            priklad[u-1] /= priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "*" in priklad:
        p = priklad.count("*")
        for i in range(p):
            u = priklad.index("*")
            priklad[u-1] *= priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "-" in priklad:
        p = priklad.count("-")
        for i in range(p):
            u = priklad.index("-")
            priklad[u-1] -= priklad[u+1]
            del priklad[u]
            del priklad[u]
    if "+" in priklad:
        p = priklad.count("+")
        for i in range(p):
            u = priklad.index("+")
            priklad[u-1] += priklad[u+1]
            del priklad[u]
            del priklad[u]
    return(priklad)

priklad = vypocet(priklad, c)
print()
if len(priklad) > 0:
    print(priklad[0])
input()
#(22*51+(60   - 25)/6.5)^6
