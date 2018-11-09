#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
10 10
1 2 1 0 0 0 0 0 2 3 <= row, col, start x, y
3 0 2 0 1 2 1 0 1 2 <= map
4 0 1 0 1 2 3 2 0 1
3 2 0 0 0 1 2 4 0 0
0 0 0 0 0 0 1 5 3 0
0 1 2 1 0 1 5 4 3 0
0 1 2 3 1 3 6 2 1 0
0 0 3 4 8 9 7 5 0 0
0 0 0 3 7 8 6 0 1 2
0 0 0 0 0 0 0 0 1 0
                    <= print answer
-1 -1 -1  0  0  0  0  0 -2 -2 
-1  0 -1  0 -3 -3 -3  0 -2 -2 
-1  0 -1  0 -3 -3 -3 -3  0 -2 
-1 -1  0  0  0 -3 -3 -3  0  0 
 0  0  0  0  0  0 -3 -3 -3  0 
 0 -3 -3 -3  0 -3 -3 -3 -3  0 
 0 -3 -3 -3 -3 -3 -3 -3 -3  0 
 0  0 -3 -3 -3 -3 -3 -3  0  0 
 0  0  0 -3 -3 -3 -3  0 -4 -4 
 0  0  0  0  0  0  0  0 -4  0 
有4个小岛

# solving another problem in this section
# count islands and fill color
'''

n, m = map(int, input().split())
M = [list(map(int, input().split())) for i in range(n)]
# no need to record that elements have checked
# count islands
_c = 0
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
def dfs(x: int, y: int) -> None:
    # global M
    M[x][y] = -_c
    # each dirction
    for dx, dy in D:
        tx = x + dx
        ty = y + dy
        # out of range
        if tx < 0 or tx >= n or ty < 0 or ty >= m:
            continue
        # has passed or not a road
        if M[tx][ty] > 0:
                dfs(tx, ty)

for row in range(n):
    for col in range(m):
        if M[row][col] > 0:
            _c += 1
            dfs(row, col)

# print
for row in M:
    for col in row:
        print('%2d '%(col), end='')
    print()

utf8stdout = open(1, 'w', encoding='utf-8')
print('有%d个小岛'%(_c), file=utf8stdout)
