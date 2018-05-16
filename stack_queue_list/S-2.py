#!/usr/bin/env python3

# Quiz url
# http://bbs.codeaha.com/problem-12013.html

# read
L = list(input())

# init stack
# attention floor division
length = len(L)
mid = length // 2
stack = L[:mid]

# anthor part
if (length & 1):
    L = L[mid+1:]
else:
    L = L[mid:]

# match
flag = 'YES'
for x in L:
    if x != stack.pop():
        flag = 'NO'
        break

print(flag)

'''
Sample:
ahaha           <= input
YES

But, in python, when we got stack and anthor part, we can
# ----------------- codes goes to -----------------
# ATTENTION: L.reverse() returns None!
L.reverse()
if L == stack:
    print('YES')
else:
    print('NO')
# ---------------- codes ends here ----------------
COOOOL : )
'''
