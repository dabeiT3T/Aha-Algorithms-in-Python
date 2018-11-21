#!/usr/bin/env python3
'''
5 7                 <= vertices, edges
1 2 2               <= G
1 5 10
2 3 3
2 5 7
3 4 4
4 5 5
5 3 6
0 2 5 9 9           <= print answer

# Bellman-Ford optimized with queue.
# here we use adjacency matrix.
'''

# read
_vertex, _edge = map(int, input().split())
# G
G = []
for i in range(_edge):
    u, v, w = map(int, input().split())
    G.append((u-1, v-1, w))

# suppose starting vertex
startVertex = 0
# starting shortest weight to other vertices
dis = [float('inf') if i != startVertex else 0 for i in range(_vertex)]
# stack
L = []

#init
L.append(startVertex)

while L:
    vertex, *L = L
    # or in [(u, v, w) for u, v, w if u == vertex]
    for u, v, w in G:
        if u == vertex:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                if v not in L:
                    L.append(v)

# print
print(*dis)
