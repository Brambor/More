deníkKg={"brambor":7,"chleba":0.3}
deníkKs={"chipsy":1,"jahody":7}
print("Food:")
food=list(set(deníkKg))
for i in range(len(food)):
    print(food[i]+" "+str(deníkKg[food[i]])+"kg")
print()
food=list(set(deníkKs))
for i in range(len(food)):
    print(food[i]+" "+str(deníkKs[food[i]])+"ks")
