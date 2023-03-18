from random import randrange

c=0

res = 900
res1 = 1200
size = 30
rad = 240
fps = 10
length = 1
dx, dy = 0, 0

cols, rows = 40, 30
TILE = 30

int0 = 100

# аномалии
anom1 = randrange(0, res1, size), randrange(0, res, size)
anom2 = randrange(0, res1, size), randrange(0, res, size)
anom3 = randrange(0, res1, size), randrange(0, res, size)
anom4 = randrange(0, res1, size), randrange(0, res, size)
anom5 = randrange(0, res1, size), randrange(0, res, size)

# локаторы
lock1 = randrange(0, res1, size), randrange(0, res, size)
lock2 = randrange(0, res1, size), randrange(0, res, size)
lock3 = randrange(0, res1, size), randrange(0, res, size)

# поле зрения
aur1 = lock1[0] - size*10, lock1[1] - size*10
aur2 = lock2[0] - size*10, lock2[1] - size*10
aur3 = lock3[0] - size*10, lock3[1] - size*10