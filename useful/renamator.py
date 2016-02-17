for f in os.listdir(path):
	with open("{}/{}".format(path, f), "rb") as oldfile:
		newname = "{}{}".format((7 - len(f))*"0", f)
		with open("{}/new/{}".format(path, newname), "wb") as newfile:
			newfile.write(oldfile.read())