import sys
sys.stdin= open('bj1697.txt','r')

from collections import deque
N,K=map(int,input().split())
Q=deque([(N,0)])
Set=set()
while Q:
    n,c=Q.popleft()
    if n==K:print(c);break
    for next in [n+1,n-1,2*n]:
        if 0<=next<=100000 and not next in Set:
            Set.add(next)
            Q.append((next,c+1))
