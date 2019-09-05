import sys
sys.stdin = open('bj3197.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1] and not M[y][x]:return True
    return False
L=[int(x)for x in input().split()]
A=[list(map(str,input()))for y in range(L[0])]
print(A)
M=[[0]*L[1]for _ in range(L[0])]
Q=[]
for i in range(L[0]):
    for j in range(L[1]):
        if A[i][j]=='L':Q.append([i,j,1]);M[i][j]=1
y=2
while True:
    q=[]
    while Q:
        hY,hX,Y=Q.pop(0)
        if Y==y:continue
        for dir in range(4):
            nY=hY+dy[dir]
            nX=hX+dx[dir]
            if IS(nY,nX):
                if A[nY][nX]=='.':M[nY][nX]+=M[hY][hX];Q.append([nY,nX,Y])
                elif A[nY][nX]=='X':M[nY][nX]+=M[hY][hX];q.append([nY,nX,Y+1])
    Q=q
    y+=1