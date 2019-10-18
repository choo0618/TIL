import sys
sys.stdin = open('bj17144.txt','r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]
up_dir = [3,0,1,2]
do_dir = [1,0,3,2]
def IS(y,x):
    if -1<y<R and -1<x<C:return True
    return False

def Dust(y,x):
    tmp = Arr[y][x] // 5
    for dir in range(4):
        nY = y + dy[dir]
        nX = x + dx[dir]
        if IS(nY, nX) and Arr[nY][nX] != -1:
            Map[nY][nX] += tmp
            Arr[y][x] -= tmp
    Map[y][x] += Arr[y][x]

def BFS(y,x,dir_list,check):
    hY = y
    hX = x
    for dir in dir_list:
        while IS(hY+dy[dir],hX+dx[dir]):
            nY = hY + dy[dir]
            nX = hX + dx[dir]
            if check == 'up' and nY == y+1:break
            if check == 'down' and nY == y-1:break
            Arr[hY][hX] = Arr[nY][nX]
            Arr[nY][nX] = 0
            hY, hX = nY, nX
            if (hY, hX) == (y, x+1):break

R, C, T = map(int, input().split())
Arr = [[int(x)for x in input().split()]for y in range(R)]
Result = 0
for a in range(R):
    if Arr[a][0] == -1:
        air = a
        break
while T:
    Map = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if Arr[i][j] and Arr[i][j] != -1:
                Dust(i,j)
    Arr = Map
    BFS(air,0,up_dir, 'up')
    BFS(air+1,0,do_dir, 'down')
    Arr[air][0] = Arr[air + 1][0] = -1
    T -= 1
for r in range(R):
    Result += sum(Arr[r])
print(Result+2)



