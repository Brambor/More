from urllib.request import Request, urlopen
import time

def myrequest(url):
	worked = False
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	a = time.time()
	while not worked:
		try:
			print(time.time()- a)
			a = time.time()
			webpage_read = urlopen(req).read().decode("utf-8")
			print("Sorry, this video cannot be edited." in webpage_read)
			worked = True
		except:
			print("failed to connect to \n{}".format(url))
	return webpage_read

vid = "ByNDv3uG0eg"
url = "https://www.youtube.com/enhance?v="
page = myrequest("{}{}".format(url, vid))