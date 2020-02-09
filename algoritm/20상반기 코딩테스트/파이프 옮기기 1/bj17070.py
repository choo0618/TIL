import sys
sys.stdin=open('bj17070.txt','r')

# dx=[1,0,1]
# dy=[0,1,1]
# def IS(y,x):
#     return -1<y<N and -1<x<N
# def DFS(y,x,d):
#     R=0
#     if (x,y)==(N-1,N-1):return 1
#     for dir in range(3):
#         if d+dir==1:continue
#         Y,X=y+dy[dir],x+dx[dir]
#         if not IS(Y,X):continue
#         if dir==2 and (Arr[x][y+1] or Arr[x+1][y]):continue
#         R+=DFS(Y,X,dir)
#     return R
# N=int(input())
# Arr=[[int(x)for x in input().split()]for y in range(N)]
# print(DFS(0, 1, 0))

# from collections import deque
# dx=[1,0,1]
# dy=[0,1,1]
# Dic={0:1,1:0,2:-1}
# def IS(y,x):
#     return -1<y<N and -1<x<N
# def Check(y,x):
#     for d in range(2):
#         Y,X=y+dy[d],x+dx[d]
#         if not IS(Y,X) or Arr[Y][X]:return False
#     return True
# N=int(input())
# Arr=[[int(x)for x in input().split()]for y in range(N)]
# Map=[[[0,0,0]for _ in range(N)]for __ in range(N)]
# Que=deque([(0,1,0)])
# Map[0][1][0]=1
# R=0
# while Que:
#     y,x,dir=Que.popleft()
#     if (y,x)==(N-1,N-1):R+=1;continue
#     for d in range(3):
#         if Dic[dir]==d or (d==2 and not Check(y,x)):continue
#         Y,X=y+dy[d],x+dx[d]
#         if IS(Y,X) and not Arr[Y][X]:
#             if d==2:Map[Y][X][2]=
#             else:
#                 Map[Y][X][d]=1
#                 Que.append((Y,X,d))
# print(Map[N-1][N-1])


N=int(input())
Arr=[[int(x)for x in input().split()]for y in range(N)]
Map=[[[0,0,0]for _ in range(N)]for __ in range(N)]
Map[0][1][0]=1
for x in range(2,N):
    if not Arr[0][x]:Map[0][x][0]=Map[0][x-1][0]
for y in range(N):
    for x in range(2,N):
        if Arr[y][x]==Arr[y-1][x]==Arr[y][x-1]==0:
            Map[y][x][2]=Map[y-1][x-1][0]+Map[y-1][x-1][1]+Map[y-1][x-1][2]
        if not Arr[y][x]:
            Map[y][x][0]=Map[y][x-1][2]+Map[y][x-1][0]
            Map[y][x][1]=Map[y-1][x][2]+Map[y-1][x][1]
print(sum(Map[-1][-1]))

# def pipe(x,y,d):
#     global ans
#     if x==N-1==y:ans+=1
#     if (d==0 or d==1) and y+1<N and A[x][y+1]==0:pipe(x,y+1,0)
#     if x+1<N and y+1<N and A[x][y+1]==A[x+1][y]==A[x+1][y+1]==0:pipe(x+1,y+1,1)
#     if (d==1 or d==2) and x+1<N and A[x+1][y]==0:pipe(x+1,y,2)
# N=int(input())
# A=[[int(x)for x in input().split()] for _ in range(N)]
# ans=0
# pipe(0,1,0)
# print(ans)

