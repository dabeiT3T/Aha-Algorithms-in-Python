#!/usr/bin/env python3
'''
# it is worse than S_4 in enum when enter 9 :(
  and, it costs 5.104963s on my computer,
  on 1.6Ghz processor
  when output redirects to a file.
  
# but on server, on 2.50GHz processor
  it costs only 3.43s
  when output redirects to a file.
# it seems my method is better :)
'''

# Quiz url
# http://bbs.codeaha.com/problem-12031.html

# import time
# start = time.clock()

# read
n = int(input())

L = [0] * n
box = [0] * n

# function
def dfs(depth):
    # end
    if depth == n:
        for i in box:
            print(i, sep='', end='')
        print()

        return None

    # get one number
    for x in range(n):
        if not L[x]:
            box[depth] = x+1
            L[x] = 1
            dfs(depth+1)
            L[x] = 0

    return None

dfs(0)

# end = time.clock()
# print(end-start)
