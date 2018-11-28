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

# Prim with adjacency list and heap.
'''

# add elements to adjacency list
def addToAdjcencyList(u, v, w) -> None:
    G.append((u, v, w))
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

# here is some tree func
def siftDown(node: int) -> None:
    # changeable vars
    # global T
    # temp which child node (value) is shorter
    tmp = node;
    # left child node
    if node * 2 <= len(T) and dis[T[node-1]] > dis[T[node*2-1]]:
        tmp = node * 2
    # right child node
    if (node * 2 + 1) <= len(T) and dis[T[tmp-1]] > dis[T[node*2]]:
        tmp = node * 2 + 1

    # swap
    if tmp != node:
        _pos[T[tmp-1]], _pos[T[node-1]] = _pos[T[node-1]], _pos[T[tmp-1]]
        T[tmp-1], T[node-1] = T[node-1], T[tmp-1]
        siftDown(tmp)

def siftUp(node: int) -> None:
    tmp = node;
    # father node
    if node // 2 > 0 and dis[T[node-1]] < dis[T[node//2-1]]:
        tmp = node // 2

    # swap
    if tmp != node:
        _pos[T[tmp-1]], _pos[T[node-1]] = _pos[T[node-1]], _pos[T[tmp-1]]
        T[tmp-1], T[node-1] = T[node-1], T[tmp-1]
        siftUp(tmp)

# def main():
# read
_nodes, _edges = map(int, input().split())
# init adjacency list
first = [None for i in range(_nodes)]
G = []
nextL = []

for i in range(_edges):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    addToAdjcencyList(u, v, w)
    addToAdjcencyList(v, u, w)

# suppose root
root = 0
# init dis
dis = [float('inf')] * _nodes
dis[root] = 0
for u, v, w in travelList(root):
    dis[v] = w
# build tree
T = []
# node's index in T
_pos = []
for i in range(_nodes):
    if i != root:
        _pos += [len(T)]
        T += [i]
    else:
        _pos += [None]

# make it a heap
for i in range(len(T)//2, 0, -1):
    siftDown(i)

# total
total = 0
while T:
    # move largest weight to root
    _pos[T[0]], _pos[T[-1]] =  None, 0
    T[0], T[-1] = T[-1], T[0]
    # pop the smallest node
    *T, vertex = T
    siftDown(1)
    total += dis[vertex]
    dis[vertex] = 0
    for u, v, w in travelList(vertex):
        if w < dis[v]:
            dis[v] = w
            siftUp(_pos[v]+1)

# print
print(total)
