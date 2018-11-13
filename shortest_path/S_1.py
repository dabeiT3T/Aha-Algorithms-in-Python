#!/usr/bin/env python3
'''
4 8             <= vertices, edges
1 2 2           <= G
1 3 6
1 4 4
2 3 3
3 1 7
3 4 1
4 1 5
4 3 12

0 2 5 4         <= print answer
9 0 3 4
6 8 0 1
5 7 10 0

# Floyd-Warshall is used to get the shortest path
# between any two vertices
# with positive weight
'''

# read
_vertex, _edge = map(int, input().split())
# init Graph
G = [
    [0 if i == j else float('inf') for j in range(_vertex)]
    for i in range(_vertex)
]
# get weight
for i in range(_edge):
    x, y, weight = map(lambda n: int(n)-1, input().split())
    G[x][y] = weight + 1

# Floyd-Warshall O(N^3)
for n in range(_vertex):
    for i in range(_vertex):
        for j in range(_vertex):
            if G[i][n]+G[n][j] < G[i][j]:
                G[i][j] = G[i][n] + G[n][j]

# print
for row in G:
    print(*row)
