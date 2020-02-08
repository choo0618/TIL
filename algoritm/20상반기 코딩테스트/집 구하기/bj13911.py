import sys
sys.stdin = open('bj13911.txt','r')

from collections import deque
def DIS(L,t):
    Dm=[-1]*(V+1)
    for l in L:Dm[l]=0
    Que=deque(L)
    while Que:
        x=Que.popleft()
        for m in Map[x]:
            a,b=m
            D=Dm[x]+b
            if (Dm[a]==-1 or D<Dm[a]) and D<=t:
                Dm[a]=D
                Que.append(a)
    return Dm
V,E=map(int,input().split())
Map=[[]for _ in range(V+1)]
for i in range(E):
    a,b,c=map(int,input().split())
    Map[a].append((b,c))
    Map[b].append((a,c))
M,x=map(int,input().split())
m=[int(x)for x in input().split()]
Md=DIS(m,x)
S,y=map(int,input().split())
s=[int(x)for x in input().split()]
Sd=DIS(s,y)
R=10**8
for i in range(V+1):
    if Md[i]>0 and Sd[i]>0:R=min(R,Md[i]+Sd[i])
print(R if R!=10**8 else -1)