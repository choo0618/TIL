import sys
sys.stdin = open('bj16954.txt','r')

from collections import deque
dx=[0,1,1,1,0,-1,-1,-1,0]
dy=[0,-1,0,1,1,1,0,-1,-1]
def IS(y,x):
    return -1<y<8 and -1<x<8
A=[list(map(str,input()))for _ in range(8)]
S=deque([(7,0)])
W=[]
R=0
Map=[[[0]*9 for __ in range(8)]for _ in range(8)]
while S and not R:
    s=deque()
    while S:
        y,x=S.popleft()
        if A[y][x]=='#':continue
        if (y,x)==(0,7):R=1
        for d in range(9):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and A[Y][X]!='#' and not Map[Y][X][d]:
                Map[Y][X][d]=1
                s.append((Y,X))
    S=s
    A.pop()
    A.insert(0,['.']*8)
print(R)