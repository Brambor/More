import time
import random

a=input("Jakmile nebudete chtít psát jména, nechte jedno prázdné.\n")
kolo=[]
while a != "":
    kolo.append(a)
    a=input()
while True:
    input("Chcete ho roztočit?")
    Time=random.randint(15,30)
    for i in range(Time):
        for i in kolo:
            print(i)
            time.sleep(int(1/Time))
        Time-=1
    
