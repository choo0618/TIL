import sys
sys.stdin=open('bj16928.txt','r')

from collections import deque
N,M=map(int,input().split())
Dic={}
for d in range(N+M):
    a,b=map(int,input().split())
    Dic[a]=b
Map=[0]*101
Map[1]=1
Q=deque([(1,0)])
while Q:
    a,c=Q.popleft()
    if a==100:print(c);break
    for d in range(1,7):
        b=a+d
        C=c+1
        if b in Dic:b=Dic[b]
        if b<=100 and not Map[b]:
            Map[b]=1
            Q.append((b,C))
