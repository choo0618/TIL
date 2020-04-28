import sys
sys.stdin = open('bj13023.txt','r')

def DFS(n,o,d):
    global R
    if d==4:R=1;return
    if d>Max[o]:Max[o]=d
    if Max[n] and Max[n]+d<4:return
    V[n]=1
    for f in Map[n]:
        if V[f]:continue
        DFS(f,o,d+1)
        if R:return
    V[n]=0
N,M=map(int,input().split())
D=[0]*N
Map=[[]for _ in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    Map[a].append(b)
    Map[b].append(a)
R,V,Max=0,[0]*N,[0]*N
for i in range(N):
    DFS(i,i,0)
    if R:break
print(R)
