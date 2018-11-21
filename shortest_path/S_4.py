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
# here we use adjacency list with array
# (which is list in python).
'''

# read
_vertex, _edge = map(int, input().split())
# declare
first = [None for i in range(_vertex)]
_next = []
G = []
# read G
for x in range(_edge):
    u, v, w = map(int, input().split())
    # convert index to index starting from 0
    u -=1
    v -=1
    G.append((u, v, w))
    if first[u] != None:
        _next.append(first[u])
    else:
        _next.append(None)
    first[u] = x

# suppose starting vertex
startVertex = 0

# function which to read turple from adjacency list
def readNodes(start:int):
    pointer = start
    # node has a pointer
    if first[pointer] != None:
        yield G[first[pointer]]
    else:
        # avoid _next[None]
        return None
    # pointer move on
    pointer = first[pointer]
    while _next[pointer] != None:
        yield G[_next[pointer]]
        pointer = _next[pointer]

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
    for u, v, w in readNodes(vertex):
        if dis[v] > dis[u] + w:
            dis[v] = dis[u] + w
            if v not in L:
                L.append(v)

# print
print(*dis)
