# http://www.pythonchallenge.com/pc/def/peak.html
import pickle
#import sys



text = open("5.txt", "r+b")
string = text.read()
input("loaded")

#with open("myfile", "rb") as f:
#    byte = f.read(1)
#    while byte != b"":
#        # Do stuff with byte.
#        byte = f.read(1)

#input("working?")
pickle.Unpickler(text).load()

# pickle.load(file[, *, fix_imports=True, encoding="ASCII", errors="strict"])
#pickle.load()

#pickletools.dis(string)

input("DONE")