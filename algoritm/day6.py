# import sys
# sys.stdin = open("input.txt", "r")
#
# # # 종이 붙이기
# def Paper(here):
#     global ans
#     if here == howmany:
#         if howmany!=0:
#             ans += 1
#             return
#     if here > howmany: return
#     Paper(here + 10)
#     Paper(here + 20)
#     Paper(here + 20)
# N = int(input())
# for n in range(N):
#     ans = 0
#     howmany = int(input())
#     start = 0
#     Paper(start)
#     print("#%d %d"%(n+1,ans))


# # 괄호 검사
# stack = [0]*1000
# top = -1
#
# info = [0] * 128
#
# info[ord(')')] = '('
# info[ord('}')] = '{'
#
#
# N = int(input())
# for n in range(N):
#     stack = [0] * 1000
#     top = -1
#     Data = input()
#     for c in Data:
#         if c=='(' or c=='{':
#             top += 1
#             stack[top] = str(c)
#         elif c==')' or c=='}':
#             if info[ord(c)] == stack[top]:
#                 stack.pop(top)
#                 top -= 1
#             else:
#                 top=99999
#                 break
#     if top==-1:print(f'#{n+1} 1')
#     else:print(f'#{n+1} 0')


# # 그래프 경로
# def DFS(here):
#     visited[here] = True
#     for next in range(P[0] + 1):
#         if MyMap[here][next] and not visited[next]:
#             DFS(next)
#
# N = int(input())
# for n in range(N):
#     P=[int(x) for x in input().split()]
#     L=[[int(x) for x in input().split()]for y in range(P[1])]
#     G=[int(x) for x in input().split()]
#     MyMap = [[0]*(P[0]+1) for i in range(P[0]+1)]
#     visited=[0]*(P[0]+1)
#
#     for i in range(P[1]):
#         Start=L[i][0]
#         Stop=L[i][1]
#         MyMap[Start][Stop]=1
#     DFS(G[0])
#     if visited[G[1]]:
#         print(f'#{n+1} 1')
#     else:
#         print(f'#{n+1} 0')


# # 반복문자
# N = int(input())
# for n in range(N):
#     stack = [0] * 1000
#     top = -1
#     Data = input()
#
#     for c in Data:
#         top+=1
#         stack[top]=c
#         if stack[top]==stack[top-1]:
#             stack.pop(top)
#             stack.pop((top-1))
#             top-=2
#         print(stack)
#     cnt=0
#     for cn in stack:
#         if cn:
#             cnt+=1
#     print(f'#{n+1} {cnt}')



# stack=[0]*10000
# top = -1
# MyMap = [[0]*8 for i in range(8)]
# visited=[0]*8
#
# def push(x):
#     global top
#     top += 1
#     stack[top] = x
#
# def pop():
#     global top
#     if top ==-1: return 0
#     x = stack[top]
#     top -= 1
#     return x
#
# def findnext(here):
#     for next in range(8):
#         if MyMap[here][next] and not visited[next]:
#             return next
#
# def DFS(here):
#     global top
#     print(here)
#     visited[here] = True
#     while here:
#         next = findnext(here)
#         if next: push(here)
#         while next :
#             here = next
#             print(here)
#             visited[here] = True
#             next = findnext(here)
#             push(here)
#         here = pop()
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

# 작업순서
# for n in range(10):
#     P=[int(x)for x in input().split()]
#     L=[int(x)for x in input().split()]
#     m=[[0]*(P[0]+1)for i in range(P[0]+1)]
#     for i in range(0,len(L),2):
#         m[L[i+1]][L[i]]=1
#     A=[]
#     while len(A)!=P[0]:
#         for i in range(1,len(m)):
#             if sum(m[i])==0:
#                 if i not in A:
#                     A.append(i)
#                     for j in range(1,len(m)):
#                         if m[j][i]==1:
#                             m[j][i]-=1
#     print(f'#{n+1} {" ".join(map(str,A))}')