import msvcrt

pole=[["#"]*9 for i in range(9)]

x = 4
y = 4
znak=pole[y][x]
#for a in range(1):
while True:
    char = msvcrt.getch()
    print(char)
    pole[y][x]=znak
    if (char == b'a'):
        x -= 1
    elif (char == b'd'):
        x += 1
    elif (char == b'w'):
        y -= 1
    elif (char == b's'):
        y += 1
    znak=pole[y][x]
    pole[y][x]="0"
    pole_show=[]
    for b in pole:
        pole_show.append("".join(b))
    pole_show="\n".join(pole_show)
    print(pole_show)
