#!/usr/bin/env python3
'''
5 7 1 5     <= V, E, start, end vertex
1 2         <= G
1 3
2 3
2 4
3 4
3 5
4 5
2           <= print answer
'''

# Quiz url
# https://bbs.codeaha.com/problem-12038.html

# read
_v, _e, startVertex, endVertex = map(int, input().split())
# init G
'''
  0 inf inf
inf   0 inf
inf inf   0
'''
G = [
    [0 if i == j else float('inf') for j in range(_v)]
    for i in range(_v)
]
for i in range(_e):
    x, y = map(lambda n: int(n)-1, input().split())
    G[x][y] = 1
    G[y][x] = 1
# v has passed
L = [0 for i in range(_v)]

# function
def bfs():
    global Q
    while Q:
        (vertex, cnt), *Q = Q
        if vertex == endVertex:
            print(cnt)
            break

        for keyV, edge in enumerate(G[vertex-1]):
            if edge == 1 and not L[keyV]:
                L[keyV] = 1
                Q.append((keyV+1, cnt+1))
    # let's review while-else
    else:
        print('impossible')

# init
L[startVertex-1] = 1
Q = [(startVertex, 0)]
bfs()
