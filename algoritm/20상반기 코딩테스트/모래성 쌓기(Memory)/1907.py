import sys
sys.stdin=open('1907.txt','r')

dx=[1,1,1,0,-1,-1,-1,0]
dy=[-1,0,1,1,1,0,-1,-1]
def IS(y,x):
    return -1<y<H and -1<x<W
for t in range(int(input())):
    H,W=map(int,input().split())
    A=[list(map(str,input()))for _ in range(H)]
    C,R=[],0
    for i in range(H):
        for j in range(W):
            if A[i][j]!='.' and A[i][j]!='9':C.append((i,j,int(A[i][j])))
    while True:
        B=[]
        L=[]
        for y,x,n in C:
            cnt=0
            for d in range(8):
                Y,X=y+dy[d],x+dx[d]
                if IS(Y,X) and A[Y][X]=='.':cnt+=1
            if cnt>=n:B.append((y,x,n))
            else:L.append((y,x,n))
        if not B:break
        for y,x,n in B:A[y][x]='.'
        C=L
        R+=1
    print('#%d %d'%(t+1,R))