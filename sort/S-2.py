#!/usr/bin/env python3

# read
numbers = input('numbers: ')
L = list(map(int, numbers.split(' ')))

# sort
for i in range(len(L)-1):
    for j in range(len(L)-i-1):
        if L[j] < L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]

# print
# desc sort
# for x in L[::-1]:
for x in L:
    print(x, end=' ')

# new line
print('')

'''
Sample:
numbers: 8 100 50 22 15 6 1 1000 999 0
                    <= nums splited with one space
1000 999 100 50 22 15 8 6 1 0
                    <= print answer

Complexity: O(N*N)
'''