import sys
sys.stdin= open('bj1348.txt','r')

# from collections import deque
# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# def IS(y,x):
#     return -1<y<R and -1<x<C
# def DFS(n):
#     if m[n]:return False
#     m[n]=1
#     for i in range(1,P-99):
#         if not Dis[i][n]:continue
#         if Dis[i][n]<=Mid and (Pa[i]==-1 or(not m[Pa[i]] and DFS(Pa[i]))):
#             Car[n]=i
#             Pa[i]=n
#             return True
#     return False
#
# R,C=map(int,input().split())
# Arr=[list(map(str,input()))for _ in range(R)]
# tmp,P=0,100
# Q=[]
# for i in range(R):
#     for j in range(C):
#         if Arr[i][j]=='C':tmp+=1;Arr[i][j]=tmp;Q.append((i,j,tmp,0))
#         elif Arr[i][j]=='P':P+=1;Arr[i][j]=P
#         elif Arr[i][j]=='.':Arr[i][j]=0
# if not tmp:print(0)
# elif tmp>P:print(-1)
# else:
#     Dis=[[0]*(tmp+1) for _ in range(P-99)]
#     for q in Q:
#         Map=[[0]*C for _ in range(R)]
#         Que=deque([q])
#         while Que:
#             y,x,tmp,dis=Que.popleft()
#             for d in range(4):
#                 Y,X,nd=y+dy[d],x+dx[d],dis+1
#                 if IS(Y,X) and not Map[Y][X] and Arr[Y][X]!='X':
#                     if Arr[Y][X]-100>0:
#                         Dis[Arr[Y][X]-100][tmp]=nd
#                     Map[Y][X]=tmp
#                     Que.append((Y,X,tmp,nd))
#     Pa=[-1]*(P-99)
#     Car=[-1]*(tmp+1)
#     match,Mid=0,999999
#     for c in range(1,tmp+1):
#         m=[0]*(tmp+1)
#         if DFS(c):match+=1
#     if match!=tmp:print(-1)
#     else:
#         Low,High=0,R*C
#         while Low+1<High:
#             Mid=(Low+High)//2
#             match=0
#             Pa=[-1]*(P-99)
#             Car=[-1]*(tmp+1)
#             for c in range(1,tmp+1):
#                 if Car[c]==-1:
#                     m=[0]*(tmp+1)
#                     if DFS(c):match+=1
#             if match==tmp:High=Mid
#             else:Low=Mid
#         print(High)
#


def dfs(x,t):
    visited[x]=1
    for nt,nx in path[x]:
        if nt>t:break
        if P[nx]==-1 or (not visited[P[nx]] and dfs(P[nx],t)):
            C[x]=nx;P[nx]=x;Z[x]=nt
            return 1
    return 0
def bfs(A):
    global r
    q=deque([[A[0],A[1],0]])
    visited=[[-1]*m for _ in range(n)]
    visited[A[0]][A[1]]=0
    while q:
        x,y,t=q.popleft()
        for k in range(4):
            nx,ny=x+dx[k],y+dy[k]
            if 0<=nx<n and 0<=ny<m and D[nx][ny]!='X' and visited[nx][ny]==-1:
                visited[nx][ny]=t+1;q.append([nx,ny,t+1]);r=max(t+1,r)
                if D[nx][ny]=='P':path[i].append([t+1,Num[nx][ny]])
from collections import deque
dx,dy=[0,0,1,-1],[1,-1,0,0]
n,m=map(int,input().split())
D=[input() for _ in range(n)]
Num=[[-1]*m for _ in range(n)];num=0
Car=[]
for i in range(n):
    for j in range(m):
        if D[i][j]=='C':Car.append([i,j])
        if D[i][j]=='P':Num[i][j]=num;num+=1
if len(Car)==0:print(0);exit(0)
if len(Car)>num:print(-1);exit(0)
path=[[] for _ in range(len(Car))]
l,r=0,0
for i in range(len(Car)):
    bfs(Car[i])
    path[i]=sorted(path[i])
res=-1
while l<=r:
    m=(l+r)//2
    C=[-1]*len(Car)
    P=[-1]*num
    Z=[-1]*len(Car)
    ans=0
    for i in range(len(Car)):
        if C[i]==-1:
            visited=[0]*len(Car)
            if dfs(i,m):ans+=1
    if ans==len(Car):
        res=max(Z)
        r=m-1
    else:l=m+1
print(res)