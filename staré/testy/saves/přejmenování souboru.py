import os

a=input("Name of save.\n")
b=input("New name.\n")
#save=open(a+".txt","w+")
os.rename(a+'.txt',b+'.txt')
