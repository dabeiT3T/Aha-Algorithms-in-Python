#!/usr/bin/env python3
'''
6 5             <= nodes, edges
1 4             <= G
1 5
2 5
2 6
3 4
3               <= print answer
# use adjacency list instead.
'''

# add elements to adjacency list
def addToAdjcencyList(u, v) -> None:
    G.append((u, v))
    if first[u] != None:
        nextL.append(first[u])
        first[u] = len(G) - 1 
    else:
        first[u] = len(G) - 1 
        nextL.append(None)

# travel the adjacency list
def travelList(node: int) -> int:
    index = first[node]
    if first[node] != None:
        yield G[index]
    else:
        # avoid next[None]
        return None

    while nextL[index] != None:
        yield G[nextL[index]]
        index = nextL[index]

# deep first search
def dfs(node: int) -> bool:

    for u, v in travelList(node):
        if not used[v]:
            used[v] = 1
            if not hasMatched[v] or dfs(hasMatched[v]):
                hasMatched[node] = v
                hasMatched[v] = node
                return True
    return False


# def main():
# read
_nodes, _edges = map(int, input().split())
# init adjacency list
first = [None for i in range(_nodes)]
G = []
nextL = []

for i in range(_edges):
    u, v = map(lambda x: int(x)-1, input().split())
    addToAdjcencyList(u, v)
    addToAdjcencyList(v, u)

# success
total = 0
# match couple
hasMatched = [0] * _nodes
for i in range(_nodes):
    # used node
    used = [0] * _nodes
    if (dfs(i)): total += 1

# print answer
print(total)
