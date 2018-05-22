#!/usr/bin/env python3
'''
Sample:
9                           <= how many nums
2 3 5 8 9 10 18 26 32       <= nums
6                           <= insert num
2 3 5 6 8 9 10 18 26 32     <= print answer

# codes in the book may cause bug : )
  U cannot insert num which is either smaller or bigger than any of the nums.
  Because it hasn't defined head.
'''

# Quiz url
# Not Found

# read
n = input()
data = [0] + list(map(int, input().split()))
n = int(input())

# list right used to store point
right = list(range(1, len(data))) + [0]
data.append(n)
index = len(data) - 1
# right[0] represent head
# data  = [0, 1, 2, 3, 4, 5, n]
# right = [1, 2, 3, 4, 5, 0,]
#insert n
q = 0
# if u want u use while-else
# while right[q]:
while True:
    # if u want u use while-else
    # if data[right[q]] > n:
    if not right[q] or data[right[q]] > n:
        right.append(right[q])
        right[q] = index
        break

    q = right[q]
# if u want u use while-else, n is the biggest
# else:
#     right.append(0)
#     right[q] = index

# print
q = 0
while right[q]:
    print(data[right[q]], end=' ')
    q = right[q]
# last one and new line
print()
