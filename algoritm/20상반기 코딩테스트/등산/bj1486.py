import sys
sys.stdin = open('bj1486.txt','r')

print(ord('A')-65)
print(ord('Z')-65)
print(ord('a')-71)
print(ord('z')-71)

from collections import deque
dx=[1,0,-1,0]
dy=[0,-1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
def BFS(q,Mid):
    Map=[[[-1]*M for _ in range(N)]for __ in range(N)]
    Map[0][0][0]=0
    Que=deque([q])
    while Que:
        y,x,t,tmp=Que.popleft()
        for d in range(4):


N,M,T,D=map(int,input().split())
A=[list(map(str,input()))for _ in range(N)]
for i in range(N):
    for j in range(M):
        k=ord(A[i][j])
        if k>=97:k-=71
        else:k-=65
        A[i][j]=k
l,r=0,51
while l<=r:
    Mid=(l+r)//2
    if BFS((0,0,0,0),Mid):l=Mid+1
    else:R=Mid-1