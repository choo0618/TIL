import sys
sys.stdin=open('input.txt','r')

# # 상원이의 생일파티
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(L[1])]
#     A.sort()
#     R=[[],[]]
#     for y in range(L[1]):
#         a=A[y][0]
#         b=A[y][1]
#         if a==1:R[0].append(b)
#         elif a in R[0] and not b in R[0] and not b in R[1]:R[1].append(b)
#         elif b in R[0] and not a in R[0] and not a in R[1]:R[1].append(a)
#     print(R)
#     print('#%d %d' % (n+1,len(R[0])+len(R[1])))

# # 격자판의 숫자 이어 붙이기
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# def IsSafe(y,x):
#     if -1<y<4 and -1<x<4:return True
#     else:return False
# def DFS(y,x,r):
#     r+=str(A[y][x])
#     if len(r)==7:
#         if not int(r) in R:
#             R.append(int(r))
#         return
#     for dir in range(4):
#         nY=y+dy[dir]
#         nX=x+dx[dir]
#         if IsSafe(nY,nX):
#             DFS(nY,nX,r)
# T=int(input())
# for n in range(T):
#     A=[[int(x)for x in input().split()]for y in range(4)]
#     R=[]
#     for y in range(4):
#         for x in range(4):
#             DFS(y,x,'')
#     print('#%d %d'%((n+1),len(R)))

# # 올림픽 종목투표
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     L1=[int(x)for x in input().split()]
#     L2=[int(x)for x in input().split()]
#     R=[0]*(L[0])
#     for y in L2:
#         t=0
#         while L1[t]>y:t+=1
#         R[t]+=1
#     print('#%d %d'%(n+1,R.index(max(R))+1))