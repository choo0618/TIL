import sys
sys.stdin = open('bj15683.txt','r')

dx=[0,1,0,-1]
dy=[-1,0,1,0]
d=[[0],[[0],[1],[2],[3]],[[0,2],[1,3]],[[0,1],[1,2],[2,3],[0,3]],[[0,1,2],[1,2,3],[2,3,0],[3,0,1]],[[0,1,2,3]]]
def IS(y,x):
    if -1<x<L[1] and -1<y<L[0] and A[y][x]!=6:return True
    return False
def C():
    r=0
    for y in range(L[0]):
        for x in range(L[1]):
            if not A[y][x]:r+=1
    return r
def DFS(x):
    global A,R
    if x==len(Q):
        r=C()
        if r<R:R=r
        return
    for i in d[Q[x][2]]:
        q=[]
        hY=Q[x][0]
        hX=Q[x][1]
        for j in i:
            n=1
            while True:
                nY=hY+n*dy[j]
                nX=hX+n*dx[j]
                if IS(nY,nX):
                    if not A[nY][nX]:A[nY][nX]=Q[x][2];q.append([nY,nX])
                else:break
                n+=1
        DFS(x+1)
        for b in q:A[b[0]][b[1]]=0
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
Q=[]
R,r=9999,0
for i in range(L[0]):
    for j in range(L[1]):
        if A[i][j]and A[i][j]!=6:Q.append([i,j,A[i][j]])
DFS(0)
print(R)
