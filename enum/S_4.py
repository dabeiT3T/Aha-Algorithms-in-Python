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
  yes, it costs 0.727735s on my computer,
  on 1.6Ghz processor
  when output redirects to a file.
  
# but on server, on 2.50GHz processor
  it costs only 0.42s
  when output redirects to a file.
# algorithm
  if n == 1, just print 1;
  if n == 2, we have 2, and we have 1's permutations,
  put 2 to 1's left, middle and right:
  that is, 21 and 12;
  if n == 3, we have 3, and we have (1 and 2)'s permutations,
  put 3 to each permutation's left, middle and right:
  to 21 => 321, 231, 213
  to 12 => 312, 132, 123
  if n == 4, yes, we have 4 and we have (1, 2 and 3)'s permutations
  u are right, it's recursion.
  n's permutations =    |- 1 (n = 1)
                        |_ put n to left, middle, right 
                            of each (n-1)'s permutation (n > 1)
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
for x in range(1, n+1):
    S += str(x)
# get answer
L = recursion(S)
L.sort()

# print
for x in L:
    print(x)
    
# end = time.clock()
# print(end-start)
