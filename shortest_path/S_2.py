#!/usr/bin/env python3
'''
6 9
1 2 1
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
# here we use adjacency matrix.
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
# suppose starting vertex
startVertex = 0
# starting shortest weight to other vertices
# should use copy instead of the pointer
dis = G[startVertex][:]
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

    for vertex, weight in enumerate(G[shortestVertex]):
        if weight+dis[shortestVertex] < dis[vertex]:
            dis[vertex] = weight + dis[shortestVertex]

# print answer
print(*dis)
