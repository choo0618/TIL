import sys
sys.stdin = open('bj1981.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
def BFS(y,x,Min,Max):
    if Min<=Arr[y][x]<=Max:
        Que=[(y,x)]
        Map[0][0]=1
    else:return
    while Que:
        Q=[]
        for q in Que:
            for d in range(4):
                Y,X=q[0]+dy[d],q[1]+dx[d]
                if IS(Y,X) and not Map[Y][X] and Min<=Arr[Y][X]<=Max:
                    Map[Y][X]=1
                    Q.append((Y,X))
        Que=Q
N=int(input())
Arr=[[int(x)for x in input().split()]for y in range(N)]
Set=set()
for a in Arr:
    for n in a:Set.add(n)
L=list(Set)
L.sort()
Low,High,ML=0,L.index(Arr[N-1][N-1]),L.index(Arr[0][0])
R=987654321
while Low<=ML:
    Map=[[0]*N for _ in range(N)]
    BFS(0,0,L[Low],L[High])
    if Map[N-1][N-1]:
        R=min(R,L[High]-L[Low])
        Low+=1
    elif High+1<len(L):High+=1
    else:break
print(R)