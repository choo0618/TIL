import sys
sys.stdin = open('bj11724.txt','r')

def BFS(y,x,t):
    Que=[[y,x]]
    Map[y]=t
    Map[x]=t
    while Que:
        Q=[]
        for q in Que:
            for n in range(N):
                if m[q[1]][n] and not Map[n]:
                    Map[n]=t
                    Q.append([q[1],n])
        Que=Q

N,M=map(int,input().split())
Map=[0]*N
m=[[0]*N for _ in range(N)]
for i in range(M):
    y,x=map(int,input().split())
    m[y-1][x-1]=1
    m[x-1][y-1]=1
T,tmp=1,0
for i in range(N):
    Check=0
    for j in range(N):
        if m[i][j] and not Map[j]:
            Check=1
            BFS(i,j,T)
    if Check:T+=1
    if Map[i]==0:tmp+=1
print(T+tmp-1)