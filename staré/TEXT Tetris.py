import time

def pis(pole):
    for i in pole[pole[0]]:
        print(i,end="")
    pole[0]+=1
    return(pole)

pole=[1,["1"," "," "," "," "," "," "," "," "," "],["2"," "," "," "," "," "," "," "," "," "],["3"," "," "," "," "," "," "," "," "," "],["4"," "," "," "," "," "," "," "," "," "],["5"," "," "," "," "," "," "," "," "," "],["6"," "," "," "," "," "," "," "," "," "],["7"," "," "," "," "," "," "," "," "," "],["8"," "," "," "," "," "," "," "," "," "],["9"," "," "," "," "," "," "," "," "," "],["1","0"," "," "," "," "," "," "," "," "],["1","1"," "," "," "," "," "," "," "," "],["1","2"," "," "," "," "," "," "," "," "],["1","3"," "," "," "," "," "," "," "," "],["1","4"," "," "," "," "," "," "," "," "],["1","5"," "," "," "," "," "," "," "," "],["1","6"," "," "," "," "," "," "," "," "],["1","7"," "," "," "," "," "," "," "," "]]
zobrazeni=["1234","2345","3456","4567"]
speed=0
score=0
lines=0
best=0

input()
for p in range(1):
    time.sleep(0.5)
#    print("\n\n\n\n\n\n")
#    for i in range(1):
#        time.sleep(0.5)
#        print("╔══════════╦═════╗\n║1         ║Next ║\n║2         ║1234 ║\n║3         ║2345 ║\n║4         ║3456 ║\n║5         ║4567 ║\n║6         ╠═════╣\n║7         ║Speed║\n║8         ║0    ║\n║9         ╠═════╣\n║10        ║Score║\n║11        ║0    ║\n║12        ╠═════╣\n║13        ║Lines║\n║14        ║0    ║\n║15        ╠═════╣\n║16        ║Best ║\n║17        ║0    ║\n╚══════════╩═════╝")
    print(p)
    print("╔══════════╦═════╗\n║",end="")
    pis(pole)
    print("║Next ║\n║",end="")
    pis(pole)
    for i in range(4):
        print("║"+zobrazeni[i]+" ║\n║",end="")
        pis(pole)
    print("╠═════╣\n║",end="")
    pis(pole)
    print("║Speed║\n║",end="")
    pis(pole)
    space=" "*(5-len(list(str(speed))))
    print("║"+str(speed)+space+"║\n║",end="")
    pis(pole)
    print("╠═════╣\n║",end="")
    pis(pole)
    print("║Score║\n║",end="")
    pis(pole)
    space=" "*(5-len(list(str(score))))
    print("║"+str(score)+space+"║\n║",end="")
    pis(pole)
    print("╠═════╣\n║",end="")
    pis(pole)
    print("║Lines║\n║",end="")
    pis(pole)
    space=" "*(5-len(list(str(lines))))
    print("║"+str(lines)+space+"║\n║",end="")
    pis(pole)
    print("╠═════╣\n║",end="")
    pis(pole)
    print("║Best ║\n║",end="")
    pis(pole)
    space=" "*(5-len(list(str(best))))
    print("║"+str(best)+space+"║\n╚══════════╩═════╝",end="")
    pole[0]=1
input()
