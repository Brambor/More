from random import randint
from time import sleep
import queue

class Map():
    def __init__(self, y, x):
        self.x, self.y = x, y
        self.objs, self.corpses, self.grass, self.stone, self.ID = [], [], [], [], 0
        self.wait = randint(1, 10)
        self.znaky = ["$"]
        for i in range(self.x*self.y):
            self.znaky.append(str(i))
    def add(self, obj):
        self.objs.append(obj)
        self.ID += 1
    def addc(self, obj):
        self.corpses.append(obj)
    def addg(self, obj):
        self.grass.append(obj)
    def adds(self, obj):
        self.stone.append(obj)
    def draw(self):
        x, y = self.x, self.y
        pole = []
        for i in range(x):
            pole.append([])
            pole[i].extend([" "]*y)
        
        for obj in self.grass:
            pole[obj.y][obj.x] = obj.znak
            
        for obj in self.stone + self.corpses:
            pole[obj.y][obj.x] = obj.znak
            
        for obj in self.objs:
            pole[obj.y][obj.x] = obj.znak #str(obj.ID)
        
        for i in range(x):
            pole[i] = "".join(pole[i])
        pole = "\n".join(pole)
        print()
        print(pole, end = "")
    def update(self):
        for obj in self.objs + self.grass + self.corpses:
            obj.update()
        self.wait -= 1
        if self.wait == 0:
            self.wait = randint(1, 10)
            self.addg(Grass(randint(1, self.x - 2), randint(1, self.y - 2), self))
        
class Sprite():
    def __init__(self, znak, y, x, mapa):
        self.y, self.x = y, x
        self.znak = znak
        self.mapa = mapa
        self.hungry = 50
        self.priority = "eat"
    def move(self):
        pass            
    def closest(self, ents):
        far = mapa.x * mapa.y
        for i in range(len(ents)):
            nfar = abs(ents[i].x - self.x) + abs(ents[i].y - self.y)
            if nfar < far:
                far = nfar
                self.target = ents[i]
    def runto(self):
        ax = abs(self.x - self.target.x)
        ay = abs(self.y - self.target.y)
        if ax + ay == 1:
            return None        
        if ax >= ay:
            go = (1, 0)
            if self.x > self.target.x:
                go = (-1, 0)
        else:
            go = (0, 1)        
            if self.y > self.target.y:
                go = (0, -1)
        return (self.x + go[0], self.y + go[1])
    def runrand(self, beh):
        if beh < 25:
            return (self.x, self.y - 1)
        elif 25 <= beh and beh < 50:
            return (self.x + 1, self.y)
        elif 50 <= beh and beh < 75:
            return (self.x, self.y + 1)
        elif 75 <= beh and beh < 100:
            return (self.x - 1, self.y)
    def hunger(self):
        self.hungry -= 2
        if self.hungry <= 0:
            self.mapa.addc(Corpse(self.y, self.x, mapa, self.food))
            self.mapa.objs.remove(self)
        elif self.hungry < 250:
            self.priority = "eat"
    def eat(self, eatit, toeat):
        for obj in self.mapa.corpses + self.mapa.grass:
            if abs(self.x - obj.x) + abs(self.y - obj.y) == 1 and eatit == obj.znak:
                if toeat == 0:
                    return True
                if toeat > obj.food:
                    toeat = obj.food
                obj.food -= toeat
                self.hungry += toeat
                if self.hungry >= 350:
                    self.priority = "augment"
                return
    def validate(self, goto):
        gut = True
        for obj in self.mapa.objs + self.mapa.corpses + self.mapa.stone:
            if goto[0] == obj.x and goto[1] == obj.y:
                gut = False
        return gut
    def update(self):
        newpos = self.move()
        if newpos == None:
            pass
        elif self.validate(newpos) == True:
            self.x, self.y = newpos
    def search(self, dest, passit):
        self.q, self.done, self.znaky, self.index = queue.Queue(), False, ["A"], 0
        self.pole = []
        self.q.put((0, self.y, self.x))
        for i in range(self.mapa.y):
            self.pole.append([])
            self.pole[i].extend([" "]*self.mapa.x)
        for obj in self.mapa.grass:
            self.pole[obj.x][obj.y] = obj.znak
        for obj in self.mapa.stone + self.mapa.corpses:
            self.pole[obj.x][obj.y] = obj.znak
        for obj in self.mapa.objs:
            self.pole[obj.x][obj.y] = obj.znak + str(obj.ID)
        self.pole[self.x][self.y] = "$"
        if self.searchthere(dest, passit):
            return self.searchback()
        return None
    def searchthere(self, dest, passit):
        while not self.done:
            if not self.q.empty():
                me, x, y = self.q.get()
                for pos in [[x, y - 1], [x + 1, y], [x, y + 1], [x - 1, y]]:
                    self.searchit(pos[0], pos[1], me + 1, dest, passit)
            else:
                return False
        return True
    def searchit(self, x, y, next, dest, passit):
        place = self.pole[y][x]
        if place in passit:
            self.pole[y][x] = self.mapa.znaky[next]
            self.q.put((next, x, y))
        elif place in dest:
            self.done = True
            self.destin, self.destx, self.desty = next, x, y
    def searchback(self):
        for i in range(self.destin - 1):
            for e in [[self.destx, self.desty - 1], [self.destx + 1, self.desty], [self.destx, self.desty + 1], [self.destx - 1, self.desty]]:
                self.findback(e[0], e[1])
        return self.desty, self.destx
    def findback(self, x, y):
        place = self.pole[y][x]
        if place == self.mapa.znaky[self.destin - 1]:
            self.pole[y][x] = "X"
            self.destin, self.destx, self.desty = self.destin - 1, x, y
    def augment(self, znak, close = False):
        for obj in self.opposites:
            if abs(self.x - obj.x) + abs(self.y - obj.y) == 1:
                if close:
                    return True
                self.hungry, obj.hungry = self.hungry - 200, obj.hungry - 200
                self.priority, obj.priority = ["eat"]*2
                mapa.add(Sheep(self.y, self.x, self.mapa.ID, mapa))
                return

