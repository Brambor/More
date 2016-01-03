from urllib.request import Request, urlopen
import time

url1 = "http://i9.mangareader.net/mysterious-girlfriend-x/"
kap = 0
url2 = "/mysterious-girlfriend-x-"
stranka = 585677 #585677
mastranka = 1
strany_celkem = 0
waitfor = 0

kapitoly = []
cesta = "C:\Documents and Settings\Administrator\Plocha\Tonda\wget-1.17.1-win32\www.mangareader.net\mysterious-girlfriend-x"
for n in range(85): #C:\Documents and Settings\Administrator\Plocha\Tonda\wget-1.17.1-win32\www.mangareader.net\mysterious-girlfriend-x
    myfile = open("{}\{}\{}".format(cesta, n, 2), "r")
    a = myfile.read().split("mysterious-girlfriend-x-")[2].split(".jpg")[0] ###TODO: This is it!!!
    kapitoly.append(int(a) - 2)

start = time.time()



#kap = 50
#mastranka = 2
#strany_celkem = 1009


while kap < 100:
    try:
        ted = time.time()
        req = Request("".join([url1, str(kap), url2, str(stranka), ".jpg"]), headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()

        strany_celkem += 1

        myfile = open("{} - {} ({}).png".format(kap, mastranka, strany_celkem), "wb")
        myfile.write(webpage)
        myfile.close()

        print("kap {}\tstranka {}\tstrany celkem {}\tcas {}".format(kap, mastranka, strany_celkem, time.time() - ted))
        stranka += 1
        mastranka += 1
        waitfor = 0
    except:
        print("kap {}\tstranka {}\tstrany celkem {}\tcas {}\n\t FAILED\t strana {}".format(kap, mastranka, stranka - 585676, time.time() - ted, stranka))
        waitfor += 1
        if mastranka != 1 and waitfor > 100:
            kap += 1
            stranka = kapitoly[kap]
            mastranka = 1
        stranka += 1

#base = http://i1.mangareader.net/mysterious-girlfriend-x/0/mysterious-girlfriend-x-585677.jpg
print(time.time() - start)
input("DONE")