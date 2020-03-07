import sys
sys.stdin = open('bj16236.txt','r')

from collections import deque
def IS(y,x):
    return -1<y<N and -1<x<N
def Check(x):
    for i in range(min(x,7)):
        if F[i]:return True
    return False
def Eat(f):
    for i in range(N):
        if not f[i]: continue
        f[i].sort()
        F[A[i][f[i][0]]]-=1
        A[i][f[i][0]] = 0
        return i,f[i][0]
    return -1,-1
def BFS(y,x,s):
    R,eat=0,0
    while Check(s):
        d,Q,Map=10**9,deque([(y,x,0)]),[[0]*N for _ in range(N)]
        f=[[]for _ in range(N)]
        while Q:
            y,x,t=Q.popleft()
            if t>d:break
            if 0<A[y][x]<s:d=t;f[y].append(x);continue
            for Y,X in (y-1,x),(y,x-1),(y,x+1),(y+1,x):
                if IS(Y,X) and not Map[Y][X] and A[Y][X]<=s:
                    Map[Y][X]=1
                    Q.append((Y,X,t+1))
        y,x=Eat(f)
        if y==-1:break
        else:R+=d;eat+=1
        if eat==s:eat=0;s+=1
    return R
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
F=[0]*7
for i in range(N):
    for j in range(N):
        if A[i][j]==9:y=i;x=j;A[i][j]=0
        elif A[i][j]:F[A[i][j]]+=1
print(BFS(y,x,2))

from collections import deque
def IS(y,x,s):
    return -1<y<N and -1<x<N and A[y][x]<=s
def BFS(y,x,s):
    R,c,A[y][x]=0,0,0
    while True:
        M=[[0]*N for _ in range(N)]
        if c==s:s+=1;c=0
        Q=deque([(y,x,0)])
        M[y][x]=1
        d,l=10**9,[]
        while Q:
            y,x,hr=Q.popleft()
            if hr>d:break
            if 0<A[y][x]<s:
                d=hr
                l.append((y,x))
            for Y,X in (y-1,x),(y,x-1),(y,x+1),(y+1,x):
                if IS(Y,X,s) and not M[Y][X]:Q.append((Y,X,hr+1));M[Y][X]=1
        if d==10**9:break
        l.sort()
        y,x=l[0]
        A[y][x]=0
        c+=1
        R+=d
    return R
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
for i in range(N):
    for j in range(N):
        if A[i][j]==9:print(BFS(i,j,2))