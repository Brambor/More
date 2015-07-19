breakit=False
print("Start!")
while True:
    if breakit==True:
        break
    menu=input("menu\n")
    if menu=="help":
        print("help")
    elif menu=="1":
        print(1)
    elif menu=="2":
        while True:
            print(2)
            menu1=input("menu1\n")
            if menu1=="help":
                print("help")
            elif menu1=="1":
                print(1)
            elif menu1=="2":
                print(2)
            elif menu1=="back":
                breakit=True
                break
    elif menu=="back":
        print("can not")
    
