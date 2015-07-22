# http://www.pythonchallenge.com/pc/def/oxygen.html
import pygame
pic = pygame.image.load("7.png")
strings = []
delky = []
for typ in ["RGBX"]: # "RGB", "RGBX", "RGBA", "ARGB", "RGBA_PREMULT", "ARGB_PREMULT"
	string = pygame.image.tostring(pic, typ)
	strings.append(string)
	#print(string)
for i in range(len(strings)):
	strings[i] = strings[i].decode("utf-8", errors = "ignore")
for i in strings:
	delky.append(len(list(i)))
print(delky) # [179265, 239020, 239020, 239020, 239020, 239020] [138999, 138998, 138998, 138998, 138998, 138998]
string = strings[0]
mylist = list(string)
pocet = 0
vysledek = ""
last = [] # prostě něco, co tam určitě nebude
for i in range(0, 138996):
	if mylist[i] == mylist[i+1]  == mylist[i+2]  == mylist[i+3]: #může jich tu být i 25, výstup je stejný (myslím, že max délka = výšce té skvrny :))
		pocet += 1
		if mylist [i] != last:
			vysledek += mylist[i]
			print(mylist[i], end = "")
			last = mylist[i]
#print(vysledek)
print("DONE first part")
# Já to extraktoval!!!!!! yay! jsem tak šťastý :D takovou divnou myšlenkou jsem to dokázal :D
#[105, 10, 16, 101, 103, 14, 105, 16, 121] to byl můj výsledek, nepočítal jsem se zdvojenýma jedničkama :/ To mě mělo napadnout :'(
zadani = [105, 10, 16, 101, 103, 14, 105, 16, 121]
for i in range(len(zadani)): #30
	if zadani[i] < 100: #30
		zadani[i] +=100 #30
for i in zadani:
	print(str(chr(i)), end = "")
print()
input("DONE")

# http://www.pythonchallenge.com/pc/def/integrity.html