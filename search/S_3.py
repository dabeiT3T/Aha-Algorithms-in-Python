#!/usr/bin/env python3
'''
5 4                 <= n m
0 0 1 0             <= map
0 0 0 0
0 0 1 0
0 1 0 0
0 0 0 1
1 1 4 3             <= start, end x, y
7                   <= print answer

3 3                 <= input
1 1 1 
0 1 0 
0 1 0 
2 1 3 3
No Way!             <= print answer

# codes in the book may cause bugs
  what if start pos equals end pos?
# with python's principle, it is easy to show off : )
  - use lambda instead of def reachTarget
  - (x, y, s), *Q = Q instead of Q.pop(0)
  COOOOOOOOOOOOOOOOOOL
'''

# Quiz url
# https://bbs.codeaha.com/problem-12032.html

# read
n, m = map(int, input().split())
M = [list(map(int, input().split())) for x in range(n)]
# start x,y end x, y
sx, sy, ex, ey = map(lambda x: int(x)-1, input().split())
# road has passed
L = [[0]*m for x in range(n)]
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
def reachTarget(x, y, *o):
    if x == ex and y == ey:
        return True
    else:
        return False

def bfs():
    # if start pos equals end pos
    if reachTarget(*Q[0]):
        return 0
    # bfs
    while Q:
        # get father's info
        (x, y, s), *Q = Q
        # each direction
        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            # out of range
            if tx < 0 or ty < 0 or tx >= n or ty >= m:
                continue
            # cannot pass or has passed
            if M[tx][ty] == 0 and L[tx][ty] == 0:
                Q.append((tx, ty, s+1,))
            # hit
            if reachTarget(tx, ty):
                return s+1
    return None

# init
L[sx][sy] = 1
Q = [(sx, sy, 0)]
minStep = bfs()

# print
print(minStep if minStep != None else 'No Way!')
