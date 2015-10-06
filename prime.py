#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def primeCount(stNum,endNum) :
    
    num = [ x for x in range(stNum,endNum)]
    
    idx = -1
    
    for x in num :
        idx += 1
        for y in range(2,x//2+1) :
            if not x % y :
                num[idx] = "*"
                break

    return len([ x for x in num if x != "*" ])

cnt = 1
cntMax = 1000**2 # いくつまで計算を行うか
ans = []

while cnt < cntMax :
    print "--"
    print cnt*1000-1000+1
    ans.append(primeCount(cnt*1000-1000+1,cnt*1000+1))
    cnt += 1

print ans

X = range(1,cntMax)
Y = ans

plt.bar(X,Y, align="center")
plt.xticks(X,[ str(x*1000-1000+1) + "~" for x in X])
plt.show()
