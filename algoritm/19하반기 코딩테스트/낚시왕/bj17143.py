import sys
sys.stdin = open('bj17143.txt', 'r')

import pprint
# 0 상 하 우 좌
dx = [0,0,0,1,-1]
dy = [0,-1,1,0,0]
change_dir = [0,2,1,4,3]
R, C, M = map(int, input().split())
# (i,j) 속력 방향 크기
Arr = [[int(x)for x in input().split()]for y in range(M)]
Map = [[0]*C for _ in range(R)]
for shark in Arr:
    Map[shark[0]-1][shark[1]-1] = shark[2:]
Man = 0
Result = 0
while Man < C:
    for i in range(R):
        if Map[i][Man]:
            Result += Map[i][Man][2]
            Map[i][Man] = 0
            break
    MMap = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if Map[i][j]:
                v, dir, size = Map[i][j]
                hY, hX = i, j
                for go in range(v):
                    hY += dy[dir]
                    hX += dx[dir]
                    if hY == -1:
                        hY += 2
                        dir = 2
                    elif hY == R:
                        hY -=2
                        dir = 1
                    elif hX == -1:
                        hX += 2
                        dir = 3
                    elif hX == C:
                        hX -= 2
                        dir = 4
                if not MMap[hY][hX]:
                    MMap[hY][hX] = [v, dir, size]
                else:
                    if size > MMap[hY][hX][2]:
                        MMap[hY][hX] = [v, dir, size]
    Map = MMap
    Man += 1
print(Result)