import pygame
from math import sqrt
from parametrs import *
from collections import deque

pygame.init()

im = pygame.image.load('map.png')  # слово сталкер не нужно если открываешь фаил в пустой рабочей среде

#x, y = randrange(0, res1, size), randrange(0, res, size)
q, w = 0, 0


# локаторы
l1 = pygame.image.load('n.png')
l2 = pygame.image.load('n2.png')
l3 = pygame.image.load('n3.png')

# поле зрения
loud1 = pygame.Surface((size*21, size*21))
loud1.fill((255, 255, 255))
loud1.set_alpha(80)

loud2 = pygame.Surface((size*21, size*21))
loud2.fill((255, 255, 255))
loud2.set_alpha(80)

loud3 = pygame.Surface((size*21, size*21))
loud3.fill((255, 255, 255))
loud3.set_alpha(80)

# шрифт и вывод данных от локаторов
font = pygame.font.SysFont('Arial', 20)
t1 = font.render(str(lock1), True, pygame.Color('darkorange'))
title1 = font.render(('лок 1'), True, pygame.Color('darkorange'))
t2 = font.render(str(lock2), True, pygame.Color('darkorange'))
title2 = font.render(('лок 2'), True, pygame.Color('darkorange'))
t3 = font.render(str(lock3), True, pygame.Color('darkorange'))
title3 = font.render(('лок 3'), True, pygame.Color('darkorange'))


#man = [(x, y)]
st = pygame.image.load('12.png')




surf = pygame.display.set_mode((res1 * 1.5, res))
surf.fill(pygame.Color('black'))



def get_rect(x, y):
    return x * TILE + 1, y * TILE + 1, TILE - 2, TILE - 2


def get_next_nodes(x, y):
    check_next_node = lambda x, y: True if 0 <= x < cols and 0 <= y < rows and not grid[y][x] else False
    ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1],[1,1],[-1, 1]
    return [(x + dx, y + dy) for dx, dy in ways if check_next_node(x + dx, y + dy)]


def get_clikmuse_pos():
    x, y = randrange(0, res1, size), randrange(0, res, size)
    grid_x, grid_y = x // TILE, y // TILE
    pygame.draw.rect(sc, pygame.Color('red'), get_rect(grid_x, grid_y ))
    return (grid_x, grid_y)

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return queue, visited


grid = [[1 if ((col > anom1[0]/TILE-7 and row > anom1[1]/TILE-7) and (col < anom1[0]/TILE+7 and row < anom1[1]/TILE+7) or (
        col > anom2[0]/TILE-7 and row > anom2[1]/TILE-7) and (col < anom2[0]/TILE+7 and row < anom2[1]/TILE+7) or (
        col > anom3[0]/TILE-7 and row > anom3[1]/TILE-7) and (col < anom3[0]/TILE+7 and row < anom3[1]/TILE+7) or (
        col > anom4[0]/TILE-7 and row > anom4[1]/TILE-7) and (col < anom4[0]/TILE+7 and row < anom4[1]/TILE+7) or (
        col > anom5[0]/TILE-7 and row > anom5[1]/TILE-7) and (col < anom5[0]/TILE+7 and row < anom5[1]/TILE+7) ) else 0 for col in range(cols)] for row in range(rows)]
print(grid)
# dict of adjacency lists

r1 = sqrt(((anom1[0] - lock1[0]) / size)**2 + ((anom1[1] - lock1[1]) / size)**2)
int1 = round((int0 / r1**2), 2)
print(int1, r1)

graph = {}
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        if not col:
            graph[(x, y)] = graph.get((x, y), []) + get_next_nodes(x, y)



# BFS settings
start = (q, w)
goal = start
queue = deque([start])
visited = {start: None}
blue = (0, 0, 255)


sc = pygame.Surface([res1, res])
clock = pygame.time.Clock()


