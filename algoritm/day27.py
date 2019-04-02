import sys
sys.stdin=open('input.txt','r')

# 병합정렬

# 퀵정렬

# 이진탐색

# # 전기버스 2
# def DFS(which,battery,c):
#     global R
#     if which>=L[0]:
#         if c<R:R=c;return
#     if c>=R:
#         return
#     for i in range(battery,-1,-1):
#         if which+i<=L[0]:
#             DFS(which+i,L[which+i],c+1)
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     L.append(0)
#     R=987654321
#     DFS(1,L[1],0)
#     print('#%d %d'%((n+1),(R-1)))

# # 최소생산비용
# def C(n,r):
#     global R
#     if n==N:
#         if R>r:
#             R=r
#         return
#     if r>=R:
#         return
#     for y in range(N):
#         if not M[y]:
#             M[y]=A[n][y]
#             C(n+1,r+A[n][y])
#             M[y]=0
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     M=[0]*N
#     R=987654321
#     C(0,1)
#     print('#%d %d'%(n+1,R-1))