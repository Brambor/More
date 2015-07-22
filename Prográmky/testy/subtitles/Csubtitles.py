import time

titulky=open("subtitles.txt","r")
Ltitulky=titulky.read().split("\n")
titulky.close()
for i in Ltitulky:
    CLtitulky=i
    for i in CLtitulky:
        print(i,end="")
        time.sleep(0.049)
    print()
    time.sleep(0.5)
