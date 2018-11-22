#!/usr/bin/env python3
'''
14              <= nodes' quantity 
                <= nodes
99 5 36 7 22 17 46 12 2 19 25 28 1 92
                <= print answer
1 2 5 7 12 17 19 22 25 28 36 46 92 99
'''

# read
_nodes = int(input())
# emmmmm, we save a tree in a list :(
T = list(map(int, input().split()))

# function
def siftDown(node: int) -> None:
    global T
    # temp which child node (value) is shorter
    tmp = node;
    # left child node
    if node * 2 <= len(T) and T[node-1] > T[node*2-1]:
        tmp = node * 2
    # right child node
    if (node * 2 + 1) <= len(T) and T[tmp-1] > T[node*2]:
        tmp = node * 2 + 1

    # swap
    if tmp != node:
        T[tmp-1], T[node-1] = T[node-1], T[tmp-1]
        siftDown(tmp)

def createHeap() -> None:
    for i in range(_nodes//2, 0, -1):
        siftDown(i)

def deleteMin() -> int:
    global T
    T[0], T[-1] = T[-1], T[0]
    minNodeValue = T.pop()
    siftDown(1)
    return minNodeValue

# main
createHeap()

for i in range(_nodes):
    print(deleteMin(), end=' ')

print()
