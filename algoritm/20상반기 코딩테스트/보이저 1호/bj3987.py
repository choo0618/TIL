import sys
sys.stdin = open('bj3987.txt','r')

from collections import deque

ro={0:'U',1:'R',2:'D',3:'L'}
dx = [0,1,0,-1]
dy = [-1,0,1,0]
a1 = {0:1,1:0,2:3,3:2}   # /
a2 = {0:3,1:2,2:1,3:0}   # \

def IS(y,x):
    return -1<y<N and -1<x<M

N,M = map(int,input().split())
Arr = [list(map(str,input()))for y in range(N)]
PR,PC = map(int,input().split())
R=['U',0]
for sdir in range(4):
    Map = [[[0]*4for x in range(M)]for y in range(N)]
    r,dir,tmp = 0,sdir,0
    Map[PR-1][PR-1][dir]=1
    Q = deque([(PR-1,PC-1,dir)])
    while Q:
        r+=1
        hY,hX,d = Q.popleft()
        Map[hY][hX][d] = 1
        if Arr[hY][hX]=='/':d = a1[d]
        elif Arr[hY][hX]=='\\':d = a2[d]
        nY = hY+dy[d]
        nX = hX+dx[d]
        if IS(nY,nX) and Arr[nY][nX]!='C':
            if Map[nY][nX][d]:tmp=1
            else:Q.append([nY,nX,d])
    if tmp:
        R=[ro[sdir],'Voyager']
        break
    if r>R[1]:
        R[0] = ro[sdir]
        R[1] = r
for p in R:print(p)





