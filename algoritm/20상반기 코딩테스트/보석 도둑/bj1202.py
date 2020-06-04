import sys
sys.stdin = open('bj1202.txt','r')

import heapq
N,K=map(int,input().split())
J,B=[],[]
for i in range(N):
    m,v=map(int,input().split())
    J.append((m,v))
for i in range(K):B.append(int(input()))
J.sort()
B.sort()
R,idx=0,0
Q=[]
for i in range(K):
    while idx<N and J[idx][0]<=B[i]:heapq.heappush(Q,-J[idx][1]);idx+=1
    if Q:R-=heapq.heappop(Q)
print(R)