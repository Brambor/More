def ctverec(i,i2):
    velky,maly=i,i2
    x,y=[0]*2
    if velky < 3:
        x+=3*velky
    elif velky < 6:
        x+=3*(velky-3)
        y+=3
    else:
        x+=3*(velky-6)
        y+=6
    if maly < 3:
        x+=maly
    elif maly < 6:
        x+=maly-3
        y+=1
    else:
        x+=maly-6
        y+=2
    return x,y
def zobrazit(vse):
    for sudoku in vse:
        for i in [sudoku]:
            zobrazitL=[]
            for i2 in range(9):
                zobrazitL.append("".join(i[i2]))
            zobrazitL="\n".join(zobrazitL)
            print(zobrazitL,end="\n\n")
def resitel(sudoku):
    Mlinie=[[str(x+1) for x in range(9)] for i in range(9)]
    Mctverec=[[str(x+1) for x in range(9)] for i in range(9)]
    Msloup=[[str(x+1) for x in range(9)] for i in range(9)]
    Mvsechny=[]
    for i in range(9):
        a=[]
        for i2 in range(9):
            a.append([])
        Mvsechny.append(a)
    for i in range(9):
        for i2 in range(9):
            if sudoku[i][i2] in Mlinie[i]:
                del Mlinie[i][Mlinie[i].index(sudoku[i][i2])]
    for i in range(9):
        for i2 in range(9):
            if sudoku[i2][i] in Msloup[i]:
                del Msloup[i][Msloup[i].index(sudoku[i2][i])]
    for i in range(9):
        for i2 in range(9):
            x,y=ctverec(i,i2)
            if sudoku[y][x] in Mctverec[i]:
                del Mctverec[i][Mctverec[i].index(sudoku[y][x])]
    for i in range(9):
        for i2 in range(len(Mlinie[i])):
            for i3 in range(9):
                if sudoku[i][i3]=="#":
                    if Mlinie[i][i2] in Msloup[i3]:
                        x,y=ctverec(i,i3)
                        if Mlinie[i][i2] in Mctverec[y]:
                            Mvsechny[i][i3].append(Mlinie[i][i2])
    for i in range(9):
        for i2 in range(9):
            if sudoku[i][i2]=="#" and len(Mvsechny[i][i2])==0:
                return(["nic"])
    for i in range(9):
        for i2 in range(9):
            if len(Mvsechny[i][i2])==1:
                sudoku[i][i2]=Mvsechny[i][i2][0]
                return([sudoku])
            elif len(Mvsechny[i][i2])>1:
                more=[]
                for i3 in range(len(Mvsechny[i][i2])):
                    sudoku[i][i2]=Mvsechny[i][i2][i3]
                    more.append([[], [], [], [], [], [], [], [], []])
                    for i4 in range(9):
                        more[i3][i4].extend(sudoku[i4])
                return(more)
    return([sudoku])