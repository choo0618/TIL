import sys
sys.stdin=open('input.txt','r')

# # 보급로
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# def IsPossible(y, x):
#     if -1<y<N and -1<x<N:
#         return True
#     else:return False
# def DFS(y,x,s):
#     global S
#     if y==x==N-1:
#         if s<S:S=s
#         return
#     if s>=S:return
#     for dir in range(4):
#         if IsPossible(y+dy[dir],x+dx[dir]):
#             newY=y+dy[dir]
#             newX=x+dx[dir]
#             if M[newY][newX]>s:
#                 M[newY][newX]=s
#                 DFS(newY,newX,s+A[newY][newX])
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[list(map(int,input()))for y in range(N)]
#     M=[[999]*N for _ in range(N)]
#     S=987654321
#     DFS(0,0,0)
#     print('#%d %d'%((n+1),S))

# 전깃줄1
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
A.sort()
L=[0]*N
for j in range(N):
    L[j]=1
    max1=0
    for i in range(j-1,-1,-1):
        if A[j][1]>A[i][1]:
            max1=int(L[i]+1)
            if max1>L[j]:
                L[j]=max1
print(N-max(L))
M2=max(L)
for z in range(M2,-1,-1):
    