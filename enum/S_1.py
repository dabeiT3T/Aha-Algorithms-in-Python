#!/usr/bin/env python3
'''
124+659=783     <= print answer
125+739=864
127+359=486
127+368=495
128+367=495
128+439=567
129+357=486
129+438=567
129+654=783
129+735=864
134+658=792
135+729=864
...             <= more
total=168       <= total

It really takes a long time to enum : (
'''

# Quiz url
# Not Found

L = [0] * 9
total = 0
for L[0] in range(1, 10):
    for L[1] in range(1, 10):
        for L[2] in range(1, 10):
            for L[3] in range(1, 10):
                for L[4] in range(1, 10):
                    for L[5] in range(1, 10):
                        for L[6] in range(1, 10):
                            for L[7] in range(1, 10):
                                for L[8] in range(1, 10):
                                    B = [0] * 9
                                    for x in L:
                                        B[x-1] = 1
                                    if (sum(B) == 9 and (
                                        (L[0]+L[3])*100 + 
                                        (L[1]+L[4])*10 +
                                        L[2]+L[5]) == 
                                        (L[6]*100+L[7]*10+L[8])):
                                        print('{0[0]}{0[1]}{0[2]}+{0[3]}{0[4]}{0[5]}={0[6]}{0[7]}{0[8]}'.format(L))
                                        total += 1

print('total=%d' % (total/2))
