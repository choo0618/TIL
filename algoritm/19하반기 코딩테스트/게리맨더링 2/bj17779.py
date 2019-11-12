import sys
sys.stdin = open('bj17779.txt','r')

dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]
cdx = [0, 1, -1, 0]
cdy = [-1, 0, 0, 1]

def IS(y,x):
    if -1<y<N and -1<x<N:return True
    return False

def RL(y,x,dir):
    List = []
    while True:
        y += dy[dir]
        x += dx[dir]
        if IS(y,x) and y!= N-1:
            List.append([y,x])
        else:
            return List
def BT(left,right):
    L = []
    nY = left[0]
    nX = left[1]
    while True:
        nY += dy[0]
        nX += dx[0]
        if IS(nY, nX):
            L.append([nY, nX])
        else:break
    rY = right[0]
    rX = right[1]
    while True:
        rY += dy[1]
        rX += dx[1]
        if [rY, rX] in L:
            return [rY, rX]
        if not IS(rY, rX):
            return 0

N = int(input())
A = [[int(x)for x in input().split()]for y in range(N)]
Result = 987654321

for i in range(0,N-2):
    for j in range(1,N-1):
        Left = RL(i,j,1)
        Right = RL(i,j,0)
        for left in Left:
            for right in Right:
                Top = [i,j]
                Bottom = BT(left,right)
                if not Bottom:
                    continue
                Map = [[0]*N for _ in range(N)]
                tY, tX = i, j
                for dir in range(4):
                    while True:
                        Map[tY][tX] = 5
                        tY += dy[dir]
                        tX += dx[dir]
                        if [tY,tX] == Top or [tY,tX] == left or [tY,tX] == right or [tY,tX] == Bottom:
                            break
                n = 1
                for dir in range(4):
                    if not dir:
                        nY, nX = Top
                    elif dir == 1:
                        nY, nX = right
                    elif dir == 2:
                        nY, nX = left
                    elif dir == 3:
                        nY, nX = Bottom
                    while True:
                        nY += cdy[dir]
                        nX += cdx[dir]
                        if IS(nY,nX):
                            Map[nY][nX] = n
                        else:
                            break
                    n += 1
                Que = [[0, 0, 1], [0, N-1, 2], [N-1, 0, 3], [N-1, N-1, 4]]
                while Que:
                    Q = []
                    for q in Que:
                        Map[q[0]][q[1]] = q[2]
                        for dir in range(4):
                            nY = q[0]+cdy[dir]
                            nX = q[1]+cdx[dir]
                            if IS(nY,nX) and not Map[nY][nX]:
                                Map[nY][nX] = q[2]
                                Q.append([nY, nX, q[2]])
                    Que = Q
                rList = [0]*6
                for ry in range(N):
                    for rx in range(N):
                        rList[Map[ry][rx]] += A[ry][rx]
                rList[5] += rList[0]
                result = max(rList[1:6]) - min(rList[1:6])
                if result < Result:
                    Result = result
print(Result)
#
#
n = int(input())
grid = [[]] + [[0]+list(map(int,input().split())) for i in range(n)]
ans = 99**9

def divide(x, y, d1, d2):
    pop = [0]*5
    for r in range(1, n+1):
        for c in range(1, n+1):
            if x+y <= r+c <= x+y+2*d2 and y-x-2*d1 <= c-r <= y-x:
                pop[4]+= grid[r][c]
            elif 1<=r<x+d1 and 1<=c<=y: pop[0]+= grid[r][c]
            elif 1<=r<=x+d2 and y<c<=n: pop[1]+= grid[r][c]
            elif x+d1<=r<=n and 1<=c<y-d1+d2: pop[2]+= grid[r][c]
            else: pop[3]+= grid[r][c]
    return max(pop) - min(pop)

for x in range(1, n):
    for y in range(1, n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if not (x+d1+d2<=n and 1<=y-d1 and y+d2<=n): continue
                ans = min(ans, divide(x, y, d1, d2))
print(ans)


