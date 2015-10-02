# coding: utf-8
# Here your code !


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

while cnt < 10 :
    print "--"
    print cnt*1000-1000+1
    print primeCount(cnt*1000-1000+1,cnt*1000+1)
    cnt += 1
