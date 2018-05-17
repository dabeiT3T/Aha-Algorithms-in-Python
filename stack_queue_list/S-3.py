#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Quiz url
# Not Found

# table stack
L = []

# def function for discarding
def discard(player, poker):
    # has same poker
    global L
    if poker in L:
        pos = L.index(poker)
        win = L[pos:]
        win.reverse()
        player += [poker] + win
        L = L[:pos]
    else:
        L.append(poker)

# read
player1 = list(map(int, input().split()))
player2 = list(map(int, input().split()))

# game begin
while player1 and player2:
    # player1 turn
    t = player1.pop(0)
    # judge
    discard(player1, t)

    if not player1: break
    # player2 turn
    t = player2.pop(0)
    # judge
    discard(player2, t)

# print
utf8stdout = open(1, 'w', encoding='utf-8')
if player1:
    print('小哼win', file=utf8stdout)
    print('小哼当前手中的牌是 ' + str(player1)[1:-1].replace(',', ''), file=utf8stdout)
else:
    print('小哈win', file=utf8stdout)
    print('小哈当前手中的牌是 ' + str(player2)[1:-1].replace(',', ''), file=utf8stdout)
print('桌上的牌是 ' + str(L)[1:-1].replace(',', ''), file=utf8stdout)

'''
Sample:
2 4 1 2 5 6                      <= player1's pokers
3 1 3 5 6 4                      <= player2's pokers
小哈win                          <= print answer
小哈当前手中的牌是 1 6 5 2 3 4 1
桌上的牌是 3 4 5 6 2

# In python3, by default, it cannot print unicode due to its sys.stdout setting.
  (<_io.TextIOWrapper name='<stdout>' mode='w' encoding='US-ASCII'>)
  U see, it can only print US-ASCII, so we need to pass a utf-8 stdout to print().
# It's better to use 'for' to print list here, so u don't need to use slice & replace.
  They may take more time : )
'''
