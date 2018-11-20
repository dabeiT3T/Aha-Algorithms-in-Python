#!/usr/bin/env python3
'''
6 9             <= vertices, edges
1 2 1           <= G
1 3 12
2 3 9
2 4 3
3 5 5
4 3 4
4 5 13
4 6 15
5 6 4
0 1 8 4 13 17   <= print answer

# Dijkstra is used to get the shortest path
# of one specified vertex
# with positive weight.
# here we use adjacency list with array
# (which is list in python).
# 
# G                     first       _next
# 0 => (0, 1, 1)        1           None
# 1 => (0, 2, 12)       3           0
# 2 => (1, 2, 9)        4           None
# 3 => (1, 3, 3)        7           2
# 4 => (2, 4, 5)        8           None
# 5 => (3, 2, 4)        None        None
# 6 => (3, 4, 13)                   5
# 7 => (3, 5, 15)                   6
# 8 => (4, 5, 4)                    None
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

print(G)
print(first)
print(_next)
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

# dis
dis = [float('inf') for x in range(_vertex)]
dis[startVertex] = 0
# init startVertex's dis
for u, v, w in readNodes(startVertex):
    dis[v] = w

# vertices which are not confirmed
confirmed = [0 for i in range(_vertex)]
confirmed[startVertex] = 1

while not all(confirmed):
    # find the shortest weight but not confirmed
    shortest = float('inf')
    shortestVertex = startVertex
    for vertex, weight in enumerate(dis):
        if not confirmed[vertex] and weight < shortest:
            shortest = weight
            shortestVertex = vertex

    # others are infinate
    if shortestVertex == startVertex:
        break

    # let's track shortestVertex
    confirmed[shortestVertex] = 1

    for u, vertex, weight in readNodes(shortestVertex):
        if weight+dis[shortestVertex] < dis[vertex]:
            dis[vertex] = weight + dis[shortestVertex]

# print answer
print(*dis)
