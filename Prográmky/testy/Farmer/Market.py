
                    Atime+=int(len(ZakazniciStanek)/2+0.5)
                    if len(stanek) > 0:
                        prizes={}
                        print("Set prize")
                        for i in range(len(stanek)):
                            breakZakaznici=False
                            while True:
                                if breakZakaznici==True:
                                    break
                                for i in stanek:
                                    prize=input(i+": ")
                                    if prize.isdigit():
                                        if float(prize) > 0.0:
                                            print("OK")
                                            prizes["Strawberry"]=float(prize)
                                            breakZakaznici=True
                                            break
                                        elif float(prize)==0:
                                            print("You can not sell things 'for free'.")
                                        else:
                                            print("You can not pay for selling things.")
                                    else:
                                        print("Prize is expressible only by numbers. Eventually with point('.')")
                        for i in range(len(ZakazniciStanek)):
                            menu1=input("1. Wait on customer.\n2. Do not wait on customer.")
                            if menu1=="help":
                                help()
                                print("Note: You can not go back in this menu by writing back but by choose 2.")
#                            elif menu1=="1":obsluhování zákazníku:
#                            elif menu1=="2":obsloužit/neobsloužit
