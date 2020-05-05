import sys
sys.stdin = open('bj15558.txt','r')

from collections import deque
N,K=map(int,input().split())
A=[list(map(int,input()))+[1]*K for y in range(2)]
V=[[0]*(N+K) for _ in range(2)]
Q=deque([(0,0,-1)])
R=0
while Q:
    y,x,t=Q.popleft()
    if x>=N:R=1;break
    for Y,X in (y,x+1),(y,x-1),((y+1)%2,x+K):
        if V[Y][X] or not A[Y][X] or X<=t+1:continue
        V[Y][X]=1
        Q.append((Y,X,t+1))
print(R)