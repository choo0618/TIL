import sys
sys.stdin = open('bj17472.txt', 'r')

import itertools
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
Distance = [[99999]*(n+1) for _ in range(n+1)]
Dis_Index = []
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
Island = [99999]*(n+1)
Result = 99999
Comb = list(itertools.combinations(Dis_Index,n-1))
for comb in Comb:
    result = 0
    visited = [1]+[0]*n
    visited[comb[0][0]] = 1
    for turn in range(3):
        for idx,c in enumerate(comb):
            if (visited[c[0]] and not visited[c[1]]) or (visited[c[1]] and not visited[c[0]]):
                visited[c[0]], visited[c[1]] = 1, 1
                result += c[2]
    if all(visited) and result < Result:
        Result = result
if Result == 99999:Result = -1
print(Result)
