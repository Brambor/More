import time
def datum(sl,cas):
    dny,mesice,kontrola=cas
    cas=[]
    if kontrola=True and dny > sl:
        dny-=sl
        mesice+=1
        cas=[dny,mesice,kontrola]
    else:
        kontrola=False
        cas=[dny,mesice,kontrola]
    return cas

while True:
    kontrola=True
    sec=
