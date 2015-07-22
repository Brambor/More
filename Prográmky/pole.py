import msvcrt


x,y=[5]*2
pole=[["#"] * x for i in range(y)]
x,y=int(x/2),int(y/2)

#while True:
for p in range(1):
    #print(pole)
    print(str(x)+" "+str(y))
    pole_zobrazeni=pole[:]
    print(pole)
    pole_zobrazeni[y][x]="X"
    print(pole)
    pole_zobrazeni2=[]
    for i in pole_zobrazeni:
        pole_zobrazeni2.append("".join(i))
    pole_zobrazeni2="\n".join(pole_zobrazeni2)
    #print(pole)
    #print(pole_zobrazeni2)
    char = msvcrt.getch()
    #print(char)
    if (char == b'a'):
        x -= 1
    elif (char == b'd'):
        x += 1
    elif (char == b'w'):
        y -= 1
    elif (char == b's'):
        y += 1
