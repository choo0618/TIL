import sys
sys.stdin = open('4301.txt', 'r')

dx = [2, 0]
dy = [0, 2]

def IS(y,x):
    if -1<y<L[1] and -1<x<L[0]: return True
    return False

T = int(input())
for t in range(T):
    L = [int(x)for x in input().split()]
    Map = [[1] * L[0]for _ in range(L[1])]
    Result = 0
    for i in range(L[1]):
        for j in range(L[0]):
            if Map[i][j]:
                for dir in range(2):
                    nY = i + dy[dir]
                    nX = j + dx[dir]
                    if IS(nY, nX):
                        Map[nY][nX] = 0
    for r in Map:
        Result += sum(r)
    print('#%d %d'%(t+1, Result))