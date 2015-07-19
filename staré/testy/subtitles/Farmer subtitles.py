import time
input()
for i in range(50):
    print()
titulky=open("subtitles.txt","r").read().split("\n")
for i in titulky:
    print(i)
    time.sleep(1)
