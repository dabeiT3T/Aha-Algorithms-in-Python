#!/usr/bin/env python3
'''
6 9             <= nodes, edges
2 4 11          <= G
3 5 13
4 6 3
5 6 4
2 3 6
4 5 7
1 2 1
3 4 9
1 3 2
19              <= print answer
'''

# read
_nodes, _edges = map(int, input().split())
# read G and save in array(list)
G = [
    [float('inf') if col != row else 0 for col in range(_nodes)]
    for row in range(_nodes)
]
for i in range(_edges):
    u, v, w = map(int, input().split())
    G[u-1][v-1] = w
    G[v-1][u-1] = w

# suppose root
root = 0
# dis
dis = G[root]
# total
total = 0

for i in range(_nodes-1):
    # find the shortest path
    shortest = 0
    minValue = float('inf')
    for key, value in enumerate(dis):
        if value and value < minValue:
            shortest = key
            minValue = value

    total += minValue
    dis[shortest] = 0

    # relation
    for key, value in enumerate(G[shortest]):
        if value < dis[key]:
            dis[key] = value

# print
print(total)