import sys
# sys.stdin = open('bj3665.txt','r')
sys.stdin = open('E.in','r')

for t in range(int(input())):
    N=int(input())
    rank=[int(x)for x in input().split()]
    D=[0]*(N+1)
    d=[[0]*(N+1) for _ in range(N+1)]
    Q,R,F=[],[],0
    for i in range(N):
        for j in range(i+1,N):
            d[rank[i]][rank[j]]=1
            D[rank[j]]+=1
    for i in range(int(input())):
        a,b=map(int,input().split())
        if d[a][b]:a,b=b,a
        d[a][b],d[b][a]=1,0
        D[a]-=1;D[b]+=1
    for i in rank:
        if not D[i]:Q.append(i)
    while Q:
        a=Q.pop()
        R.append(a)
        if Q:F=1;break
        for b in range(1,N+1):
            if not d[a][b]:continue
            D[b]-=1
            if not D[b]:Q.append(b)
    if F:print('?')
    elif len(R)!=N:print('IMPOSSIBLE')
    else:print(*R)