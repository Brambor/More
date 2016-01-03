from urllib.request import Request, urlopen
import time

#input()
url = "http://www.mangareader.net/mysterious-girlfriend-x" #base = "http://www.mangareader.net/mysterious-girlfriend-x/0/1"
kap = "0"
stranka = "1" #1
celkem = 0

start = time.time()

while True:

	ted = time.time()
	req = Request("{}/{}/{}".format(url, kap, stranka), headers={'User-Agent': 'Mozilla/5.0'})
	webpage_read = urlopen(req).read().decode('utf-8')

	if "is not released yet" in webpage_read:
		break

	#http://i3.mangareader.net/mysterious-girlfriend-x/0/mysterious-girlfriend-x-585760.jpg
	url_obr = webpage_read.split("mysterious-girlfriend-x-")[-1].split(".jpg")[0]
	url_to_pic = "".join("{}{}{}".format("http://i3.mangareader.net/mysterious-girlfriend-x/", kap, "/mysterious-girlfriend-x-"))
	req = Request("".join((url_to_pic, url_obr, ".jpg")), headers={'User-Agent': 'Mozilla/5.0'})
	obr = urlopen(req).read()

	#save
	ctyrnazev = (2 - len(kap))*"0" + kap + (2 - len(stranka))*"0" + stranka
	myfile = open("{}\{}.png".format("C:\Documents and Settings\Administrator\Plocha\Tonda\MGX2", ctyrnazev), "wb")
	myfile.write(obr)
	myfile.close()

	#next page
	kapstr = webpage_read.split("'/mysterious-girlfriend-x/")[1].split("';")[0]
	if "/" in kapstr:
		kap, stranka = kapstr.split("/")
	else:
		kap, stranka = kapstr, "1"

	celkem += 1
	print("strana {}\tza {}\tsekund".format(ctyrnazev, time.time() - ted))

print("{} stranek\tza {}\tsekund".format(celkem, time.time() - start))
input("DONE")