from urllib.request import Request, urlopen
import time

#input()
url = "http://www.mangahere.co/manga/mysterious_girlfriend_x" #base = "http://www.mangareader.net/mysterious-girlfriend-x/0/1"
vol = "01" #01
chap = "000" #000
ep = "50" #1
celkem = 0
doesnotwork = []
start = time.time()
doeswork = False

while True:
	ted = time.time()
	req1 = Request("{}/v{}/c{}/{}.html".format(url, vol, chap, ep), headers={'User-Agent': 'Mozilla/5.0'})
	webpage_read = urlopen(req1).read().decode('utf-8')

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
	else:
		doesnotwork.append(petinazev)
		print("{} was not downloaded".format(petinazev))
		errorlog.write(", {}".format(petinazev))
		errorlog.close()
		doeswork = False

	#next page
	if len(webpage_read.split('selected="selected">')[1].split('</option>')[1]) > 200:
		if "Next Chapter:" in webpage_read:
			vch = webpage_read.split('Next Chapter:</strong> <a href="http://www.mangahere.co/manga/mysterious_girlfriend_x/')[1].split('/">')[0]
			vol, chap = vch.split('/')
			vol, chap = vol[1:], chap[1:]
			ep = "1"
		else:
			break
	else:
		ep = str(int(ep) + 1)


	celkem += 1
	print("strana {}\tza {}\tsekund".format(petinazev, time.time() - ted))

print("{} stranek\tza {}\tsekund".format(celkem, time.time() - start))
if len(doesnotwork) > 0:
	print("These files has not been downloaded:", end = " ")
	for dnw in doesnotwork:
		print(dnw, end = ", ")
input("\nDONE")
