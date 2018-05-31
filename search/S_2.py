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

# deep fast search is very interesting
  and i think i can use it in game `picture matching`
  (which is `lianliankan` in chinese) : )
'''

# Quiz url
# http://bbs.codeaha.com/problem-12032.html

# read
n, m = map(int, input().split())
M = [list(map(int, input().split())) for x in range(n)]
# start x,y end x, y
sx, sy, ex, ey = map(lambda x: int(x)-1, input().split())
# min step
minStep = None
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
def dfs(x, y, depth):
    # get it
    if x == ex and y == ey:
        global minStep
        if minStep == None or minStep > depth:
            minStep = depth
        return None
    # loop
    for dx, dy in D:
        # new coordinates
        tx = x + dx
        ty = y + dy
        # out of range
        if tx < 0 or ty < 0 or tx >= n or ty >= m:
            continue
        # road and first pass
        if not M[tx][ty] and not L[tx][ty]:
            L[tx][ty] = 1
            dfs(tx, ty, depth+1)
            L[tx][ty] = 0

L[sx][sy] = 1
dfs(sx, sy, 0)
# print
print(minStep if minStep != None else 'No Way!')
