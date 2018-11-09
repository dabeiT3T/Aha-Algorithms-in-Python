#!/usr/bin/env python3
'''
5 4             <= row, col, start x, y
5 3 5 3         <= map
1 5 3 0
2 3 5 1
6 1 1 5
1 5 5 4
                <= print answer
(1, 1) (1, 2) (2, 2) (3, 2) (3, 3) (3, 4) (4, 4) (5, 4)

# <Learning Python> says,
# u can use dict instead of switch
# which python does not include
# btw, nintendo switch is terrific : )
'''

# Quiz url
# https://bbs.codeaha.com/problem-12023.html

# read
n, m = map(int, input().split())
M = [list(map(int, input().split())) for i in range(n)]
# road has passed
L = [[0] * m for i in range(n)]
# path
P = []
# pipe-in direction
D = {
    'left': 1,
    'up': 2,
    'right': 3,
    'down': 4
}
# flag
_f = False


# function
def dfs(x: int, y: int, direct: int) -> None:
    global _f
    # get the target
    if x == n-1 and y == m:
        _f = True
        print(*P)
        return None

    # out of range
    if x < 0 or x >= n or y < 0 or y >= m:
        return None

    if L[x][y]:
        return

    L[x][y] = 1
    # the index in book start from 1
    P.append((x+1, y+1))

    if (M[x][y] > 4):
        ls = F['straight'][direct]
    else:
        ls = F['curve'][direct]

    for l in ls:
        l(x, y)

    L[x][y] = 0
    P.pop()

# lambda dict
# just for fun
F = {
    'straight': {
        D['left']: [
            lambda x, y: dfs(x, y+1, D['left']),
        ],
        D['up']: [
            lambda x, y: dfs(x+1, y, D['up']),
        ],
        D['right']: [
            lambda x, y: dfs(x, y-1, D['right']),
        ],
        D['down']: [
            lambda x, y: dfs(x-1, y, D['down']),
        ],
    },
    'curve': {
        D['left']: [
            lambda x, y: dfs(x+1, y, D['up']),
            lambda x, y: dfs(x-1, y, D['down']),
        ],
        D['up']: [
            lambda x, y: dfs(x, y+1, D['left']),
            lambda x, y: dfs(x, y-1, D['right']),
        ],
        D['right']: [
            lambda x, y: dfs(x-1, y, D['down']),
            lambda x, y: dfs(x+1, y, D['up']),
        ],
        D['down']: [
            lambda x, y: dfs(x, y+1, D['left']),
            lambda x, y: dfs(x, y-1, D['right']),
        ],
    },
}

dfs(0, 0, D['left'])

# print
if not _f:
    print('impossible')
