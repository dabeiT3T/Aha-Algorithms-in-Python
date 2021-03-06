#!/usr/bin/env python3
'''
5 5         <= V, E
1 2         <= G
1 3
1 5
2 4
3 5
1 2 3 5 4   <= print answer
'''

# read
_v, _e = map(int, input().split())
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
def bfs() -> None:
    global Q
    while Q:
        vertex, *Q = Q
        print(vertex, end=' ')
        for keyV, edge in enumerate(G[vertex-1]):
            if edge == 1 and not L[keyV]:
                L[keyV] = 1
                Q.append(keyV+1)

# init
L[0] = 1
Q = [1]
bfs()
print()
