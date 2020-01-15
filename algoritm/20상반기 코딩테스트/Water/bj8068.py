import sys
sys.stdin = open('bj8068.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def BFS(y,x,h):
    Map[y][x]=1
    Que,water,tmp = [[y,x]],[[y,x]],0
    while Que:
        Q=[]
        for q in Que:
            for dir in range(4):
                nY=q[0]+dy[dir]
                nX=q[1]+dx[dir]
                if Arr[nY][nX]<=h and not Map[nY][nX]:
                    if (nY==0 or nY==N-1 or nX==0 or nX==M-1) or Arr[nY][nX]<h:
                        tmp=1
                        continue
                    Map[nY][nX]=1
                    water.append([nY,nX])
                    Q.append([nY,nX])
        Que=Q
    if tmp:water=[]
    return water
N,M=map(int,input().split())
Arr,Max,R=[],0,0
for i in range(N):
    I = list(map(int,input().split()))
    Arr.append(I)
    if max(I)>Max:Max=max(I)
for m in range(1,Max):
    Map=[[0] * M for _ in range(N)]
    Water=[]
    for i in range(1,N-1):
        for j in range(1,M-1):
            if Arr[i][j]==m and not Map[i][j]:
                Water += BFS(i,j,m)
    for w in Water:
        Arr[w[0]][w[1]]+=1
        R+=1
print(R)

