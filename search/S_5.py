#!/usr/bin/env python3
'''
10 10 6 8
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
38                  <= print answer
# solving this problem with bfs
'''

# Quiz url
# https://bbs.codeaha.com/problem-12035.html

# input
n, m, sx, sy = map(int, input().split())
M = [list(map(int, input().split())) for i in range(n)]
# now we use dict instead of list to record roads have passed
# eg. L[(6, 8)] = True
# or use L = [[0] * m for i in range(n)]
L = {}
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
# area
A = 0

# function
def bfs() -> None:
    global Q, A
    while Q:
        (x, y), *Q = Q
        A += 1
        # each dirction
        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            # out of range
            if tx < 0 or tx >= n or ty < 0 or ty >= m:
                continue
            # has passed or not a road
            if not L.get((tx, ty)) and M[tx][ty] != 0:
                Q.append((tx, ty))
                L[(tx, ty)] = True

# init
L[(sx, sy)] = True
Q = [(sx, sy)]
bfs()

print(A)
