import sys
sys.stdin= open('bj8111.txt','r')

from collections import deque
for t in range(int(input())):
    N=int(input())
    Q=deque([1])
    Map=[0]*(N+1)
    A=[[0,0]for _ in range(N+1)]
    A[1]=[-1,'1']
    Map[1]=1
    R='BRAK'
    Check=1
    while Q and Check:
        n=Q.popleft()
        P=[(n*10)%N,(n*10+1)%N]
        for i in range(2):
            if Map[P[i]]:continue
            A[P[i]][0]=n
            A[P[i]][1]=str(i)
            if not P[i]:Check=0;break
            Q.append(P[i])
            Map[P[i]]=1
    L=''
    N=0
    while A[N][0]!=-1:
        L=A[N][1]+L
        N=A[N][0]
    L=A[N][1]+L
    print(L)

from collections import deque
for t in range(int(input())):
    N=int(input())
    Q=deque([1])
    Map=[0]*(N+1)
    Map[1]=-1
    while Q:
        n=Q.popleft()
        P=[(n*10)%N,(n*10+1)%N]
        for i in [0,1]:
            new=(10*n+i)%N
            if Map[new]:continue
            Q.append(new)
            Map[new]=n
    L=''
    c=0
    while Map[c]!=-1:
        d=+(Map[c]*10%N!=c)
        L=str(d)+L
        c=Map[c]
    L='1'+L
    print(L)
