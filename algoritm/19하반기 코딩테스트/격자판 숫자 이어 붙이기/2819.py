import sys
sys.stdin = open('2819.txt', 'r')

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]
def IS(y,x):
    if -1<y<4 and -1<x<4:return True
    return False
T = int(input())
for t in range(T):
    A = [[str(x)for x in input().split()]for y in range(4)]
    Result = set()
    for y in range(4):
        for x in range(4):
            Que = [[y, x, A[y][x]]]
            while len(Que[0][2]) != 7:
                Q = []
                for q in Que:
                    for dir in range(4):
                        nY = q[0] + dy[dir]
                        nX = q[1] + dx[dir]
                        if IS(nY, nX):
                            Q.append([nY, nX, q[2]+A[nY][nX]])
                Que = Q
            for ad in Que:
                Result.add(ad[2])
    print('#%d %d'%(t+1,len(Result)))