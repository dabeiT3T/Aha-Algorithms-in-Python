#!/usr/bin/env python3

# This is quick sort
def quickSort(start, end):
    if start > end:
        return;

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
L = list(map(int, numbers.split(' ')))

# sort
quickSort(0, len(L)-1)

# print
# desc sort
# for x in L[::-1]:
for x in L:
    print(x, end=' ')

# new line
print('')

'''
Sample:
numbers: 6 1 2 7 9 3 4 5 10 8
                    <= nums splited with one space
1 2 3 4 5 6 7 8 9 10
                    <= print answer

Complexity: O(N*N)
Ave. Complexity: O(NlogN)
'''