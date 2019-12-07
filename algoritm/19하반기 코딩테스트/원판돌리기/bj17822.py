import sys
sys.stdin = open('bj17822.txt','r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def IS(y,x):
    if -1<=x<=M and -1<y<N:return True
    return False

def Same(y,x):
    for dir in range(4):
        nY = y + dy[dir]
        nX = x + dx[dir]
        if IS(nY, nX):
            if nX == -1:
                nX = M - 1
            elif nX == M:
                nX = 0
            if Arr[i][j] == Arr[nY][nX]:
                Map[i][j] = 1

N, M, T = map(int, input().split())
Arr = [list(map(int, input().split()))for _ in range(N)]
Rotate = [list(map(int, input().split()))for _ in range(T)]

for rotate in Rotate:
    Sum, Count = 0, 0
    for y in range(N):
        for x in range(M):
            if Arr[y][x]:
                Count += 1
                Sum += Arr[y][x]
    if not Count: break
    Check = 1
    Map = [[0]*M for m in range(N)]
    p = rotate[0]
    while p <= N:
        for turn in range(rotate[2]):
            if rotate[1]:
                Arr[p-1].append(Arr[p-1].pop(0))
            else:
                Arr[p-1].insert(0, Arr[p-1].pop(M-1))
        p += rotate[0]
    for i in range(N):
        for j in range(M):
            if Arr[i][j]:
                Same(i,j)
    for y in range(N):
        for x in range(M):
            if Map[y][x]:
                Check = 0
                Sum -= Arr[y][x]
                Arr[y][x] = 0
    if Check:
        avg = Sum/Count
        for y in range(N):
            for x in range(M):
                if Arr[y][x]:
                    if Arr[y][x] > avg:
                        Arr[y][x] -= 1
                    elif Arr[y][x] < avg:
                        Arr[y][x] += 1
R = 0
for i in range(N):
    for j in range(M):
        if Arr[i][j]:
            R += Arr[i][j]
print(R)