class Myclass():
	def __init__(self): #To asi znáš
		print("I'm alive!")

print("#A = Myclass()")
A = Myclass()

class Myclass2(Myclass): #Děd z Myclass
	def __str__(self): #Když se někdo zeptá na str(Myclass2), tak
		return "7" #uveď hodnotu "7"


print("\n#B = Myclass2()")
B = Myclass2()

print("\n#print(B)")
print(B)

input("\nKoukni do komentářů :)")