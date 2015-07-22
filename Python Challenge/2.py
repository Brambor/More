# http://www.pythonchallenge.com/pc/def/ocr.html

pocet = {}
abeceda = list("abcdefghijklmnopqrstuvwxyz")
text = open("2.txt", "r")
string = text.read()
Lstring = list(string)
print(len(Lstring))
for i in Lstring:
	if i in pocet:
		pocet[i] += 1
	else:
		pocet[i] = 1
print(pocet)
input()

text=""
for i in Lstring:
	if i in abeceda:
		text = text + i
print(text)
input()

# http://www.pythonchallenge.com/pc/def/equality.html