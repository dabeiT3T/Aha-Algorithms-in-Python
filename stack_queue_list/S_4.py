#!/usr/bin/env python3
'''
Sample:
9                           <= how many nums
2 3 5 8 9 10 18 26 32       <= nums
6                           <= insert num
2 3 5 6 8 9 10 18 26 32     <= print answer

# In python, we can find the insert position x first and then
  D.insert(x, data)
# Or, use sort
  D.append(data)
  D.sort()
# Or, u can define a class which is more like linked-list
  class LinkedList:
      data = None
      pnext = None

  a = LinkedList()
  b = LinkedList()
  a.data = b.data = 3
  a.pnext = b
  if a.pnext:
      pass
  print(a.pnext.pnext.data)
'''

# Quiz url
# Not Found

# read
n = input()
L = list(map(int, input().split()))
n = int(input())

# dict as linked-list
# but i'd recommend u to use class, see following examples
# head's data is None
head = None
q = head
for data in L:
    # one linked-list
    D = {
        'data': data,
        'next': None,
    }
    # head
    if head:
        q['next'] = D
        q = D
    else:
        q = head = D

# insert n
q = head
while q:
    if not q['next'] or q['next']['data'] > n:
        D = {
            'data': n,
            'next': None,
        }
        D['next'] = q['next']
        q['next'] = D
        break
    # move to next linked-list
    q = q['next']

# print
q = head
while q:
    print(q['data'], end=' ')
    q = q['next']
# new line
print()
