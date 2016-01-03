from urllib.request import Request, urlopen
import time
from os import listdir

#input()
url = "http://www.mangahere.co/manga/mysterious_girlfriend_x" #base = "http://www.mangareader.net/mysterious-girlfriend-x/0/1"
vol = "01" #01
chap = "000" #000
ep = "1" #1
celkem = 0
start = time.time()
doeswork = False

path = "C:\Documents and Settings\Administrator\Plocha\Tonda\MGX3 right"
fs = [f for f in listdir(path)]
ef = []
for i in range(len(fs)-1):
	f1 = open("{}\{}".format(path, fs[i]), "rb")
	f2 = open("{}\{}".format(path, fs[i + 1]), "rb")
	if list(f1) == list(f2):
		print(fs[i + 1])
		ef.append(fs[i + 1])


for f in ef:
	ted = time.time()
	while not doeswork:

		prechap = str(int(f[0])*10 + int(f[1]))
		chap = (3 - len(prechap))*"0" + prechap
		if f[2] == "5":
			chap += ".5"
		ep = str(int(f[3])*10 + int(f[4]))
		req1 = Request("{}/v{}/c{}/{}.html".format(url, vol, chap, ep), headers={'User-Agent': 'Mozilla/5.0'})
		webpage_read = urlopen(req1).read().decode('utf-8')
		while "is not available yet" in webpage_read:
			prevol = str(int(vol) + 1)
			vol = (2 - len(prevol))*"0" + prevol
			print(vol)
			req1 = Request("{}/v{}/c{}/{}.html".format(url, vol, chap, ep), headers={'User-Agent': 'Mozilla/5.0'})
			webpage_read = urlopen(req1).read().decode('utf-8')
		print(f)

		#http://a.mhcdn.net/store/manga/794/10-092.0/compressed/cmysterious_girlfriend_x_-_chapter_092_-_page_036.jpg?v=1411607222
		try:
			url_to_pic = webpage_read.split('" onerror="')[0].split('<img src="')[-1]
			req2 = Request(url_to_pic, headers={'User-Agent': 'Mozilla/5.0'})
			obr = urlopen(req2).read()
			doeswork = True
		except:
			doeswork = False
			errorlog = open("C:\Documents and Settings\Administrator\Plocha\Tonda\errorlog MGX3.txt", "a")
		#save
		#chap does not need to be edited every ep, only every chap
		
		if len(chap.split(".")) == 1:
			mychap = str(int(chap)) + "0"
		else:
			mychap = str(int(chap.split(".")[0])*10 + int(chap.split(".")[1]))
		mychap = (3 - len(mychap))*"0" + mychap

		petinazev = (mychap + (2 - len(ep))*"0" + ep)
		print("Does work:{}".format(doeswork))
		if doeswork:
			myfile = open("{}\{}.jpg".format("C:\Documents and Settings\Administrator\Plocha\Tonda\MGX3", petinazev), "wb")
			myfile.write(obr)
			myfile.close()
	doeswork = False
	#next page
	#nahoře


	celkem += 1
	print("strana {}\tza {}\tsekund".format(petinazev, time.time() - ted))

print("{} stranek\tza {}\tsekund".format(celkem, time.time() - start))
input("\nDONE")
