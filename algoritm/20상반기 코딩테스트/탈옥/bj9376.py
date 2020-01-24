import sys
sys.stdin=open('bj9376.txt','r')

from collections import deque
dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<H+2 and -1<x<W+2
T=int(input())
for t in range(T):
    H,W=map(int,input().split())
    Arr=['.'*(W+2)]+[['.']+list(map(str,input()))+['.']for y in range(H)]+['.'*(W+2)]
    Que,tmp,R=deque([(0,0,0)]),1,987654321
    for i in range(H+2):
        for j in range(W+2):
            if Arr[i][j]=='$':Que.append((i,j,tmp));tmp+=1;Arr[i][j]='.'
    Map=[[[-1]*3 for x in range(W+2)] for _ in range(H+2)]
    for q in Que:Map[q[0]][q[1]][q[2]]=0
    while Que:
        y,x,t=Que.popleft()
        for d in range(4):
            Y,X=y+dy[d],x+dx[d]
            if IS(Y,X) and Arr[Y][X]!='*' and Map[Y][X][t]==-1:
                L=Map[y][x][t]
                if Arr[Y][X]=='#':
                    Map[Y][X][t]=Map[y][x][t]+1
                    Que.append((Y,X,t))
                elif Arr[Y][X]=='.':
                    Map[Y][X][t]=Map[y][x][t]
                    Que.appendleft((Y,X,t))
    for i in range(H+2):
        for j in range(W+2):
            if Arr[i][j]=='*':continue
            r=sum(Map[i][j])
            if Arr[i][j]=='#':r-=2
            R=min(R,r)
    print(R)