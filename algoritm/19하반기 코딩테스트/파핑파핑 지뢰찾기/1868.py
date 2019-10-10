import sys
sys.stdin = open('1868.txt', 'r')

dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]
def IS(y,x):
    if -1 < y < N and -1 < x < N:
        return True
    return False
def check(y,x):
    count = 0
    for dir in range(8):
        nY = y + dy[dir]
        nX = x + dx[dir]
        if IS(nY, nX):
            if A[nY][nX]=='*':
                count += 1
    return count

T = int(input())
for t in range(T):
    N = int(input())
    A = [list(map(str,input()))for _ in range(N)]
    Map = [[0] * N for _ in range(N)]
    R = 0
    for y in range(N):
        for x in range(N):
            if A[y][x] == '.' and not check(y,x):
                R += 1
                A[y][x] = 0
                Que = [[y,x]]
                while Que:
                    hY, hX = Que.pop(0)
                    for dir in range(8):
                        nY = hY + dy[dir]
                        nX = hX + dx[dir]
                        if IS(nY, nX) and A[nY][nX] == '.':
                            C = check(nY, nX)
                            if not C:
                                Que.append([nY,nX])
                                A[nY][nX] = 0
                            else:
                                A[nY][nX] = C
    for c in A:
        R += c.count('.')
    print('#%d %d'%(t+1,R))



