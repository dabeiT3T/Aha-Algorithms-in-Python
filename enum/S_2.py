#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
13 13               <= input
#############
#GG.GGG#GGG.#
###.#G#G#G#G#
#.......#..G#
#G#.###.#G#G#
#GG.GGG.#.GG#
#G#.#G#.#.###
##G...G.....#
#G#.#G###.#G#
#...G#GGG.GG#
#G#.#G#G#.#G#
#GG.GGG#G.GG#
#############
将炸弹放置在(9, 9), 最多可以消灭8个敌人
                    <= print answer
'''

# Quiz url
# https://bbs.codeaha.com/problem-12033.html

# read
row, col = map(int, (input().split()))
M = []
for x in range(row):
    M.extend([list(input())])

# enum
maxmons = r = c = 0
for i in range(1, row-1):
    for j in range(1, col-1):
        # if flat
        if M[i][j] == '.':
            mons = 0
            # up
            # u'd better use nomarl loop, here just practice list parsing
            for x in [L[j] for (tc, L) in enumerate(M) if tc < i][::-1]:
                if x == '#':
                    break
                if x == 'G':
                    mons += 1

            # down
            for x in [L[j] for (tc, L) in enumerate(M) if tc > i]:
                if x == '#':
                    break
                if x == 'G':
                    mons += 1

            # left
            for x in M[i][j-1:0:-1]:
                if x == '#':
                    break
                if x == 'G':
                    mons += 1

            # right
            for x in M[i][j+1:-1]:
                if x == '#':
                    break
                if x == 'G':
                    mons += 1

            # update
            if mons > maxmons:
                maxmons = mons
                r = i
                c = j

# print
utf8stdout = open(1, 'w', encoding='utf-8')
print('将炸弹放置在(%d, %d), 最多可以消灭%d个敌人'%(r, c, maxmons), file=utf8stdout)
