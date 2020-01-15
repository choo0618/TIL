import sys
sys.stdin = open('bj1113.txt','r')

# N,M=map(int,input().split())
# Arr=[]
# Min,R=987654321,0
# try:
#     for i in range(N):
#         I=list(map(int,input()))
#         Arr.append(I)
#         if i==0 or i==N-1:
#             for ii in range(1,M-1):
#                 if I[ii]<Min:Min=I[ii]
#                 # if min(I[1:M-2])<Min:Min=min(I[1:M-2])
#         else:
#             if min(I[0],I[M-1])<Min:Min=min(I[0],I[M-1])
#     for i in range(1,N-1):
#         for j in range(1,M-1):
#             if Arr[i][j]<Min:R+=Min-Arr[i][j]
# except:pass
# print(R)

# dx=[1,0,-1,0]
# dy=[0,1,0,-1]
# def BFS(i,j,n):
#     global R
#     Min = 987654321
#     Que = [(i,j)]
#     Map[i][j]=n
#     while Que:
#         Q=[]
#         for q in Que:
#             Map[q[0]][q[1]] = n
#             for dir in range(4):
#                 nY = q[0]+dy[dir]
#                 nX = q[1]+dx[dir]
#                 if Map[nY][nX] and Map[nY][nX]!=n and Arr[nY][nX]<Min:Min=Arr[nY][nX]
#                 if not Map[nY][nX] and Arr[nY][nX]>=Arr[q[0]][q[1]]:
#                     if not nY or nY==N-1 or not nX or nX==M-1:
#                         if Arr[nY][nX]<Min:Min=Arr[nY][nX]
#                     else:
#                         if Arr[nY][nX] > Arr[q[0]][q[1]] and Arr[nY][nX]<Min:
#                             Min = Arr[nY][nX]
#                         Map[nY][nX]=n
#                         Q.append((nY,nX))
#         Que=Q
#     for i1 in range(1,N-1):
#         for j1 in range(1,M-1):
#             if Map[i1][j1]==n and Arr[i1][j1]<Min:
#                 R+=Min-Arr[i1][j1]
# N,M=map(int,input().split())
# Arr = [list(map(int,input()))for y in range(N)]
# Map = [[0]*M for m in range(N)]
# R,n = 0,1
# for i in range(1,N-1):
#     for j in range(1,M-1):
#         if not Map[i][j]:
#             BFS(i,j,n)
#             n+=1
# print(R)

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def BFS(y,x,tmp):
    Que = [[y,x]]
    Map[y][x]=tmp
    mi=987654321
    while Que:
        Q = []
        for q in Que:
            for d in range(4):
                nY=q[0]+dy[d]
                nX=q[1]+dx[d]
                if not Map[nY][nX]:
                    Map[nY][nX]=tmp
                    Q.append([nY,nX])
                elif Map[nY][nX]==1:
                    if Arr[nY][nX]<=Arr[q[0]][q[1]]:
                        Map[q[0]][q[1]]=1
                        mi = Arr[q[0]][q[1]]
                    elif Arr[nY][nX]<mi:mi=Arr[nY][nX]
        Que=Q
    Min[tmp] = mi
N,M=map(int,input().split())
Arr,Max,tmp = [],0,2
for i in range(N):
    I = list(map(int,input()))
    Arr.append(I)
    if i==0 or i==N-1:
        if max(I)>Max:Max=max(I)
    else:
        if max(I[0],I[M-1])>Max:Max=max(I[0],I[M-1])
Map,Min,R = [[0]*M for m in range(N)],[0,Max],0
for i in range(N):
    for j in range(M):
        if not i or i==M-1 or not j or j==M-1 or Arr[i][j]>=Max:Map[i][j]=1
for i in range(1,N-1):
    for j in range(1,M-1):
        if not Map[i][j]:
            Min.append(0)
            BFS(i,j,tmp)
            tmp+=1
for i in range(1,N-1):
    for j in range(1,M-1):
        if Map[i][j]!=1:R+=Min[Map[i][j]]-Arr[i][j]
print(R)
