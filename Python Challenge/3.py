# http://www.pythonchallenge.com/pc/def/equality.html

abeceda = "abcdefghijklmnopqrstuvwxyz"
ABECEDA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
La = list(abeceda)
LA = list(ABECEDA)

text = open("3.txt", "r")
string = text.read()
Lstring = list(string)
Lstring.insert(0, "a")
Lstring.append("a")
vysledek = ""
for i in range(4, 101247):
	#pass
	if Lstring[i-4] in La and Lstring[i-3] in LA and Lstring[i-2] in LA and Lstring[i-1] in LA and Lstring[i] in La and Lstring[i+1] in LA and Lstring[i+2] in LA and Lstring[i+3] in LA and Lstring[i+4] in La:
		vysledek = vysledek + Lstring[i]
print(vysledek)
input("end")

# na stránce je linkedlist.php, takže přepíŠete html na php :)
# http://www.pythonchallenge.com/pc/def/linkedlist.php