#!/usr/bin/env python3
'''
3                       <= input
123                     <= permutations
132
213
231
312
321
# it may spend more than 1s when enter 9 :(
  yes, it costs 0.71067s on my computer,
  on 1.6Ghz processor
  when output redirects to a file.
  
# but on server, on 2.50GHz processor
  it costs only 0.43s
  when output redirects to a file.
'''

# Quiz url
# http://bbs.codeaha.com/problem-12031.html

# import time
# start = time.clock()

# read
n = int(input())

# recursion
def recursion(s):
    # end of recursion
    if len(s) == 1:
        return [s]

    # get one char
    c = s[-1]
    # get s[:-1] permutations
    T = recursion(s[:-1])
    L = []
    for item in T:
        for x in range(len(item)+1):
            L.append(item[:x]+c+item[x:])
    return L

# number string
S = ''
for x in range(n):
    S += chr(ord('1')+x)
# get answer
L = recursion(S)
L.sort()

# print
for x in L:
    print(x)
    
# end = time.clock()
# print(end-start)
