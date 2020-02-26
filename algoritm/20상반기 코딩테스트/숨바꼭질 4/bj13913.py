import sys
sys.stdin= open('bj13913.txt','r')

from collections import deque
N,K=map(int,input().split())
Q=deque([(N,0)])
Map,P=[0]*100001,[0]*100001
Map[N]=1
while Q:
    n,c=Q.popleft()
    if n==K:
        print(c)
        L=deque()
        while n!=N:
            L.appendleft(n)
            n=P[n]
        L.appendleft(N)
        print(' '.join(map(str,L)))
        break
    for next in [n+1,n-1,2*n]:
        if 0<=next<=100000 and not Map[next]:
            P[next]=n
            Map[next]=1
            Q.append((next,c+1))