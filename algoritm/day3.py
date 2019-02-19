import sys
sys.stdin = open("input.txt", "r")
# A = [[int(x) for x in input().split()]for y in range(num)]
# # 4방향 합
# def IsSafe(y,x):
#     if x>=0 and x<5 and y>=0 and y<5: return True
#     else: return False
#
# def Mycalc(a,b):
#     if a>b: return a-b
#     else: return b-a
#
#
# Data = [[0 for _ in range(5)]for _ in range(5)]
# for i in range(5):
#     Data[i] = list(map(int,input().split()))
#
#
# dy = [-1,1,0,0]
# dx = [0,0,-1,1]
#
# sum = 0
# for y in range(5):
#     for x in range(5):
#         for dir in range(4):
#             newY = y + dy[dir]
#             newX = x + dx[dir]
#             if IsSafe(newY,newX):
#                 sum +=Mycalc(Data[y][x], Data[newY][newX])
# print(sum)
#
# # 부분집합
# L = list(map(int, input().split()))
# n = len(L)
# cnt = 0
# for i in range(1<<n):
#     result=[]
#     for j in range(n+1):
#         if i & (1<<j):
#             result.append(L[j])
#     print(result)
#     if sum(result)==0:
#         print(result)
#         cnt += 1
# print(cnt)
#
#
# # Sequential Search
# N = int(input())
# L = list(map(int, input().split()))
# for s in L:
#     if s==N:
#         print(True)
#         break
#     elif N<s:
#         print(False)
#         break
#
# # Binary Search
# N = int(input())
# L = list(map(int, input().split()))
# n = len(L)
# start,end = 0,n-1
# IsDone = False
# while start<=end:
#     mid = (start + end) // 2
#     if N == L[mid]:
#         print(True)
#         IsDone = True
#         break
#     elif N>L[mid]:
#         start = mid+1
#     else:
#         end = mid-1
# if IsDone == False:
#     print(False)
#
# # 선택 정렬 과정
# L = list(map(int, input().split()))
# n = len(L)
# for a in range(n-1):
#     min = 9999
#     c=0
#     for b in range(a+1,n):
#         if L[b]<min:
#             min=L[b]
#             c = b
#     if L[a] > min:
#         L[a],L[c] = L[c],L[a]
# print(L)
#
#
# # Sum
# for n in range(10):
#     N=int(input())
#     A=[[int(x) for x in input().split()]for y in range(100)]
#     a,b,c,d=0,0,0,0
#     for i in range(100):
#         if sum(A[i])>a:
#             a=sum(A[i])
#         e=sum([col[i] for col in A])
#         if b<e:
#             b=e
#         c+=A[i][i]
#         d+=A[i][99-i]
#     print("#%d %d"%(N,max(a,b,c,d)))
#
#
# # 달팽이
n=5
for y in range(n):
    for x in range(n):
        a=0
        m=min(x,y,n-x-1,n-y-1)
        if x>=y:
            a=x+y+1-2*m
        else:
            a=(n-1-2*m)*4-(x+y-2*m)+1
        print("%d"%(a), end=" ")
    print()