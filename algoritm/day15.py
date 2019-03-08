import sys
sys.stdin = open("input.txt", "r")

# # 간단한 압축 풀기
# T=int(input())
# for n in range(T):
#     N=int(input())
#     a=''
#     print("#%d"%(n+1))
#     for x in range(N):
#         L=[x for x in input().split()]
#         a+=(L[0]*int(L[1]))
#     p=0
#     for c in a:
#         if p%10==0 and not p==0:
#             print()
#         print(c,end='')
#         p+=1
#     print()

# # 두 개의 숫자열
# T=int(input())
# for n in range(T):
#     L=[int(x) for x in input().split()]
#     A=[[int(x) for x in input().split()]for y in range(2)]
#     R=0
#     if L[0]>L[1]:
#         L[0],L[1]=L[1],L[0]
#         A[0],A[1]=A[1],A[0]
#     for x in range(L[1]-L[0]+1):
#         r=0
#         for m in range(L[0]):
#             r+=A[0][m]*A[1][m+x]
#         if r>R:
#             R=r
#     print("#%d %d"%(n+1,R))

# # 추억의 2048 - runtime
# N=int(input())
# for num in range(N):
#     L=[x for x in input().split()]
#     n=int(L[0])
#     A=[[int(x) for x in input().split()]for y in range(n)]
#     M=[[0]*n for _ in range(n)]
#     W=0
#     if L[1]=='down':W=1
#     elif L[1]=='right':W=2
#     elif L[1]=='up':W=3
#     for _ in range(W):
#         A=list(map(list,zip(*A[::-1])))
#     for y in range(n):
#         for x in range(0,n-1):
#             if A[y][x] and A[y][x]==A[y][x+1]:
#                 A[y][x]*=2
#                 A[y][x+1]=0
#             elif A[y][x] and A[y][x+1]==0:
#                 for Q in range(x+1,n-x):
#                     if A[y][Q]:
#                         if A[y][x]==A[y][x+Q]:
#                             A[y][x]*=2
#                             A[y][x+Q]=0
#                         break
#     for j in range(n):
#         cnt = 0
#         for i in range(n):
#             if A[j][i]:
#                 M[j][cnt]=A[j][i]
#                 cnt+=1
#     if not W==0:
#         for _ in range(4-W):
#             M=list(map(list, zip(*M[::-1])))
#     print("#%d"%(num+1))
#     for R in range(n):
#         print(*M[R])

# # 추억의 2048
# N=int(input())
# for num in range(N):
#     L=[x for x in input().split()]
#     n=int(L[0])
#     A=[[int(x) for x in input().split()]for y in range(n)]
#     M=[[0]*n for _ in range(n)]
#     W=0
#     if L[1]=='down':W=1
#     elif L[1]=='right':W=2
#     elif L[1]=='up':W=3
#     for _ in range(W):
#         A=list(map(list,zip(*A[::-1])))
#     for y in range(n):
#         for x in range(0,n-1):
#             if A[y][x]:
#                 for Q in range(x+1,n):
#                     if A[y][Q]:
#                         if A[y][x]==A[y][Q]:
#                             A[y][x]*=2
#                             A[y][Q]=0
#                         break
#     for j in range(n):
#         cnt = 0
#         for i in range(n):
#             if A[j][i]:
#                 M[j][cnt]=A[j][i]
#                 cnt+=1
#     if not W==0:
#         for _ in range(4-W):
#             M=list(map(list, zip(*M[::-1])))
#     print("#%d"%(num+1))
#     for R in range(n):
#         print(*M[R])

# # 숫자 배열 회전
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     R=[]
#     for _ in range(N):
#         A=list(map(list,zip(*A[::-1])))
#         R.append(A)
#     print('#%d'%(n+1))
#     for y in range(N):
#         for x in range(3):
#             print(''.join(map(str,R[x][y])),end=' ')
#         print()

# # 가장 빠른 문자열 타이핑
# T=int(input())
# for n in range(T):
#     L=[x for x in input().split()]
#     l=len(L[1])
#     c,z=0,0
#     while z!=len(L[0]):
#         if L[0][z:l+z]==L[1]:
#             z+=l
#         else:
#             z+=1
#         c+=1
#     print('#%d %d'%(n+1,c))










