#!/usr/bin/env python3
'''
Sample:
encrypted qq: 631758924     <= encrypted qq
6 1 5 9 4 7 2 8 3           <= print answer
'''

# Quiz url
# http://bbs.codeaha.com/problem-12010.html

# read
# get n, but in python we dont need it
n = input()
L = list(input('encrypted qq: '))

Q = []

while L:
    # del 1st num
    # (why python list has no shift method?)
    n = L.pop(0)
    # this is true qq num
    Q.append(n)
    # pop 1st num, append to the list tail
    if L:
        L.append(L.pop(0))

# decrypted qq
qq = ' '.join(Q)

# print
print(qq)
