import sys
sys.stdin=open('input.txt','r')

# # 동철이의 일분배
# def C(n,r):
#     global R
#     if n==N:
#         if r>R:
#             R=r
#         return
#     if r<=R:
#         return
#     for y in range(N):
#         if not M[y]:
#             M[y]=A[n][y]
#             C(n+1,r*A[n][y])
#             M[y]=0
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)*0.01for x in input().split()]for y in range(N)]
#     M=[0]*N
#     R=0
#     C(0,1)
#     print('#%d %0.6f'%(n+1,round(100*R,6)))

# # 최소합
# dx=[1,0]
# dy=[0,1]
# def IsPossible(y,x):
#     if -1<y<N and -1<x<N:
#         return True
#     else:
#         return False
# def C(y,x,s):
#     global R
#     if s>R:
#         return
#     if y==x==N-1:
#         if s<R:
#             R=s
#         return
#     for dir in range(2):
#         if IsPossible(y+dy[dir],x+dx[dir]):
#             newY=y+dy[dir]
#             newX=x+dx[dir]
#             C(newY,newX,s+A[newY][newX])
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     M=[0]*N
#     R=987654321
#     S=0
#     C(0,0,A[0][0])
#     print('#%d %d'%((n+1),R))

# # 전자카트
# def C(n,s,c):
#     global R
#     if c==N-1:
#         s+=A[n][0]
#         if s<R:R=s
#         return
#     if s>R:return
#     for y in range(N):
#         if not M[y] and A[n][y]:
#             M[y]=1
#             C(y,s+A[n][y],c+1)
#             M[y]=0
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     M=[0]*N
#     M[0]=1
#     R=987654321
#     C(0,0,0)
#     print('#%d %d'%((n+1),R))

# # 컨테이너 운반
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(2)]
#     A[0].sort(reverse=True)
#     A[1].sort(reverse=True)
#     R=0
#     for j in range(L[0]):
#         for i in range(len(A[1])):
#             if A[0][j]<=A[1][i]:
#                 R+=A[0][j]
#                 A[1].pop(i)
#                 break
#     print('#%d %d'%((n+1),R))

# # 화물도크
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     A.sort(key=lambda x: x[1])
#     M=[]
#     i=0
#     while i!=len(A)-1:
#         if A[i][1]>A[i+1][0]:
#             A.pop(i+1)
#         else:i+=1
#     print('#%d %d'%((n+1),len(A)))

# 베이비진게임


# # 최적경로
# def C(n,s,c):
#     global R
#     if c==N:
#         s+=M[n][1]
#         if R>s:R=s
#         return
#     if s>R:return
#     for y in range(N+2):
#         if not M1[y]:
#             M1[y]=1
#             C(y,s+M[n][y],c+1)
#             M1[y]=0
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[int(x)for x in input().split()]
#     M=[[0]*(N+2)for _ in range(N+2)]
#     M1=[1]*2+[0]*N
#     R=987654321
#     for j in range(0,N*2+4,2):
#         for i in range(j+2,N*2+4,2):
#             M[j//2][i//2]=M[i//2][j//2]=abs(A[j]-A[i])+abs(A[j+1]-A[i+1])
#     C(0,0,0)
#     print('#%d %d'%((n+1),R))