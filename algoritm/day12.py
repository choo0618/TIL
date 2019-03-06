import sys
sys.stdin = open("input.txt", "r")

# # 테이블
# L=[int(x) for x in input().split()]
# print(L)
# B=[[0]*5 for y in range(14)]  # L R 자녀 부모 레벨
# for x in range(0,len(L),2):
#     if not B[L[x]][0]:
#         B[L[x]][0]=L[x+1]       # L
#     else:
#         B[L[x]][1]=L[x+1]       # R
#     B[L[x]][2]+=1               # 자녀수
#     B[L[x+1]][3]=L[x]           # 부모
#     B[L[x+1]][4]=B[L[x]][4]+1   # 레벨
# print(B)

# # 전위 순회
# def preorder_traverse(T):
#     if T:
#         print(T, end=' ')
#         preorder_traverse(B[T][0])
#         preorder_traverse(B[T][1])
# preorder_traverse(1)

# # 중위 순회
# def inorder_traverse(T):
#     if T:
#         inorder_traverse(B[T][0])
#         print(T, end=' ')
#         inorder_traverse(B[T][1])
# inorder_traverse(1)

# # 후위 순회
# def postorder_traverse(T):
#     if T:
#         postorder_traverse(B[T][0])
#         postorder_traverse(B[T][1])
#         print(T, end=' ')
# postorder_traverse(1)
#
# # 13의 모든 부모
# x=13
# while B[x][3]:
#     print(B[x][3], end=' ')
#     x=B[x][3]

# # 몇촌일까?
# x=[8,6]
# y=[]
# cnt=0
# for n in range(2):
#     while B[x[n]][3]:
#         if not B[x[n]][3] in y:
#             y.append(B[x[n]][3])
# print(y)

# 이진 힙
TC=int(input())
for n in range(TC):
    N=int(input())
    L=[int(x) for x in input().split()]
    L.insert(0,0)
    B=[[0]*2 for y in range(max(L)+1)]
    for x in range(1,len(L)//2):
        B[L[x]][0]=L[2*x]       # L
        B[L[x]][1]=L[2*x+1]     # R
    print(B)