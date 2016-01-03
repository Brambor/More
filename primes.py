def primes(p = [2], min = 2, max = 100):
    for n in range(min, max):
        accept = True
        for prime in p:
            if n % prime == 0:
                accept = False
        if accept:
            p.append(n)
    return(p)

p = primes()
print(p)

def delitele(n):
    """
    n cislo
    return(list dělitelů)
    """
    myd = []
    for i in range(1, n + 1):
        if n % i == 0:
            myd.append(i)
    return(myd)

def sudlich(myd):
    """
    myd list dělitelů
    return(list(list sudých, list lichých))
    """
    sud = []
    lich = []
    for i in myd:
        if i % 2 == 0:
            sud.append(i)
        else:
            lich.append(i)
    return([sud, lich])

def ok(sl):
    mysl = (sl[0], sl[1])
    if len(mysl[0]) - len(mysl[1]) == 3:
	    return True
    return False

for n in range(10000):
    a = delitele(n)
    b = sudlich(a)
    c = ok(b)
    if c:
        print(n, a, b)
        sumsud, sumlich = 0, 0
        for i in b[0]:
            sumsud += i
        for i in b[1]:
            sumlich += i
        print(sumsud/sumlich)
