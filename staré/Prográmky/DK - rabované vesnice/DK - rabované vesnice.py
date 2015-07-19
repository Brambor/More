soubor=open("Rvesnice.txt","r")
Rvesnice=soubor.read().split("\n")
soubor.close()
soubor=open("vesnice.txt","r")
vesnice=soubor.read().split("\n")
soubor.close()
menu=None
while menu != "":
    menu=input("Zadejte vesnice, které rabujete")
    if menu != "":
        Rvesnice.append(menu)
y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14=[[" "]*20]*14
for i in vesnice:
    x,y=i.split(" ")
    x,y=int(x),int(y)
    a=None
    if y==593:
        a=y1
    if y==594:
        a=y2
    if y==595:
        a=y3
    if y==596:
        a=y4
    if y==597:
        a=y5
    if y==598:
        a=y6
    if y==599:
        a=y7
    if y==600:
        a=y8
    if y==601:
        a=y9
    if y==602:
        a=y10
    if y==603:
        a=y11
    if y==604:
        a=y12
    if y==605:
        a=y13
    if y==606:
        a=y14
    a.pop(int(x)-593)
    a.insert(int(x)-593,"V")
    if y==593:
        y1=a
    if y==594:
        y2=a
    if y==595:
        y3=a
    if y==596:
        y4=a
    if y==597:
        y5=a
    if y==598:
        y6=a
    if y==599:
        y7=a
    if y==600:
        y8=a
    if y==601:
        y9=a
    if y==602:
        y10=a
    if y==603:
        y11=a
    if y==604:
        y12=a
    if y==605:
        y13=a
    if y==606:
        y14=a
print("".join(y1)+"\n"+"".join(y2)+"\n"+"".join(y3)+"\n"+"".join(y4)+"\n"+"".join(y5)+"\n"+"".join(y6)+"\n"+"".join(y7)+"\n"+"".join(y8)+"\n"+"".join(y9)+"\n"+"".join(y10)+"\n"+"".join(y11)+"\n"+"".join(y12)+"\n"+"".join(y13)+"\n"+"".join(y14))
