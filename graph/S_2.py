#!/usr/bin/env python3
'''
5 8         <= V, E
1 2 2       <= G (e, w)
1 5 10
2 3 3
2 5 7
3 1 4
3 4 4
4 5 5
5 3 3
9           <= print answer
'''

# import
import math

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
    x, y, w = map(lambda n: int(n)-1, input().split())
    # weight does not need to -1
    G[x][y] = w + 1

# v has passed
L = [0 for i in range(_v)]
# we suppose start, end v
startVertex, endVertex = 1, _v
# min weight
minWeight = float('inf')

# function
def dfs(vertex: int, weight: int) -> None:
    # bigger weight
    global minWeight
    if weight > minWeight:
        return None
    # get the target
    if vertex == endVertex:
        if weight < minWeight:
            minWeight = weight
        return None

    for keyV, w in enumerate(G[vertex-1]):
        if w and math.isfinite(w) and not L[keyV]:
            L[keyV] = 1
            dfs(keyV+1, weight+w)
            L[keyV] = 0


# init
dfs(startVertex, 0)
print(minWeight)
