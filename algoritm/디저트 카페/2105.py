import sys
sys.stdin = open('2105.txt','r')

dx=[1,-1,-1,1]
dy=[1,1,-1,-1]
def IS(y,x):
    if -1<y<N and -1<x<N and not(y==0 and x==0) and not(y==0 and x==N-1) and  not(y==N-1 and x==0) and not(y==N-1 and x==N-1):return True
    return False
# def DFS(y,x):
#     global R
#     for dir in range(4):
#         if not d[dir]:
#             nY=y+dy[dir]
#             nX=x+dx[dir]
#             if IS(nY,nX):
#                 if not A[nY][nX] in r:
#                     r.append(A[nY][nX])
#                     DFS(nY,nX)
#                 else:d[dir]=1
#             else:d[dir]=1
#     if sum(d)==4 and len(r)>R:R=len(r);return
def BFS(y,x):

T=int(input())
for n in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R=-1
    for i in range(N):
        for j in range(1,N-1):
            Q,d=[[i,j]],[0,0,0,0]
            BFS(y,x)
    print('#%d %d'%(n+1,R))