while True:
    surf.blit(sc, (0, 0))
    sc.blit(im, (0, 0))
    #sc.fill(pygame.Color('darkorange'))
    sc.blit(loud1, aur1)
    sc.blit(loud2, aur2)
    sc.blit(loud3, aur3)

    sc.blit(l1, lock1)
    sc.blit(l2, lock2)
    sc.blit(l3, lock3)



    #sc.blit(st, (q, w))
    #pygame.display.update()

    [[pygame.draw.rect(sc, pygame.Color('red'), get_rect(x, y))
    for x, col in enumerate(row) if col]for y, row in enumerate(grid)]


    #в этих условиях прописывается что если наша аномалия попадает в зону сканирования какогото из лакаторов то онк подсвечивается красным

    #1 по аномалиям

    if (anom1[0] > lock1[0] - size*5) and (anom1[0] < lock1[0] + size*5) and (anom1[1] > lock1[1] - size*5) and (
            anom1[1] < lock1[1] + size*5):

        tl1 = font.render(('(№ аномалии 1)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 50))

        #pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

        r = sqrt(((anom1[0] - lock1[0]) / size)**2 + ((anom1[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)

        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 50))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 50))


    if (anom1[0] > lock2[0] - size*5) and (anom1[0] < lock2[0] + size*5) and (anom1[1] > lock2[1] - size*5) and (
            anom1[1] < lock2[1] + size*5):

        tl1 = font.render(('(№ аномалии 1)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 350))

        #pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

        r = sqrt(((anom1[0] - lock2[0]) / size)**2 + ((anom1[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)

        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 350))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 350))


    if (anom1[0] > lock3[0] - size*5) and (anom1[0] < lock3[0] + size*5) and (anom1[1] > lock3[1] - size*5) and (
            anom1[1] < lock3[1] + size*5):

        tl1 = font.render(('(№ аномалии 1)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 650))

        #pygame.draw.rect(sc, pygame.Color('red'), (*anom1, size, size))

        r = sqrt(((anom1[0] - lock3[0]) / size)**2 + ((anom1[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)

        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 650))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 650))

    # 2

    if (anom2[0] > lock1[0] - size * 5) and (anom2[0] < lock1[0] + size * 5) and (
            anom2[1] > lock1[1] - size * 5) and (anom2[1] < lock1[1] + size * 5):
        tl1 = font.render(('(№ аномалии 2)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 70))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))
        r = sqrt(((anom2[0] - lock1[0]) / size)**2 + ((anom2[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 70))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 70))


    if (anom2[0] > lock2[0] - size * 5) and (anom2[0] < lock2[0] + size * 5) and (
            anom2[1] > lock2[1] - size * 5) and (anom2[1] < lock2[1] + size * 5):
        tl1 = font.render(('(№ аномалии 2)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 370))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))
        r = sqrt(((anom2[0] - lock2[0]) / size)**2 + ((anom2[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 370))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 370))


    if (anom2[0] > lock3[0] - size * 5) and (anom2[0] < lock3[0] + size * 5) and (
            anom2[1] > lock3[1] - size * 5) and (anom2[1] < lock3[1] + size * 5):
        tl1 = font.render(('(№ аномалии 2)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 670))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom2, size, size))
        r = sqrt(((anom2[0] - lock3[0]) / size)**2 + ((anom2[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 670))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 670))

    #3

    if (anom3[0] > lock1[0] - size * 5) and (anom3[0] < lock1[0] + size * 5) and (
            anom3[1] > lock1[1] - size * 5) and (anom3[1] < lock1[1] + size * 5):
        tl1 = font.render(('(№ аномалии 3)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 90))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))
        r = sqrt(((anom3[0] - lock1[0]) / size)**2 + ((anom3[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 90))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 90))


    if (anom3[0] > lock2[0] - size * 5) and (anom3[0] < lock2[0] + size * 5) and (
            anom3[1] > lock2[1] - size * 5) and (anom3[1] < lock2[1] + size * 5):
        tl1 = font.render(('(№ аномалии 3)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 390))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))
        r = sqrt(((anom3[0] - lock2[0]) / size)**2 + ((anom3[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 390))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 390))


    if (anom3[0] > lock3[0] - size * 5) and (anom3[0] < lock3[0] + size * 5) and (
            anom3[1] > lock3[1] - size * 5) and (anom3[1] < lock3[1] + size * 5):
        tl1 = font.render(('(№ аномалии 3)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 690))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom3, size, size))
        r = sqrt(((anom3[0] - lock3[0]) / size)**2 + ((anom3[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 690))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 690))

    #4

    if (anom4[0] > lock1[0] - size * 5) and (anom4[0] < lock1[0] + size * 5) and (
            anom4[1] > lock1[1] - size * 5) and (anom4[1] < lock1[1] + size * 5):
        tl1 = font.render(('(№ аномалии 4)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 110))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))
        r = sqrt(((anom4[0] - lock1[0]) / size)**2 + ((anom4[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 110))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 110))


    if (anom4[0] > lock2[0] - size * 5) and (anom4[0] < lock2[0] + size * 5) and (
            anom4[1] > lock2[1] - size * 5) and (anom4[1] < lock2[1] + size * 5):
        tl1 = font.render(('(№ аномалии 4)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 410))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))
        r = sqrt(((anom4[0] - lock2[0]) / size)**2 + ((anom4[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 410))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 410))


    if (anom4[0] > lock3[0] - size * 5) and (anom4[0] < lock3[0] + size * 5) and (
            anom4[1] > lock3[1] - size * 5) and (anom4[1] < lock3[1] + size * 5):
        tl1 = font.render(('(№ аномалии 4)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 710))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom4, size, size))
        r = sqrt(((anom4[0] - lock3[0]) / size)**2 + ((anom4[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 710))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 710))

    #5

    if (anom5[0] > lock1[0] - size * 5) and (anom5[0] < lock1[0] + size * 5) and (
            anom5[1] > lock1[1] - size * 5) and (anom5[1] < lock1[1] + size * 5):
        tl1 = font.render(('(№ аномалии 5)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 130))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))
        r = sqrt(((anom5[0] - lock1[0]) / size)**2 + ((anom5[1] - lock1[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 130))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 130))


    if (anom5[0] > lock2[0] - size * 5) and (anom5[0] < lock2[0] + size * 5) and (
            anom5[1] > lock2[1] - size * 5) and (anom5[1] < lock2[1] + size * 5):
        tl1 = font.render(('(№ аномалии 5)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 430))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))
        r = sqrt(((anom5[0] - lock2[0]) / size)**2 + ((anom5[1] - lock2[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 430))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 430))


    if (anom5[0] > lock3[0] - size * 5) and (anom5[0] < lock3[0] + size * 5) and (
            anom5[1] > lock3[1] - size * 5) and (anom5[1] < lock3[1] + size * 5):
        tl1 = font.render(('(№ аномалии 5)'), True, pygame.Color('darkorange'))
        surf.blit(tl1, (1400, 730))
        #pygame.draw.rect(sc, pygame.Color('red'), (*anom5, size, size))
        r = sqrt(((anom5[0] - lock3[0]) / size)**2 + ((anom5[1] - lock3[1]) / size)**2)
        int = round((int0 / r**2), 2)
        intevv = font.render(('Интенсивность :'), True, pygame.Color('darkorange'))
        surf.blit(intevv, (1550, 730))
        outint = font.render(str(int), True, pygame.Color('darkorange'))
        surf.blit(outint, (1690, 730))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    surf.blit(title1, (1250, 50))
    surf.blit(t1, (1300, 50))
    surf.blit(title2, (1250, 350))
    surf.blit(t2, (1300, 350))
    surf.blit(title3, (1250, 650))
    surf.blit(t3, (1300, 650))

    mouse_pos = get_clikmuse_pos()
    if mouse_pos and not grid[mouse_pos[1]][mouse_pos[0]]:
        queue, visited = bfs(start, mouse_pos, graph)
        goal = mouse_pos
        print(mouse_pos)

    path_head, path_segment = goal, goal
    while path_segment and path_segment in visited:
        pygame.draw.rect(sc, pygame.Color('white'), get_rect(*path_segment), TILE, border_radius=TILE // 3)
        path_segment = visited[path_segment]
    pygame.draw.rect(sc, pygame.Color('magenta'), get_rect(*path_head), border_radius=TILE // 3)

    sc.blit(st, (q, w))
    pygame.display.update()

    if c==1:
        pygame.image.save(surf, f'images/map_with_swans.png')
        break


    c+=1
    pygame.display.flip()
    clock.tick(fps)

#
