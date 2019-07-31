from os import get_terminal_size

import smore

#####

ZADANI = 2

#####

sudoku=[["#"]*9 for i in range(9)]
soubor=open("zadani.txt","r")
vse=[]
vysledky=[]
zad=soubor.read().split("\n")
troj=zad[ZADANI].split()
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

# 'ven' are all solutions
# ven = ven*60
sudoku_per_row = (get_terminal_size().columns + 1) // 10
#sudoku_per_row = 28
for i in range(0, len(ven), sudoku_per_row):
    # number the sudoku (one line)
    print(" ".join( ("%d" % j).center(9, "=") for j in range(i, min(len(ven), i+sudoku_per_row)) ))
    # print the sudoku (9 lines; as many sudoku as fit the terminal)
    print("\n".join(" ".join("".join(row) for row in rows) for rows in zip(*ven[i:i+sudoku_per_row])))
    print()  # newline

input("Toť vše.")