import sys
sys.stdin = open('bj2411.txt','r')

# DP
N,M,a,b=map(int,input().split())
A=[[0]*(M+1)for _ in range(N+1)]
DP,t=[[[0]*(a+1) for _ in range(M+1)]for _ in range(N+1)],1
for _ in range(a+b):
    if _==a:t=-1
    y,x=map(int,input().split())
    A[y][x]=t
DP[0][1][0]=1
for i in range(1,N+1):
    for j in range(1,M+1):
        if A[i][j]==-1:continue
        s,e,t=0,a+1,0
        if A[i][j]:s=t=1
        for dp in range(s,e):DP[i][j][dp]=DP[i-1][j][dp-t]+DP[i][j-1][dp-t]
print(DP[-1][-1][a])

# # BFS 메모리초과
# from collections import deque
# def IS(y,x):
#     return -1<y<N and -1<x<M
# N,M,a,b=map(int,input().split())
# A,t=[[0]*M for _ in range(N)],1
# for _ in range(a+b):
#     if _==a:t=-1
#     y,x=map(int,input().split())
#     A[y-1][x-1]=t
# Q=deque([(0,0,0)])
# R=0
# while Q:
#     y,x,i=Q.popleft()
#     if (y,x)==(N-1,M-1) and i==a:R+=1
#     for Y,X in (y,x+1),(y+1,x):
#         if IS(Y,X) and A[Y][X]!=-1:
#             Q.append((Y,X,i+A[Y][X]))
# print(R)

