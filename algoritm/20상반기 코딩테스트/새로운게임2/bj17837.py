import sys
sys.stdin = open('bj17837.txt','r')

dx=[0,1,-1,0,0]
dy=[0,0,0,-1,1]

def IS(y,x):
    return -1<y<N and -1<x<N and Arr[y][x]!=2

N,K = map(int,input().split())
Arr = [[int(x)for x in input().split()]for y in range(N)]
Drone = [[int(x)for x in input().split()]for y in range(K)]
Map = [[[]for m in range(N)]for _ in range(N)]
n=0
for idx,d in enumerate(Drone):
    Y,X = d[0]-1,d[1]-1
    Drone[idx] = [Y,X,d[2]]
    Map[Y][X].append(idx)
while n!=1000:
    n+=1
    check = 0
    for idx,d in enumerate(Drone):
        nD = d[2]
        nY = d[0]+dy[nD]
        nX = d[1]+dx[nD]
        if not IS(nY,nX):
            if nD%2:nD+=1
            else:nD-=1
            nY+=2*dy[nD]
            nX+=2*dx[nD]
            if not IS(nY,nX):
                Drone[idx][2]=nD
                continue
        IDX = Map[d[0]][d[1]].index(idx)
        move = Map[d[0]][d[1]][IDX:]
        if Arr[nY][nX]==1:move.reverse()
        Map[d[0]][d[1]] = Map[d[0]][d[1]][:IDX]
        Map[nY][nX]+=move
        for m in move:
            Drone[m][0]=nY
            Drone[m][1]=nX
        Drone[idx][2]=nD
        if len(Map[nY][nX])>=4:
            check=1
            break
    if check:break
if n==1000:print(-1)
else:print(n)
