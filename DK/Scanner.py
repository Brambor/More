print("Scanner.")
kmen,sektor,mimo=[],[],[]
while True:
    menu=input("S/K/?/exit\n")
    if menu == "K":
        vstup,pocet=None,0
        kmenInfo=[]
        while vstup !="":
            vstup=input()
            if vstup !="":
                kmenInfo.append(vstup)
                pocet+=1
        print("XXXXXXXXXXXXXXXX")
        print(kmen)
        for i in range(pocet):
            a,x1,x2,x3,x4=kmenInfo[i-1].split("\t")
            kmen.append(a)
            print(a)
            print(kmen)
        print("!!!!!!!!!!!!!!!!!!!")
    elif menu == "S":
        vstup,pocet=None,0
        while vstup !="":
            vstup=input()
            if vstup !="":
                sektor.append(vstup)
                pocet+=1
    elif menu == "?":
        sektorNOTkmen=[]
        for i in sektor:
            if i in kmen:
                str()
            else:
                if i in mimo:
                    str()
                else:
                    mimo.append(i)
        print(mimo)
    elif menu == "exit":
        break
