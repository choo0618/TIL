import sys
sys.stdin = open('bj11725.txt','r')

N=int(input())
Map=[[]for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,input().split())
    Map[a].append(b)
    Map[b].append(a)
R=[0]*(N+1)
V=[0]*(N+1)
Q=[1]
while Q:
    a=Q.pop()
    V[a]=1
    for _ in Map[a]:
        if V[_]:continue
        R[_]=a
        Q.append(_)
for _ in R[2:]:print(_)

