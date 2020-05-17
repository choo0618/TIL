import sys
sys.stdin = open('bj2003.txt','r')

N,M=map(int,input().split())
L=[int(x)for x in input().split()]
R,s,tmp=0,0,0
for e in range(N):
    tmp+=L[e]
    while tmp>=M:
        if tmp==M:R+=1
        tmp-=L[s]
        s+=1
print(R)