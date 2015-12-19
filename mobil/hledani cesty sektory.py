from random import randint
import copy
import string
import queue

class Map():
    """
    The map
    search(self); searchit(self, x, y, next); searchback(self); findback(self, x, y)
        are used for the finding
    show(self)
        print actuall state of map
    sector(self, x, y)
        does nothing, yet
    """
    def __init__(self, y, x):
        self.x, self.y = x, y
        self.pole = []
        for i in range(y):
            self.pole.append([])
            self.pole[i].extend([" "]*x)
        self.done, self.znaky = False, ["A"]
        self.q = queue.Queue()
        self.index = 0
    def show(self):
        pole = copy.copy(self.pole)    
        for i in range(len(pole)):
            pole[i] = "".join(pole[i])
        print("\n".join(pole))
        print("v"*self.x)
    def search(self):
        while not self.done:
            if not self.q.empty():
                me, x, y = self.q.get()
                poss = [[x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y]]
                for pos in poss:
                    self.searchit(pos[0], pos[1], me + 1)
            else:
                break
    def searchit(self, x, y, next):
        place = self.pole[y][x]
        if place == " ":
            self.pole[y][x] = self.znaky[next]
            self.q.put((next, x, y))
        elif place == "B":
            self.done = True
            self.destin, self.destx, self.desty = next, x, y
    def searchback(self):
        for i in range(self.destin - 1):
            for e in [[self.destx, self.desty - 1], [self.destx + 1, self.desty], [self.destx, self.desty + 1], [self.destx - 1, self.desty]]:
                self.findback(e[0], e[1])
        return self.destx, self.desty
    def findback(self, x, y):
        place = self.pole[y][x]
        if place == self.znaky[self.destin - 1]:
            self.pole[y][x] = "X"
            self.destin, self.destx, self.desty = self.destin - 1, x, y

    def  into_sector(self, x, y):
        pass
    def sector(self, x, y):
        pass
        #divide map into sectors 'big tiles' for easier searching
        #it will have it's own map (n times smaller that the original one)
        #in this map it will search like in normal one
        #so way from A to B is thrue your tile to sector tile wich leads to other sector tile that in the end leads to final sector
        #sector will have entrace for example:
    #   111111    111111
    #   1....1    1....1
    #   1....1    1....1
    #   1....1    1...@@
    #   1....1    1..@.2
    #   111111    111@22
        #which could change into
    #    1          1
    #   1.1        1.12
    #    1          12

    #patcs?

mapa = Map(20, 11)

#kameny a body
kameny = randint(int(mapa.x*mapa.y/20), int(mapa.x*mapa.y/2))
for i in range(kameny):
    mapa.pole[randint(0, mapa.y-1)][randint(0, mapa.x-1)] = "@"
mapa.pole.append(["@"]*mapa.x)
mapa.pole.insert(0, ["@"]*mapa.x)
mapa.x, mapa.y = mapa.x + 2, mapa.y + 2
for i in range(mapa.y):
    mapa.pole[i].append("@")
    mapa.pole[i].insert(0, "@")
c, d = randint(1, mapa.y-2), randint(1, mapa.x-2)
mapa.pole[c][d] = "A"
mapa.q.put((0, d, c))
print(d, c)
while True:
    a, b = randint(1, mapa.y-2), randint(1, mapa.x-2)
    if mapa.pole[a][b] != "A":
        mapa.pole[a][b] = "B"
        break

#znaky k hledání
mapa.znaky.extend(list(string.ascii_lowercase))
for i in range(mapa.x*mapa.y):
    mapa.znaky.append(str(i))

#samotné spuštění
mapa.show()
mapa.search()
mapa.show()
if mapa.done:
    print(mapa.searchback())
else:
    print("Runrand")
mapa.show()
print(mapa.destx, mapa.desty)

input()