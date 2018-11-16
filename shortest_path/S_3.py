#!/usr/bin/env python3
'''
5 5             <= vertices, edges
2 3 2           <= G
1 2 -3
1 5 5
4 5 2
3 4 3
0 -3 -1 2 4     <= print answer

# Bellman-For is used to the shortest path
# of one specified vertex
# with both positive and negative weight.
'''

# read
_vertex, _edge = map(int, input().split())
# init Graph
G = []
for i in range(_edge):
    u, v, w = map(int, input().split())
    G.append((u-1, v-1, w))

# suppose starting vertex
startVertex = 0
# starting shortest weight to other vertices
dis = [float('inf') if i != startVertex else 0 for i in range(_vertex)]

for i in range(_vertex-1):
    changed = False
    for u, v, w in G:
        if dis[v] > dis[u] + w:
            dis[v] = dis[u] + w
            changed = True
    if not changed:
        break

# for u, v, w in G:
#     if dis[v] > dis[u] + w:
#         print('Negative weight circuit!')
#         break

print(*dis)