class Dog(Sprite):
    def __init__(self, y, x, ID, mapa):
        super().__init__("P", y, x, mapa)
        self.ID = ID
        self.food = 20
        self.hungry = 100
    def move(self):
        self.hunger()
        goto = None
        if self.priority == "eat":
            if self.eat("C", 0):
                self.eat("C", 10)
            else:
                sheeps = list(filter(lambda obj: obj.znak == "O", self.mapa.objs))
                corpses = self.mapa.corpses
                if len(corpses) + len(sheeps) == 0:
                    beh = randint(0, 150)
                    goto = self.runrand(beh)
                else:
                    gofor = corpses
                    if len(corpses) == 0:
                        gofor = sheeps
                    self.closest(gofor)
                    goto = self.runto()
                    if goto == None:
                        self.mapa.addc(Corpse(self.target.y, self.target.x, self.mapa, self.target.food))
                        self.mapa.objs.remove(self.target)
        else:
            beh = randint(0, 175)
            goto = self.runrand(beh)
        print("P[" + str(self.x) + ",", str(self.y), end = "] ")
        return goto

class Sdog(Sprite):
    def __init__(self, y, x, mapa):
        super().__init__("p", y, x, mapa)
        self.evo = 5
        self.food = 10
    def move(self):
        self.hunger()
        self.evo -= 1
        if self.evo == 0:
            self.mapa.add(Dog(self.y, self.x, mapa))
            self.mapa.objs.remove(self)
            return
        beh = randint(0, 400)
        self.runrand(beh)
        print("p[" + str(self.x) + ",", str(self.y), end = "] ")

class Sheep(Sprite):
    def __init__(self, y, x, ID, mapa):
        super().__init__("O", y, x, mapa)
        self.ID = ID
        self.food = 400
        self.eatthat = 5
        self.run = 200
    def move(self):
        self.hunger()
        goto = None
        if self.priority == "eat":
            if self.eat(".", 0):
                self.eat(".", self.eatthat)
                goto = True
            else:
                gofor = self.mapa.grass
                if len(gofor) != 0:
                    goto = self.search(["."], [" "])
        elif self.priority == "augment":
            self.opposites = list(filter(lambda obj: obj.znak == "O" and obj.priority == "augment" and self.ID != obj.ID, self.mapa.objs))
            if len(self.opposites) > 0:
                if self.augment("O", True):
                    self.augment("O")
                else:
                    goto = self.search([opp.znak + str(opp.ID) for opp in self.opposites], [" ", "."])
        if goto == True:
            goto = None
        elif goto == None:
            beh = randint(0, self.run)
            goto = self.runrand(beh)
        #print("O[" + str(self.x) + ",", str(self.y) + "]", end = str(self.hungry)+", ")
        print(self.ID, self.hungry, end = ", ")
        return goto

class Ssheep(Sheep):
    def __init__(self, y, x, mapa):
        super().__init__("o", y, x, mapa)
        self.food = 15
        self.run = 250
        self.eatthat = 4

class Corpse(Sprite):
    def __init__(self, y, x, mapa, food):
        super().__init__("C", y, x, mapa)
        self.food = food
    def move(self):
        if self.food == 0:
            self.mapa.corpses.remove(self)
        return None

class Grass(Sprite):
    def __init__(self, y, x, mapa):
        super().__init__(".", y, x, mapa)
        self.food = 5
    def move(self):
        if self.food == 0:
            self.mapa.grass.remove(self)
            return None
        else:
            self.food += 1
            return None

class Stone(Sprite):
    def __init__(self, y, x, mapa):
        super().__init__("@", y, x, mapa)


mapa = Map(60, 13)

for i in range(2):
    mapa.add(Dog(randint(1, mapa.x-2), randint(1, mapa.y -2), mapa.ID, mapa))
    
for i in range(5):
    mapa.add(Sheep(randint(1, mapa.x-2), randint(1, mapa.y -2), mapa.ID, mapa))
    
for i in range(50):
    mapa.addg(Grass(randint(1, mapa.x-2), randint(1, mapa.y -2), mapa))

for i in range(mapa.y):
    mapa.adds(Stone(0, i, mapa))
    mapa.adds(Stone(mapa.x - 1, i, mapa))
for i in range(1, mapa.x - 1):
    mapa.adds(Stone(i, 0, mapa))
    mapa.adds(Stone(i, mapa.y -1, mapa))

from time import time
mapa.update()
mapa.draw()
sleep(1.5)
i = 1
a = time()
while True:
    wait = time()
    mapa.update()
    print(i, int(time() - a), end = "")
    mapa.draw()
    waitfor = 0.1 - time() + wait
    if waitfor > 0:
        sleep(waitfor)
    i += 1
#for obj in mapa.objs:
#    print(mapa.objs.index(obj))
