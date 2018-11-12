#!/usr/bin/env python3
'''
5 5         <= V, E
1 2         <= G
1 3
1 5
2 4
3 5
1 2 4 3 5   <= print answer
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
def dfs(vertex: int) -> None:
    print(vertex, end=' ')
    if vertex == _v:
        return None

    for keyV, edge in enumerate(G[vertex-1]):
        if  edge == 1 and not L[keyV]:
            L[keyV] = 1
            dfs(keyV+1)

# init
L[0] = 1
dfs(1)
print()
