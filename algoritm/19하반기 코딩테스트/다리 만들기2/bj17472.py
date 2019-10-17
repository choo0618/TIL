import sys
sys.stdin = open('bj17472.txt', 'r')

import pprint
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def IS(y,x):
    if -1<y<N and -1<x<M:return True
    return False

N, M = map(int, input().split())
Arr = [[int(x) for x in input().split()]for y in range(N)]
n = 0
Map = [[0]*M for _ in range(N)]
check = [[]]
for i in range(N):
    for j in range(M):
        if Arr[i][j] and not Map[i][j]:
            check.append([[i,j]])
            n+=1
            Map[i][j] = n
            Que = [[i,j]]
            while Que:
                que = []
                for q in Que:
                    for dir in range(4):
                        nY = q[0] + dy[dir]
                        nX = q[1] + dx[dir]
                        if IS(nY, nX) and Arr[nY][nX] and not Map[nY][nX]:
                            que.append([nY,nX])
                            Map[nY][nX] = n
                check[n] += que
                Que = que
# pprint.pprint(Map)
Distance = [[99999]*(n+1) for _ in range(n+1)]
# print(check)
Dis_Index = []
print(Dis_Index)
for idx, Dis in enumerate(check):
    for dis in Dis:
        for dir in range(4):
            hY = dis[0]
            hX = dis[1]
            cnt = 0
            check = 0
            while True:
                hY += dy[dir]
                hX += dx[dir]
                if not IS(hY,hX) or Map[hY][hX] == idx:
                    check = 1
                    break
                elif Map[hY][hX]:break
                cnt+=1
            if check:continue
            if 2 <= cnt < Distance[idx][Map[hY][hX]]:
                Distance[idx][Map[hY][hX]] = cnt
                if not [Map[hY][hX],idx,cnt] in Dis_Index:
                    Dis_Index.append([idx,Map[hY][hX],cnt])
                # Dis_Index[idx].append(Map[hY][hX])
pprint.pprint(Distance)
print(Dis_Index)
Island = [99999]*(n+1)
Result = -1
for idx, dis in enumerate(Distance[1]):
    if dis != 99999:
        result = dis
        visited = [1,1]*n
        Que = [idx, dis]
        # while Que:
        #     nIsland = Que.pop(0)
        #     for iidx, q in enumerate(Distance[idx]):
        #         if iidx
        #         visited[iidx] = 1

