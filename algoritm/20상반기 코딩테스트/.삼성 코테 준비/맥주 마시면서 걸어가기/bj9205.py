import sys
sys.stdin = open('bj9205.txt','r')

def DFS(y,x):
    global R
    if abs(y-eY)+abs(x-eX)<=1000:
        R='happy'
        return
    for i,(Y,X) in enumerate(L):
        if V[i] or abs(y-Y)+abs(x-X)>1000:continue
        V[i]=1
        DFS(Y,X)
for t in range(int(input())):
    N=int(input())
    sY,sX=map(int,input().split())
    L=[[int(x)for x in input().split()]for y in range(N)]
    eY,eX=map(int,input().split())
    V=[0]*N
    R='sad'
    DFS(sY,sX)
    print(R)

# from collections import deque
# for t in range(int(input())):
#     N=int(input())
#     sY,sX=map(int,input().split())
#     L=[list(map(int,input().split()))for _ in range(N)]
#     eY,eX=map(int,input().split())
#     V=[0]*N
#     Q=deque([(sY,sX)])
#     R='sad'
#     while Q:
#         y,x=Q.popleft()
#         if abs(y-eY)+abs(x-eX)<=1000:R='happy';break
#         for i,(Y,X) in enumerate(L):
#             if V[i] or abs(y-Y)+abs(x-X)>1000:continue
#             V[i]=1
#             Q.append((Y,X))
#     print(R)