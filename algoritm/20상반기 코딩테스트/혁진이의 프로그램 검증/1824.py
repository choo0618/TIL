import sys
sys.stdin = open('1824.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
for t in range(int(input())):
    R,C=map(int,input().split())
    A=[input()for _ in range(R)]
    Map=[[[[0,0,0,0]for _ in range(C)]for __ in range(R)] for ___ in range(16)]
    Map[0][0][0][0]=1
    Q=deque([(0,0,0,0)])
    Re='NO'
    while Q:
        q=0
        y,x,d,m=Q.popleft()
        if A[y][x]=='<':d=2
        elif A[y][x]=='>':d=0
        elif A[y][x]=='^':d=3
        elif A[y][x]=='v':d=1
        elif A[y][x]=='_':d=0 if not m else 2
        elif A[y][x]=='|':d=1 if not m else 3
        elif A[y][x]=='.':pass
        elif A[y][x]=='@':Re='YES';break
        elif A[y][x]=='+':m=m+1 if m!=15 else 0
        elif A[y][x]=='-':m=m-1 if m!=0 else 15
        elif A[y][x]=='?':q=1
        else:m=int(A[y][x])
        L=[d]if not q else list(range(4))
        for dir in L:
            Y=y+dy[dir] if -1<y+dy[dir]<R else 0 if y+dy[dir]==R else R-1
            X=x+dx[dir] if -1<x+dx[dir]<C else 0 if x+dx[dir]==C else C-1
            if not Map[m][Y][X][dir]:
                Map[m][Y][X][dir]=1
                Q.append((Y,X,dir,m))
    print('#%d %s'%(t+1,Re))