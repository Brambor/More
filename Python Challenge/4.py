# http://www.pythonchallenge.com/pc/def/linkedlist.php
import urllib.request

zbytek = b"12345"
cisla = []
i = 1
priste = False
while True:
	response = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+zbytek.decode("utf-8"))
	html = response.read()
	neco = html.split()
	if len(neco) != 6:
		if priste:
			break
		priste = True 
	zbytek = neco[5]
	if neco[5].decode("utf-8") in cisla:
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
	cisla.append(neco[5].decode("utf-8"))
	print(str(i) + ". " + html.decode("utf-8"))
	i += 1

print(html.decode("utf-8"))
input("DONE")

# http://www.pythonchallenge.com/pc/def/peak.html