import sys
sys.stdin = open("input.txt", "r")

# # 이진 힙
# TC=int(input())
# for n in range(TC):
#     N=int(input())
#     L=[int(x) for x in input().split()]
#     L.insert(0, 0)
#     B=[0]
#     B.append(L[1])
#     result=0
#     for x in range(2,len(L)):
#         B.append(L[x])
#         while B[x]<B[x//2]:
#             B[x],B[x//2]=B[x//2],B[x]
#             x=x//2
#     while N!=1:
#         N=N//2
#         result+=B[N]
#     print("#%d %d"%(n+1,result))

# # 예산관리
# B=int(input())
# n=int(input())
# L=[int(x) for x in input().split()]
# max=0
# for i in range(1<<n):
#     result=[]
#     for j in range(n+1):
#         if i&(1<<j):
#             result.append(L[j])
#         a=sum(result)
#         if a>max and a<=B:
#             max=a
# print("%d"%max)

# # 예산관리
# def DFS(x,sum):
#     global result
#     if sum>=40:
#         return
#     if x+1>n:
#         return
#     DFS(x+1,sum+L[x])
#     result.append(sum)
#     DFS(x+1,sum)
# B=int(input())
# n=int(input())
# L=[int(x) for x in input().split()]
# result=[]
# DFS(0,0)
# print(max(result))

# # 치즈
# dy=[0,0,-1,1]
# dx=[-1,1,0,0]
# def IsPossible(y, x):
#     if -1<y<N[0] and -1<x<N[1] and not visited[y][x] and A[y][x]!=1:
#         return True
#     else:
#         return False
#
# N=[int(x) for x in input().split()]
# A=[[int(x) for x in input().split()]for y in range(N[0])]

# # 사칙연산 유효성 검사
# for n in range(10):
#     N=int(input())
#     A=[[x for x in input().split()]for y in range(N)]
#     x=0
#     while x<N:
#         if x<N//2 and A[x][1].isdigit():
#             break
#         elif A[x][1].isalpha():
#             break
#         x+=1
#     if x==N:
#         print("#%d 1"%(n+1))
#     else:
#         print("#%d 0"%(n+1))

# # 중위순회
# def inorder(T):
#     if T:
#         inorder(B[T][0])
#         print(A[T-1][1], end='')
#         inorder(B[T][1])
# for n in range(10):
#     N=int(input())
#     A=[[x for x in input().split()]for y in range(N)]
#     B=[[0]*2 for x in range(N+1)]
#     for x in range(N//2):
#         if len(A[x])%2:
#             B[x+1][0]=int(A[x][2])
#         else:
#             B[x+1][0]=int(A[x][2])
#             B[x+1][1]=int(A[x][3])
#     print("#%d"%(n+1),end=' ')
#     inorder(1)
#     print()

# # 파스칼의 삼각형
# T=int(input())
# for num in range(T):
#     N=int(input())
#     L=[]
#     print("#%d"%(num+1))
#     for y in range(N):
#         l=[]
#         for x in range(y+1):
#             if x==0 or x==y:
#                 l.append(1)
#             else:
#                 l.append(L[y-1][x-1]+L[y-1][x])
#         L.append(l)
#     for n in range(len(L)):
#         print(" ".join(map(str,L[n])))

# # 사칙연산
# for n in range(10):
#     N=int(input())
#     A=[[x for x in input().split()]for y in range(N)]
#     A.insert(0,[])
#     for x in range(N,0,-1):
#         if len(A[x])==4:
#             r=A[x][1]
#             a=int(A[int(A[x][2])][1])
#             b=int(A[int(A[x][3])][1])
#             if r=='-':
#                 A[x][1]=a-b
#             elif r=='+':
#                 A[x][1]=a+b
#             elif r=='*':
#                 A[x][1]=a*b
#             else:
#                 A[x][1]=a/b
#     print("#%d %d"%(n+1,A[1][1]))

# # 농작물 수확하기
# N=int(input())
# A=[[x for x in input().split()]for y in range(N)]
# for y in range(N):
#     for x in range(N//2-y,N//2+y):
#         print(x,end=' ')
#     print()

# 단조 증가
T=int(input())
for n in range(T):
    N=int(input())
    L=[int(x) for x in input().split()]
    l=len(L)
    r=[]
    for y in range(l):
        for x in range(y+1,l):
            r.append(str(L[y]*L[x]))
    for x in range(len(r)):
        for i in range(0,len(r[x])-1):
            if int(r[x][i])>int(r[x][i+1]):
                r[x]=0
                break
        r[x]=int(r[x])
    if sum(r):
        print('#%d %d'%(n+1,max(r)))
    else:
        print('#%d -1'%(n+1))


    # # 다솔이의 다이아몬드 장식
# N=int(input())
# for n in range(N):
#     C=input()
#     l=len(C)
#     print('..'+'#...'*(l-1)+'#..')
#     print('.#'*(2*l)+'.')
#     print('#',end='')
#     for c in C:
#         print('.%s.#'%(c),end='')
#     print()
#     print('.#'*(2*l)+'.')
#     print('..'+'#...'*(l-1)+'#..')