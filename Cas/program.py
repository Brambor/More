import datetime

start = datetime.datetime.now()


zaznam = open("zaznam.txt", 'a')

zaznam.write("\n")

zaznam.write(str(start))

oldcas = open("cas.txt", "r").read().replace("\n", ";")
print(oldcas)
zaznam.write("\t" + oldcas)

name = None
while name != "Tonda" and name != "Janek":
	print("Write your name:")
	name = input()
	print(name)
zaznam.write("\t" + name)


input("press to stop")

stop = datetime.datetime.now()
zaznam.write("\t" + str(stop))
zaznam.write("\t" + oldcas.replace("1:24", "0:15"))


zaznam.close()
