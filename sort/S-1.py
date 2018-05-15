#!/usr/bin/env python3

# read
m = int(input('range (0~m): '))

numbers = input('numbers: ')
L = list(map(int, numbers.split(' ')))

# bucket
S = [0] * (m+1)
# sort
for num in L:
    S[num] += 1
# print
# desc sort
# for i in range(m, -1, -1):
for i in range(m+1):
    for j in range(S[i]):
        print(i, end=' ')

# new line
print('')

'''
Sample:
range (0~m): 1000   <= sort num from 0~1000
numbers: 8 100 50 22 15 6 1 1000 999 0
                    <= nums splited with one space
0 1 6 8 15 22 50 100 999 1000
                    <= print answer

Complexity: O(M+N)
'''
