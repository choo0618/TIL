import sys
sys.stdin = open('1861.txt','r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def IS(y, x):
    if -1<y<N and -1<x<N:return True
    return False

T = int(input())
for t in range(T):
    N = int(input())
    A = [[int(x) for x in input().split()]for y in range(N)]
    Map = [[0]*N for _ in range(N)]
    Size = [[0]*N for _ in range(N)]
    Result = []
    Max = 0
    for y in range(N):
        for x in range(N):
            size = 1
            Que = [[y, x]]
            Map[y][x] = 1
            while Que:
                hY, hX = Que.pop(0)
                for dir in range(4):
                    nY = hY + dy[dir]
                    nX = hX + dx[dir]
                    if IS(nY, nX) and (A[nY][nX] - A[hY][hX] == 1):
                        Map[nY][nX] = 1
                        size += 1
                        Que.append([nY, nX])
            Size[y][x] = size
            if size > Max:
                Max = size
    for i in range(N):
        for j in range(N):
            if Size[i][j] == Max:
                Result.append(A[i][j])
    Result.sort()
    print('#%d %d %d'%(t+1, Result[0], Max))
