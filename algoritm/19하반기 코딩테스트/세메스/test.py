import sys
sys.stdin = open('test.txt','r')

import copy
dx = [1,0]
dy = [0,1]
def IS(y,x):
    return -1<y<L[0] and -1<x<L[0]


L = [int(x)for x in input().split()]
Arr = [[int(x)for x in input().split()]for y in range(L[0])]
TypeA = [[int(x)for x in input().split()]for y in range(L[1])]
TypeB = [[int(x)for x in input().split()]for y in range(L[2])]
TypeC = [[int(x)for x in input().split()]for y in range(L[3])]

R = 987654321

Map = [[[]for x in range(L[0])]for y in range(L[0])]
Tmap = [[987654321]*L[0] for _ in range(L[0])]

Que = [[0,0,[],0]]
while Que:
    que = []
    for q in Que:
        hY = q[0]
        hX = q[1]
        htype = q[2]
        hT = q[3]
        if Arr[hY][hX] == 2:
            if hT < R:
                R = hT
                continue
        if hT > R:
            continue
        for dir in range(2):
            nY = hY + dy[dir]
            nX = hX + dx[dir]
            nType = copy.deepcopy(htype)
            nT = hT + 1
            if IS(nY,nX):
                nType.append(Arr[nY][nX])
                if len(nType)==5:
                    nType.pop(0)
                if nType in TypeA:
                    Tmap[0][0] = nT
                    Map[0][0].append([Arr[0][0]])
                    que.append([0,0,[Arr[0][0]],nT])
                    continue
                if nType in TypeB:
                    # Tmap[L[0]//2][L[0]//2] = nT
                    Map[L[0]//2][L[0]//2].append([Arr[L[0]//2][L[0]//2]])
                    que.append([L[0]//2,L[0]//2,[Arr[L[0]//2][L[0]//2]],nT])
                    continue
                if nType in TypeC:
                    Tmap[nY][nX] = hT
                    Map[nY][nX].append([Arr[nY][nX]])
                    que.append([nY,nX,[Arr[nY][nX]],hT])
                    continue
                if not nType in Map[nY][nX] or nT < Tmap[nY][nX]:
                    Tmap[nY][nX] = nT
                    Map[nY][nX].append(nType)
                    que.append([nY,nX,nType,nT])
    Que = que

if R == 987654321:
    R = -1
print(R)