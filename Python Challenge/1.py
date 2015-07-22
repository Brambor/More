# http://www.pythonchallenge.com/pc/def/map.html

#abcdefghijklmnopqrstuvwxyz
#k->m +2
#o->q +2
#e->g +2

sifra = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
Lreseni=[]
abeceda = list("abcdefghijklmnopqrstuvwxyz")
Lsifra = list(sifra)
for i in Lsifra:
	if i in abeceda:
		if abeceda.index(i) + 2 < len(abeceda):
			vystup = abeceda[abeceda.index(i) + 2]
		else:
			vystup = abeceda[abeceda.index(i) + 2 - len(abeceda)]
	else:
		vystup = i
	Lreseni.append(vystup)
reseni = "".join(Lreseni)
print(reseni)
input()

# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

# změňte map v url adrese na ocr :)
# http://www.pythonchallenge.com/pc/def/ocr.html