import sys
sys.stdin = open('bj11559.txt','r')

from collections import deque
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def IS(y,x):
    return -1<y<12 and -1<x<6
def BFS(y,x,n):
    Q = deque([[y,x]])
    while Q:
        hY,hX = Q.popleft()
        for dir in range(4):
            nY = hY+dy[dir]
            nX = hX+dx[dir]
            if IS(nY,nX) and A[nY][nX]==n and not Map[nY][nX]:
                Q.append([nY,nX])
                Map[nY][nX]=1
                Check[Cidx].append([nY,nX])

Dic = {'.':0,'R':1,'G':2,'B':3,'P':4,'Y':5}
A = [[x for x in input()]for _ in range(12)]
for i in range(12):
    for j in range(6):
        A[i][j]=Dic[A[i][j]]
R=0
while True:
    Check,Cidx,tmp=[],0,1
    Map=[[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if A[i][j] and not Map[i][j]:
                Check.append([])
                Check[Cidx].append([i,j])
                Map[i][j]=1
                BFS(i,j,A[i][j])
                Cidx+=1
    for c in Check:
        if len(c)>=4:
            tmp=0
            for bomb in c:
                A[bomb[0]][bomb[1]]=0
    if tmp:break
    A = list(map(list, zip(*A[::-1]))) # 오른쪽 회전
    for i in range(6):
        down = []
        for j in range(12):
            if A[i][j]:down.append(A[i][j])
        down += [0]*(12-len(down))
        A[i] = down
    for rotate in range(3):
        A = list(map(list, zip(*A[::-1])))
    R+=1
print(R)