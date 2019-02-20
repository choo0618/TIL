import sys
sys.stdin = open("input.txt", "r")

stack = [0]*10  # 시험시 10000
top = -1

# for i in range(1,4):
#     top+=1
#     stack[top]=i
#     # stack.append(i)
#
# while top!=-1:
#     print(stack[top])
#     top-=1
# # while stack:
# #    print(stack.pop())

# append로 받게되면 뒤에서부터 들어가기때문에 top 연산 반대로

# # 괄호검사
# Data=input()
# for c in Data:
#     if c=='(':
#         top-=1
#         stack.append(c)
#         # stack[top]=str(c)
#     elif c ==')':
#         top+=1
#         stack.pop(top)
# if top==-1:print("O")
# else:print("X")

# # 여러 괄호
# info = [0] * 128 # char 1byte ASCII code 7bit
# Data = input()
#
# info[ord(')')] = '('
# info[ord(']')] = '['
# info[ord('>')] = '<'
# info[ord('}')] = '{'
#
# for c in Data:
#     if c=='(' or c=='{' or c=='[' or c=='<':
#         top += 1
#         stack[top] = str(c)
#     elif info[ord(c)] == stack[top]:
#         stack.pop(top)
#         top -= 1
#     else:
#         top-=99999
#         break
# if top==-1:print("O")
# else:print("X")

# # stairs
# ans=0
#
# def GetSome(here):
#     global ans
#     if here==howmany:
#         ans+=1
#         return
#     if here>howmany:return
#     GetSome(here+1)
#     GetSome(here+2)
#
# howmany = int(input())
#
# start = 0
# GetSome(start)
#
# print("ans = %d"%ans)

# # 연습문제3
# MyMap = [[0]*8 for i in range(8)]
# visited=[0]*8
#
# def DFS(here):
#     print(here, end=" ")
#     visited[here]=True
#
#     for next in range(8):
#         if MyMap[here][next] and not visited[next]:
#             DFS(next)
#
# Data=list(map(int,input().split()))
# howmany = int(len(Data)/2)
#
# for i in range(howmany):
#     Start=Data[i*2]
#     Stop=Data[i*2+1]
#     MyMap[Start][Stop]=1
#     MyMap[Stop][Start]=1
#
# DFS(1)

# # ladder-비재귀
# for n in range(10):
#     N=int(input())
#     A=[]
#     for y in range(100):
#         A.append([0]+[int(x)for x in input().split()]+[0])
#     x=A[99].index(2)
#     y=99
#     while y>0:
#         if A[y][x-1]:
#             while A[y][x-1]:
#                 x-=1
#             y-=1
#         elif A[y][x+1]:
#             while A[y][x+1]:
#                 x+=1
#             y-=1
#         else:
#             y-=1
#     print("#%d %d"%(N,x-1))

# ladder-재귀 모르겠음
ans=0
def Ladder(h,n):
    if h==0:
        ans=n
        return
    elif A[h][n-1]:
        while A[h][n-1]:
            n-=1
        h-=1
    elif A[h][n+1]:
        while A[h][n+1]:
            n+=1
        h-=1
    else:
        h-=1
    Ladder(h,n)
A=[]
for y in range(100):
    A.append([0]+[int(x)for x in input().split()]+[0])
x=A[99].index(2)

Ladder(99,x)

print(ans)



