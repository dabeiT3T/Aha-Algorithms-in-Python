#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
13 13 3 3           <= row, col, start x, y
#############       <= map
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.#.#
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############
将炸弹放置在(7, 11)处，最多可以消灭10个敌人
                    <= print answer

# compared bfs with here dfs on my air, 1.6Ghz processor
# it cost 0.000774s with bfs, while
# it cost 0.000735s with dfs.
'''

# Quiz url
# https://bbs.codeaha.com/problem-12034.html

# read
n, m, sx, sy = map(int, input().split())
M = [list(input()) for x in range(n)]

# import time
# start = time.clock()

# position of max boom
mx = my = mb = 0
# road has passwd
L = [[0] * m for x in range(n)]
# direction
D = [
    # right
    [0, 1],
    # down
    [1, 0],
    # left
    [0, -1],
    # up
    [-1, 0],
]

# function
def getNum(x: int, y: int) -> None:
    global mx, my, mb
    num = 0
    # up
    # put same col elem into list
    # or using (for i for range(y-1, 0, -1): M[y][i])
    for i in [T[y] for k, T in enumerate(M) if k < x and k > 0][::-1]:
        if i == '#':
            break
        elif i == 'G':
            num += 1
    # down
    # or using (for i for range(y+1, n): M[y][i])
    for i in [T[y] for k, T in enumerate(M) if k > x and k < n-1]:
        if i == '#':
            break
        elif i == 'G':
            num += 1
    # left
    # here y cannot be 0
    for i in M[x][y-1:0:-1]:
        if i == '#':
            break
        elif i == 'G':
            num += 1
    # right
    for i in M[x][y+1:-1]:
        if i == '#':
            break
        elif i == 'G':
            num += 1

    if num > mb:
        mb = num
        mx = x
        my = y

def dfs(x: int, y: int) -> None:
    '''
    Depth-First Search
    '''
    getNum(x, y)
    for dx, dy in D:
        tx = x + dx
        ty = y + dy
        # out of range
        if tx < 0 or tx >= n or ty < 0 or ty >= m:
            continue
        # has passed or not a road
        if L[tx][ty] == 0 and M[tx][ty] == '.':
            L[tx][ty] = 1
            dfs(tx, ty)

# init
L[sx][sy] = 1
dfs(sx, sy)

# end = time.clock()
# print(end-start)

# print
utf8stdout = open(1, 'w', encoding='utf-8')
print('将炸弹放置在(%d, %d)处，最多可以消灭%d个敌人'%(mx, my, mb), file=utf8stdout)
