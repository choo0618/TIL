import sys
sys.stdin = open('bj17837.txt', 'r')

dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]

def IS(y,x):
    if -1<y<N and -1<x<N and Arr[y][x]!=2:return True
    return False

N, K = map(int, input().split())
Arr = [[int(x)for x in input().split()]for y in range(N)]
Drone = [[int(x)for x in input().split()]for y in range(K)]
Map = [[[]for m in range(N)] for _ in range(N)]
for idx in range(K):
    Drone[idx][0] -= 1
    Drone[idx][1] -= 1
    Map[Drone[idx][0]][Drone[idx][1]].append(idx)
Result = 0
while Result != 1001:
    Result += 1
    check = 0
    for idx, drone in enumerate(Drone):
        nY = drone[0] + dy[drone[2]]
        nX = drone[1] + dx[drone[2]]
        nD = drone[2]
        if not IS(nY,nX):
            if drone[2] == 1:
                nD = 2
                nX -= 2
            elif drone[2] == 2:
                nD = 1
                nX += 2
            elif drone[2] == 3:
                nD = 4
                nY += 2
            elif drone[2] == 4:
                nD = 3
                nY -= 2
        if not IS(nY, nX):
            Drone[idx][2] = nD
            continue
        Index = Map[drone[0]][drone[1]].index(idx)
        move = Map[drone[0]][drone[1]][Index:]
        Map[drone[0]][drone[1]] = Map[drone[0]][drone[1]][0:Index]
        if Arr[nY][nX] == 1:
            move.reverse()
            Map[nY][nX] += move
        elif not Arr[nY][nX]:
            Map[nY][nX] += move
        for m in move:
            Drone[m][0] = nY
            Drone[m][1] = nX
        Drone[idx][2] = nD
        if len(Map[nY][nX])>=4:
            check = 1
            break
    if check:
        break
if Result == 1001:
    Result = -1
print(Result)
