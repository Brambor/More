from os import listdir
from urllib.request import Request, urlopen

path = "E:/MGX/MGX pics"

fs = [f for f in listdir(path)]
ef = []

allpic = []

for f in fs:
	new = open("{}\\{}".format(path, f), "rb").read()
	allpic.append(new)
	print(f)

for i in range(len(allpic)):
	print(fs[i])
	for i2 in range(1, len(allpic) - i):  #value_when_true if condition else value_when_false
		if allpic[i] == allpic[i + i2]:
			print("{} is the same as {}".format(fs[i + i2], fs[i]))
			ef.append(fs[i + i2])

#for i in range(len(fs)-1):
#	f1 = open("{}\{}".format(path, fs[i]), "rb")
#	f2 = open("{}\{}".format(path, fs[i + 1]), "rb")
#	if list(f1) == list(f2):
#		print("yes!!!!, {} and {}".format(fs[i], fs[i + 1]))
#		ef.append(fs[i + 1])



#for f in ef:
#	prechap = str(int(f[0])*10 + int(f[1]))
#	chap = (3 - len(prechap))*"0" + prechap
#	if f[2] == "5":
#		chap += ".5"
#	ep = str(int(f[3])*10 + int(f[4]))
#	req1 = Request("{}/v{}/c{}/{}.html".format(url, vol, chap, ep), headers={'User-Agent': 'Mozilla/5.0'})
#	webpage_read = urlopen(req1).read().decode('utf-8')
#	while "is not available yet" in webpage_read:
#		prevol = str(int(vol) + 1)
#		vol = (2 - len(prevol))*"0" + prevol
#		print(vol)
#		req1 = Request("{}/v{}/c{}/{}.html".format(url, vol, chap, ep), headers={'User-Agent': 'Mozilla/5.0'})
#		webpage_read = urlopen(req1).read().decode('utf-8')
#	print(f)

input("DONE")
