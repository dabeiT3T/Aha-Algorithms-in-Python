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
# read G
G = []
for i in range(_edges):
    u, v, w = map(int, input().split())
    # emmmm, G += iteration is different from G.append(iteration)
    # G += 'foo' get ['f', 'o', 'o']
    # equals G.extend('foo')
    G.append((u-1, v-1, w))

# emmmmm, this is a tree
# T[i] is node i's father node
T = [i for i in range(_nodes)]

# function
def quickSort(start, end) -> None:
    if start > end:
        return;

    head = start
    tail = end
    tmp = G[start][2]

    while head != tail:
        # move right pointer
        while G[tail][2] >= tmp and head < tail:
            tail -= 1

        # move left pointer
        while G[head][2] <= tmp and head < tail:
            head +=1

        # exchange
        if head < tail:
            G[head], G[tail] = G[tail], G[head]

    G[start], G[tail] = G[tail], G[start]
    # left
    quickSort(start, head-1)
    # right
    quickSort(tail+1, end)

def getFather(node) -> int:
    if T[node] == node: return node

    T[node] = getFather(T[node])
    return T[node]

def addBranch() -> int:
    total = 0
    count = 0
    for u, v, weight in G:
        fatherU = getFather(u)
        fatherV = getFather(v)

        if fatherU != fatherV:
            T[fatherV] = fatherU
            total += weight
            count += 1

        # as a tree, branches equals nodes - 1
        if count == _nodes - 1:
            break

    return total

# main
quickSort(0, _edges-1)
total = addBranch()
# print
print(total)
