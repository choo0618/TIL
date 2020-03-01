import sys
sys.stdin = open('bj16397.txt','r')

from collections import deque
N,T,G=map(int,input().split())
Q=deque([(N,0)])
Map=[0]*100000
Map[N]=1
R='ANG'
while Q:
    n,c=Q.popleft()
    if n==G:R=c;break
    for i,next in enumerate([n+1,2*n]):
        if next>99999 or c==T:continue
        if i and next:next-=10**(len(str(next))-1)
        if not Map[next]:
            Map[next]=1
            Q.append((next,c+1))
print(R)

