import sys
sys.stdin = open('bj3055.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]and A[nY][nX]!='X':return True
    return False
L=[int(x)for x in input().split()]
A=[list(map(str,input()))for y in range(L[0])]
Q,H=[],0
for i in range(L[0]):
    for j in range(L[1]):
        if A[i][j]=='*':Q.append([i,j,'*',0])
        elif A[i][j]=='S':G=[[i,j,'S',0]]
        elif A[i][j]=='D':H=[i,j]
# Q+=G
R='KAKTUS'
while Q:
    hY,hX,s,d=Q.pop()
    if s=='S' and H==[hY,hX]:R=d;break
    for dir in range(4):
        nY=hY+dy[dir]
        nX=hX+dx[dir]
        if IS(nY,nX):
            if s=='*'and A[nY][nX]!='D'and A[nY][nX]=='.':A[nY][nX]='*';Q.append([nY,nX,s,0])
            elif s=='S' and A[nY][nX]!='*':A[nY][nX]=d+1;Q.append([nY,nX,s,d+1])
    # q,c=[],0
    # for m in Q:
    #     hY,hX,s,d=m
    #     if s=='S' and H==[hY,hX]:R=d;c=1;break
    #     for dir in range(4):
    #         nY=hY+dy[dir]
    #         nX=hX+dx[dir]
    #         if IS(nY,nX):
    #             if s=='*'and A[nY][nX]!='D'and A[nY][nX]=='.':A[nY][nX]='*';Q.append([nY,nX,s,0])
    #             elif s=='S' and A[nY][nX]!='*':A[nY][nX]=d+1;Q.append([nY,nX,s,d+1])
    # if c:break
    # Q=q
print(R)




