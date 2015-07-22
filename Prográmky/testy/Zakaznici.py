import random

print("'name' want:\n'product' 'quantity' 'prize of that item'(You can change them in 'Change prize')")

ZakazniciStanek={"Bugopaki.M.2.16:00-18:00.0.50.0.10.Strawberry,5-10,4":2,"Naxona.F.2.16:00-18:00.0.50.0.10.Strawberry,5-10,4":5}
for i in ZakazniciStanek:
    jmeno,pohlavi,Idny,Ihodiny,dny,spokojenost,obsluhy,trpelivost,nakup=i.split(".")
    plod,Vmnozstvi,Vcena=nakup.split(",")
    male,velke=Vmnozstvi.split("-")
    mnozstvi=random.randint(int(male),int(velke))
    print(jmeno+" want:\n"+plod+" "+str(mnozstvi)+"ks")#+" ("+Vcena+" penize)")
