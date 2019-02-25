import sys
sys.stdin = open("input.txt", "r")

# Binary Search (재귀)

# # 배열 최소 합
# def J(y):
#     global ans, minsum
#     if ans>=minsum:
#         return
#     if y==L:
#         if ans<minsum:
#             minsum=ans
#             return
#     for x in range(L):
#         if not visited[x]:
#             visited[x]=True
#             ans+=A[y][x]
#             J(y+1)
#             visited[x]=False
#             ans-=A[y][x]
# N = int(input())
# for n in range(N):
#     L=int(input())
#     A=[[int(x) for x in input().split()]for y in range(L)]
#     visited=[0]*L
#     ans = 0
#     minsum = 987654321
#     J(0)
#     print(f'#{n+1} {minsum}')

# # 준혁이의 여자친구 만나러 가는길
# P=[int(x) for x in input().split()]
# A=[[int(x) for x in input().split()]for y in range(P[1])]
# MyMap = [[0]*(P[0]+1) for i in range(P[0]+1)]
# L = sum(A, [])
# print(L)
# for i in range(0,len(L),3):
#     MyMap[L[i]][L[i+1]]=L[i+2]
#     MyMap[L[i+1]][L[i]] = L[i+2]
# print(MyMap)

# 토너먼트 카드게임
def T(start):
    if start==N:
        return
    if L[start] - L[start+1] == 1 or L[start] - L[start+1] == -2:
        stack.append(L[start])
    else:
        stack.append(L[start + 1])
    print(stack)
    T(start+2)


N=int(input())
L=[int(x) for x in input().split()]
stack=[]
num=[]
T(N//2)
print(stack)
# for match in range(N-1):
#     for i in range(0,len(L),2):
#         if L[i]-L[i+1]>=0 and L[i]-L[i+1]!=2:
#             stack.append(L[i])
#             num.append(i)
#         else:
#             stack.append(L[i+1])
#             num.append(i+1)
#     print(stack)
#     print(num)







