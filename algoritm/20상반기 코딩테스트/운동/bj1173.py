import sys
sys.stdin = open('bj1173.txt','r')

N,m,M,T,R = map(int,input().split())
r,now,Time = 0,m,0
if m+T>M:print(-1)
else:
    while r!=N:
        nextT = now+T
        nextR = max(m,now-R)
        if nextT <= M:
            now = nextT
            r+=1
        else:
            now = nextR
        Time+=1
    print(Time)





