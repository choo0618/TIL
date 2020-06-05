import sys
sys.stdin = open('5653.txt','r')

for t in range(int(input())):
    N,M,K=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    Q,Set=[],set()
    for i in range(N):
        for j in range(M):
            if A[i][j]:Q.append((2*A[i][j],A[i][j],i,j));Set.add((i,j))
    for i in range(K):
        Q.sort()
        q=[]
        while Q:
            c,s,y,x=Q.pop()
            if c-1:q.append((c-1,s,y,x))
            if c==s:
                for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
                    Len=len(Set)
                    Set.add((Y,X))
                    if Len!=len(Set):q.append((2*s,s,Y,X))
        Q=q
    print('#%d %d'%(t+1,len(Q)))