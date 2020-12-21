import sys
sys.stdin = open('bj20055.txt','r')

from collections import deque
N,K=map(int,input().split())
L=deque([int(x)for x in input().split()])
Map=deque([0]*N)
R=0
while K>0:
    L.rotate()
    Map.rotate()
    Map[-1]=0
    for i in range(N-2,0,-1):
        if Map[i] and Map[i+1]==0 and L[i+1]:
            L[i+1]-=1
            Map[i],Map[i+1]=0,1
            if L[i+1]==0:K-=1
    Map[-1]=0
    if L[0]:
        Map[0]=1
        L[0]-=1
        if L[0]==0:K-=1
    R+=1
print(R)