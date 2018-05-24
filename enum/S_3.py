#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
18                      <= input n <= 24
0+4=4                   <= print answer
0+11=11
1+10=11
2+2=4
2+7=9
4+0=4
7+2=9
10+1=11
11+0=11
一共可以拼出9个不同的等式
'''

# read
n = int(input()) - 4

L = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def fun(x):
    num = 0
    while x//10:
        num += L[x%10]
        x = int(x / 10)
    else:
        num += L[x]
    return num

sum = 0
for a in range(1112):
    for b in range(1112):
        c = a + b
        if fun(a) + fun(b) + fun(c) == n:
            print('%d+%d=%d'%(a, b, c))
            sum += 1

utf8stdout = open(1, 'w', encoding='utf-8')
print('一共可以拼出%d个不同的等式' % sum, file=utf8stdout)
