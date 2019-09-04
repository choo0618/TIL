import sys
sys.stdin = open('bj1697.txt','r')

n,m=map(int,input().split())
i=100000
M=[-1]*(i+1)
Q=[n]
M[n]=0
while Q:
    x=Q.pop(0)
    for nx in [x-1,x+1,x*2]:
        if 0<=nx<=i and M[nx]==-1 :
            M[nx]=M[x]+1
            Q.append(nx)
print(M[m])