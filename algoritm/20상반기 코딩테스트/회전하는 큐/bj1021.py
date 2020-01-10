import sys
sys.stdin = open('bj1021.txt','r')

N,M = map(int,input().split())
L = [int(x)for x in input().split()]
Q = [int(x)for x in range(1,N+1)]
R=0
for n in L:
    idx = Q.index(n)
    Len = len(Q)//2
    if idx<=Len:
        Sl=Q[0:idx+1]
        R+=len(Sl)-1
    else:
        Sl=Q[idx:]
        R+=len(Sl)
    Q=Q[idx+1:]+Q[0:idx]
print(R)