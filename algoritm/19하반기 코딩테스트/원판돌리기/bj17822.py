import sys
sys.stdin = open('bj17822.txt','r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def IS(y,x):
    if -1<=x<=M and -1<y<N:return True
    return False

N, M, T = map(int, input().split())
Arr = [list(map(int, input().split()))for _ in range(N)]
Rotate = [list(map(int, input().split()))for _ in range(T)]
Count = N * M

for rotate in Rotate:
    Sum = 0
    for y in range(N):
        for x in range(M):
            if Arr[y][x] != 1001:
                Sum += Arr[y][x]
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
            if not Map[i][j] and Arr[i][j] != 1001:
                Que = [[i,j]]
                while Que:
                    que = []
                    for q in Que:
                        for dir in range(4):
                            nY = q[0] + dy[dir]
                            nX = q[1] + dx[dir]
                            if IS(nY, nX):
                                if nX == -1: nX = M-1
                                elif nX == M: nX = 0
                                if Arr[q[0]][q[1]] == Arr[nY][nX] and not Map[nY][nX]:
                                    Check = 0
                                    Map[q[0]][q[1]] = 1
                                    Map[nY][nX] = 1
                                    que.append([nY, nX])
                    Que = que
    for y in range(N):
        for x in range(M):
            if Map[y][x]:
                Sum -= Arr[y][x]
                Arr[y][x] = 1001
                Count -= 1
    if Check and Count:
        check = Sum/Count
        for y in range(N):
            for x in range(M):
                if Arr[y][x]:
                    if Arr[y][x] > check:
                        Arr[y][x] -= 1
                    elif Arr[y][x] < check:
                        Arr[y][x] += 1
print(Sum)

