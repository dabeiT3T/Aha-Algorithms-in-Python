#!/usr/bin/env python3
'''
10 9            <= nodes & clues quantity
1 2             <= clues
3 4
5 2
4 6
2 6
8 7
9 7
1 6
2 4
3               <= print answer
'''

# read summary
_nodes, _clues = map(int, input().split())
# emmmmm, this is a tree
T = [i for i in range(_nodes)]

# function
def getSuperBoss(staff: int) -> int:
    if T[staff] == staff: return staff

    T[staff] = getSuperBoss(T[staff])
    return T[staff]

# read boss and staff
for i in range(_clues):
    boss, staff = map(lambda x: int(x)-1, input().split())
    bossBoss = getSuperBoss(boss)
    staffBoss = getSuperBoss(staff)
    if bossBoss != staffBoss:
        T[staffBoss] = bossBoss

# let's calculate
quantity = 0
for i in range(_nodes):
    if i == T[i]:
        quantity += 1

# print
print(quantity)
