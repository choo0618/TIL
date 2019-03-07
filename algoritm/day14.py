import sys
sys.stdin = open("input.txt", "r")

# 단조 증가
T=int(input())
for n in range(T):
    N=int(input())
    L=[int(x) for x in input().split()]
    r=-1
    for y in range(len(L)):
        for x in range(y+1,l):
            a=L[y]*L[x]
            if a단조 and a>r:
                r=a
    for x in range(len(r)):
        for i in range(0,len(r[x])-1):
            if int(r[x][i])>int(r[x][i+1]):
                r[x]=0
                break
        r[x]=int(r[x])
    if sum(r):
        print('#%d %d'%(n+1,r))


# # 콤비네이션
# def C(num,count):
#     if count==L[1] or num>L[0]:
#         for x in range(len(visited)):
#             if visited[x]:
#                 print(x,end=" ")
#         print()
#         return
#     if num==L[0] and count!=L[1]:
#         return
#     visited[num+1]=1
#     C(num+1,count+1)
#     visited[num+1]=0
#     C(num+1,count)
# L=[int(x) for x in input().split()]
# visited=[0]*(10)
# C(0,0)

# # 의석이의 세로로 말해요
# n=int(input())
# for n in range(n):
#     L=[input() for x in range(5)]
#     m=max(len(x) for x in L)
#     print("#%d"%(n+1),end=' ')
#     for x in range(5):
#         while len(L[x])!=m:
#             L[x]+='*'
#     for y in range(m):
#         for x in range(5):
#             if L[x][y]!='*':
#                 print(L[x][y],end="")
#     print()

# 어디에 단어가 들어갈 수 있을까

# # 오셀로
# def O(y,x,z):
#     if G[y][x]!=A[z][2] and G[y][x]:
#         return True
#     else:
#         return False
# def T(y,x,p):
#     for t in range(L[0]+1):
#         c=y+(dy[d]*(t+1))
#         e=x+(dx[d]*(t+1))
#         if G[c][e]==A[p][2]:
#             return True
#         elif G[c][e]==0:
#             return False
# dy=[0,-1,-1,-1,0,1,1,1]
# dx=[-1,-1,0,1,1,1,0,-1]
# N=int(input())
# for n in range(N):
#     L=[int(x) for x in input().split()]
#     A=[[int(x) for x in input().split()] for y in range(L[1])]
#     G=[[0]*(L[0]+2)for y in range(L[0]+2)]
#     s=L[0]//2
#     G[s][s],G[s+1][s+1]=2,2
#     G[s][s+1],G[s+1][s]=1,1
#     for x in range(L[1]):
#         G[A[x][1]][A[x][0]]=A[x][2]
#         for d in range(8):
#             ny=A[x][1]+dy[d]
#             nx=A[x][0]+dx[d]
#             if O(ny,nx,x) and T(ny,nx,x):
#                 while G[ny][nx]!=A[x][2]:
#                     G[ny][nx]=A[x][2]
#                     ny+=dy[d]
#                     nx+=dx[d]
#     w,b=0,0
#     for i in range(L[0]+2):
#         for j in range(L[0]+2):
#             if G[i][j]==1:
#                 b+=1
#             elif G[i][j]==2:
#                 w+=1
#     print("#%d %d %d"%(n+1,b,w))

# # 파리 퇴치
# N=int(input())
# for n in range(N):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(L[0])]
#     R=0
#     for y in range(L[0]-L[1]+1):
#         for x in range(L[0]-L[1]+1):
#             sum=0
#             for i in range(L[1]):
#                 for j in range(L[1]):
#                     sum+=A[y+i][x+j]
#             if sum>R:
#                 R=sum
#     print('#%d %d'%(n+1,R))

# # 어디에 단어가 들어갈 수 있을까
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(L[0])]
#     cnt=0
#     for y in range(L[0]):
#         a=[]
#         for x in range(L[0]):
#             a.append(A[x][y])
#         A.append(a)
#     R=0
#     for r in range(len(A)):
#         c=0
#         for s in range(L[0]):
#             if A[r][s]==1:
#                 c+=1
#             else:
#                 if c==L[1]:
#                     R+=1
#                 c=0
#         if c==L[1]:
#             R+=1
#     print('#%d %d'%(n+1,R))

# Ladder 2
# for n in range(10):
#     N=int(input())
#     A=[]
#     for y in range(100):
#         A.append([0]+[int(x) for x in input().split()]+[0])
#     R=987654321
#     r=0
#     for x in range(101):
#         tmp=x
#         if A[0][x]==1:
#             cnt=0
#             y=0
#             while y!=100:
#                 if A[y][tmp-1]:
#                     while A[y][tmp-1]:
#                         tmp-=1
#                         cnt+=1
#                 elif A[y][tmp+1]:
#                     while A[y][tmp+1]:
#                         tmp+=1
#                         cnt+=1
#                 y+=1
#                 cnt+=1
#             if cnt<R:
#                 R=cnt
#                 r=x
#     print("#%d %d"%(N,r-1))