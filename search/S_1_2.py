#!/usr/bin/env python3
'''
# it, dfs, is totally better than S_1 in enum :-O
  here it only costs 1.183098s! Amazing!

# Complexity of S_1 in enum: O(N^9)
'''

# Quiz url
# http://bbs.codeaha.com/problem-12031.html

# import time
# start = time.clock()

n = 9

L = [0] * n
box = [0] * n
total = 0

# function
def dfs(depth):
    global total
    # end
    if depth == n:
        if ((box[0]+box[3])*100 + 
            (box[1]+box[4])*10 +
            box[2]+box[5] == 
            (box[6]*100+box[7]*10+box[8])):
            print('{0[0]}{0[1]}{0[2]}+{0[3]}{0[4]}{0[5]}={0[6]}{0[7]}{0[8]}'.format(box))
            total += 1

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
print('total=%d' % (total/2))

# end = time.clock()
# print(end-start)
