#!/usr/bin/env python3
'''
6 6             <= nodes, edges
1 4             <= G
1 3
4 2
3 2
2 5
5 6
2               <= print answer

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
def dfs(current: int, father: int) -> None:
    global index
    child = 0
    index += 1

    num[current] = low[current] = index

    for (u, v) in travelList(current):
        # node v has not passed through
        if not num[v]:
            child += 1
            dfs(v, current)
            low[current] = min(low[current], low[v])
            # judge cut point
            if num[current] < low[v]:
                # cuts += [current] needs to use global
                cuts.append((current+1, v+1))
        elif v != father:
            low[current] = min(low[current], num[v])


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

# timestamp
num = [0] * _nodes
# low = num[:]
low = [0] * _nodes
# cut edges
cuts = []
# suppose root
root = 0
index = 0
dfs(root, root)
# print
print(*(str(u)+'-'+str(v) for u, v in cuts), sep='\n')
