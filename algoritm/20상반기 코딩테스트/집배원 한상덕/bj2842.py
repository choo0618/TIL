import sys
sys.stdin = open('bj2842.txt','r')

dx=[1,1,1,0,0,-1,-1,-1]
dy=[-1,0,1,1,1,0,-1,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x,t):
    Que=[(y,x)]
    Map[y][x]=t
    while Que:
        Q=[]
        for q in Que:
            for d in range(8):
                Y,X=q[0]+dy[d],q[1]+dx[d]
                if IS(Y,X) and not Map[Y][X] and Min<=H[Y][X]<=Max:
                    Map[Y][X]=t
                    Q.append((Y,X))
        Que=Q
N=int(input())
A=[list(map(str,input()))for y in range(N)]
H=[[int(x)for x in input().split()]for y in range(N)]
Que,R,Sort=[],987654321,[]
# Min,Max=987654321,0
Min,Max=0,1
for i in range(N):
    for j in range(N):
        Sort.append(H[i][j])
        if A[i][j]!='.':
            Min=min(Min,H[i][j])
            Max=max(Max,H[i][j])
            Que.append((i,j))
Sort.sort()
print(Sort)
while True:
    Map,tmp=[[0]*N for _ in range(N)],1
    for q in Que:
        if not Map[q[0]][q[1]] and Sort[Min]<=A[q[0]][q[1]]<=Sort[Max]:BFS(q[0],q[1],tmp);tmp+=1

print(Max-Min)
