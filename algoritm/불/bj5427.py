import sys
sys.stdin = open('bj5427.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[1] and -1<x<L[0]:return True
    return False
T=int(input())
for t in range(T):
    L=[int(x)for x in input().split()]
    A=[list(map(str,input()))for _ in range(L[1])]
    Q,h=[],0
    for i in range(L[1]):
        for j in range(L[0]):
            if A[i][j]=='@':h=[[i,j,'@',1]]
            elif A[i][j]=='*':Q.append([i,j,'*',0])
    Q=h+Q
    R='IMPOSSIBLE'
    while Q:
        q,c=[],0
        for d in Q:
            s=d[2]
            if s=='@' and A[d[0]][d[1]]=='*':continue
            if s=='@' and (not min([d[0],d[1]]) or (d[0]==L[1]-1 or d[1]==L[0]-1)):R=d[3];c=1;break
            for dir in range(4):
                nY=d[0]+dy[dir]
                nX=d[1]+dx[dir]
                if IS(nY,nX):
                    if s=='@' and A[nY][nX]=='.':A[nY][nX]=d[3]+1;q.append([nY,nX,'@',d[3]+1])
                    elif s=='*' and A[nY][nX]!='#'and A[nY][nX]!='*':A[nY][nX]=s;q.append([nY,nX,'*',0])
        Q=q
        if c:break
    print(R)