#!/usr/bin/env python3
'''
Sample:
numbers: 20 40 32 67 40 20 89 300 400 15
                    <= nums splited with one space
8
15 20 32 40 67 89 300 400
                    <= print answer

Complexity: O(NlogN)
'''

# Quiz url
# http://bbs.codeaha.com/problem-12001.html

# This is quick sort
def quickSort(start, end):
    if start > end:
        return

    head = start
    tail = end
    tmp = L[start]

    while head != tail:
        # move right pointer
        while L[tail] >= tmp and head < tail:
            tail -= 1

        # move left pointer
        while L[head] <= tmp and head < tail:
            head +=1

        # exchange
        if head < tail:
            L[head], L[tail] = L[tail], L[head]

    L[start], L[tail] = L[tail], L[start]
    # left
    quickSort(start, head-1)
    # right
    quickSort(tail+1, end)


# read
numbers = input('numbers: ')
# distinct
L = list(set(map(int, numbers.split(' '))))

# sort
quickSort(0, len(L)-1)

# print
print(len(L))
# desc sort
# for x in L[::-1]:
for x in L:
    print(x, end=' ')

# new line
print()
