verze = input("verze:\n1)celý méno\n2) png > jpg\n")
from os import listdir
if verze == "1":
	from os.path import isfile, join

	mypath = "C:\Documents and Settings\Administrator\Plocha\Tonda\MGX"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	for f in sorted(onlyfiles):
	    new = f.split("(")[1].split(")")[0]
	    new = "0"*(4 - len(new)) + new
	    file = open("{}\{}".format(mypath, f), "rb")
	    newfile = open("{}\MGX sorted\{}.png".format(mypath, new), "wb")
	    newfile.write(file.read())
	    file.close()
	    newfile.close()
	    print(new)

	from os import listdir
elif verze == "2":
	oldpath = "C:\Documents and Settings\Administrator\Plocha\Tonda\MGX3"
	newpath = "C:\Documents and Settings\Administrator\Plocha\Tonda\MGX3 right"

	for f in [fil for fil in listdir(oldpath)]:
		new = "{}.jpg".format(f.split(".")[0])
		oldfile = open("{}\{}".format(oldpath, f), "rb")
		newfile = open("{}\{}".format(newpath, new), "wb")
		newfile.write(oldfile.read())
		newfile.close()
		oldfile.close()
		print(new)

input("DONE")
