import smore

sudoku=[["#"]*9 for i in range(9)]
soubor=open("zadani.txt","r")
vse=[]
vysledky=[]
zad=soubor.read().split("\n")
troj=zad[1].split()#Volba zadání
for i in troj:
    j=list(i)
    sudoku[int(j[0])][int(j[1])]=j[2]
vse.append([[], [], [], [], [], [], [], [], []])
for i in range(9):
    vse[0][i].extend(sudoku[i])

while len(vse)>0:
    ven=smore.resitel(vse.pop(0))
    if ven != ["nic"]:
        konec=True
        for i in range(len(ven)):
            for i2 in range(9):
                if "#" in ven[i][i2]:
                    konec=False
        if konec:
            delka=len(vysledky)
            for i in range(len(ven)):
                vysledky.append([[], [], [], [], [], [], [], [], []])
                for i2 in range(9):
                    vysledky[delka+i][i2].extend(ven[i][i2])
        else:
            delka=len(vse)
            for i in range(len(ven)):
                vse.append([[], [], [], [], [], [], [], [], []])
                for i2 in range(9):
                    vse[delka+i][i2].extend(ven[i][i2])
input("Toť vše.")