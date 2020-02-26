import sys
sys.stdin= open('bj12851.txt','r')

from collections import deque
N,K=map(int,input().split())
Q=deque([(N,0)])
Set=set()
R,Min=0,0
Map=[0]*100001
while Q:
    n,c=Q.popleft()
    Map[n]=1
    if Min and c>Min:break
    if Min and n==K:R+=1
    if not Min and n==K:R+=1;Min=c
    for next in [n+1,n-1,2*n]:
        if 0<=next<=100000 and not Map[next]:Q.append((next,c+1))
print(Min)
print(R)