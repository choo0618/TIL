import sys
sys.stdin=open('bj2146.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x,t):
    Map[y][x]=t
    Que=[[y,x]]
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX) and A[nY][nX] and not Map[nY][nX]:
                    Map[nY][nX]=t
                    Q.append((nY,nX,t))
        IL[t]+=Q
        Que=Q
def BFS1(Array):
    Min=0
    Que=Array
    while Que:
        Min+=1
        Q=[]
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if IS(nY,nX) and Map[nY][nX]!=q[2] and not lenMap[nY][nX]:
                    if Map[nY][nX] and Map[nY][nX]!=q[2]:return Min-1
                    lenMap[nY][nX]=Min
                    Q.append((nY,nX,q[2]))
        Que=Q
    return 987654321
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[[0]*N for _ in range(N)]
tmp=1
IL=[[]]
for i in range(N):
    for j in range(N):
        if A[i][j] and not Map[i][j]:
            IL.append([])
            IL[tmp].append((i,j,tmp))
            BFS(i,j,tmp)
            tmp+=1
R=987654321
for idx,il in enumerate(IL):
    lenMap=[[0]*N for _ in range(N)]
    Min = BFS1(il)
    if Min<R:R=Min
print(R)
