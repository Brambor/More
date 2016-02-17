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

path = "E:/MGX" #"C:\\Users\\Tonda_2\\Desktop\\harddisk\\MGX"
fs = [f for f in listdir("{}\\{}".format(path, "MGX pics"))]
ef = []
allpic = []

for f in fs:
	new = open("{}\\{}".format("{}\\{}".format(path, "MGX pics"), f), "rb").read()
	allpic.append(new)
	print(f)

for i in range(len(allpic)):
	print(fs[i])
	for i2 in range(1, len(allpic) - i):  #value_when_true if condition else value_when_false #1, 5 if len(allpic) - i > 5 else len(allpic) - i
		if allpic[i] == allpic[i + i2]:
			print("{} is the same as {}".format(fs[i + i2], fs[i]))
			ef.append(fs[i + i2])

ef = ["49008.jpg"]
print(ef)

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
			errorlog = open("{}\\{}".format(path, "errorlog MGX3.txt"), "a")
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
			myfile = open("{}\{}.jpg".format("{}\\{}".format(path, "MGX pics"), petinazev), "wb")
			myfile.write(obr)
			myfile.close()
	doeswork = False
	#next page
	#nahoře


	celkem += 1
	print("strana {}\tza {}\tsekund".format(petinazev, time.time() - ted))

print("{} stranek\tza {}\tsekund".format(celkem, time.time() - start))
input("\nDONE")
