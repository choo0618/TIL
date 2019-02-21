import sys
sys.stdin = open("input.txt", "r")

# 달팽이
# n=5
# for y in range(n):
#     for x in range(n):
#         a=0
#         m=min(x,y,n-x-1,n-y-1)
#         if x>=y:
#             a=x+y+1-2*m
#         else:
#             a=(n-1-2*m)*4-(x+y-2*m)+1
#         print("%d"%(a), end=" ")
#     print()


# 색칠하기
# TC=int(input())
# for n in range(TC):
#     N = int(input())
#     C = [[int(x) for x in input().split()]for y in range(N)]
#     space=[[0]*10 for y in range(10)]
#     cl=len(C)
#     cnt=0
#     for cn in range(cl):
#         for y in range(10):
#             if y>=C[cn][1] and y<=C[cn][3]:
#                 for x in range(C[cn][0],C[cn][2]+1):
#                     space[x][y]+=C[cn][4]
#                     if space[x][y] == 3:
#                         cnt+=1
#     print("#%d %d"%(n+1,cnt))


# 부분집합
# TC=int(input())
# for n in range(TC):
#     L= list(map(int, input().split()))
#     L1=[x+1 for x in range(12)]
#     cnt=0
#     for i in range(1 << len(L1)):
#         result = []
#         for j in range(len(L1) + 1):
#             if i & (1<<j):
#                 result.append(L1[j])
#         if len(result)==L[0] and sum(result)==L[1]:
#             cnt+=1
#             print("#%d %d"%(n+1,cnt))


# 이진탐색
# TC=int(input())
# for n in range(TC):
#     L= list(map(int, input().split()))
#     A,B=0,0
#     for m in range(2):
#         l,r=1,L[0]
#         mid=0
#         if m==0:
#             if L[m+1]==1 or L[m+1]==L[0]:
#                 continue
#             else:
#                 while l<=r:
#                     mid=(l+r)//2
#                     if L[m+1]==mid:
#                         A+=1
#                         break
#                     elif L[m+1]>mid:
#                         l=mid
#                         A+=1
#                     else:
#                         r=mid
#                         A+=1
#         else:
#             if L[m+1]==1 or L[m+1]==L[0]:
#                 continue
#             else:
#                 while l<=r:
#                     mid=(l+r)//2
#                     if L[m+1]==mid:
#                         B+=1
#                         break
#                     elif L[m+1]>mid:
#                         l=mid
#                         B+=1
#                     else:
#                         r=mid
#                         B+=1
#     result=""
#     if A<B:
#         result+="A"
#     elif A==B:
#         result+="0"
#     else:
#         result+="B"
#     print("#%d %s" % (n + 1, result))


# 특별한 정렬
# TC=int(input())
# for n in range(TC):
#     N = int(input())
#     L = list(map(int, input().split()))
#     for a in range(N-1):
#         for b in range(a+1,N):
#             if a % 2 == 1:
#                 if L[a]>L[b]:
#                     L[a],L[b]=L[b],L[a]
#             else:
#                 if L[a]<L[b]:
#                     L[a],L[b]=L[b],L[a]
#     print("#%d"%(n+1), end=" ")
#     for i in range(10):
#         print(L[i], end=" ")
#     print()


# 금속막대
# TC=int(input())
# for n in range(TC):
#     N=int(input())
#     L=list(map(int,input().split()))
#     A=[]
#     cnt=[0]*(max(L)+1)
#
#     for num in range(len(L)):
#         cnt[L[num]]+=1
#
#     for go in range(len(cnt)):
#         if cnt[go]==1 and L.index(go)%2==0:
#             A.extend([L[L.index(go)],L[L.index(go)+1]])
#
#     while len(A)!=len(L):
#         for plus in range(0,len(L),2):
#             if A[-1]==L[plus]:
#                 A.extend([L[plus],L[plus+1]])
#
#     print("#%d"%(n+1),end=" ")
#     for i in range(2*N):print(A[i], end=" ")
# #     print()