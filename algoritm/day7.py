# import sys
# sys.stdin = open("input.txt", "r")

# # Forth
# N = int(input())
# for n in range(N):
#     stack=[0]*1000
#     top=-1
#     L=[x for x in input().split()]
#
#     for c in range(len(L)):
#         if L[c].isdigit():
#             L[c]=int(L[c])
#     cnt=0
#     for z in range(len(L)):
#         if isinstance(L[z], int):
#             cnt+=1
#     if cnt==len(L)/2:
#         for cal in L:
#             if isinstance(cal, int):
#                 top += 1
#                 stack[top]+=cal
#             else:
#                 if stack[top-1]==0 and top!=0:
#                     print(f'#{n+1} error')
#                     break
#                 elif cal=='+':
#                     stack[top-1]+=stack[top]
#                 elif cal=='-':
#                     stack[top-1]-=stack[top]
#                 elif cal=='/':
#                     stack[top-1]=int(stack[top-1]/stack[top])
#                 elif cal=='*':
#                     stack[top-1] *=stack[top]
#                 else:
#                     print(f'#{n+1} {stack[top]}')
#                 stack.pop(top)
#                 top -= 1
#     else:
#         print(f'#{n + 1} error')

# # 미로
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0, 0]
#
# def IsPossible(y, x):
#     if -1 < y < S and -1 < x < S and not visited[y][x] and A[y][x]!=1:
#         return True
#     else:
#         return False
# def Miro(y,x):
#     global result
#     visited[y][x] = True
#     if A[y][x] == 3:
#         result = 1
#         return result
#     for dir in range(4):
#         if IsPossible(y+dy[dir],x+dx[dir]):
#             newY = y+dy[dir]
#             newX = x+dx[dir]
#             Miro(newY, newX)
#
# N = int(input())
# for n in range(N):
#     result = 0
#     S=int(input())
#     visited = [[0] * S for _ in range(S)]
#     A=[list(map(int,input()))for y in range(S)]
#
#     for start in range(S):
#         for start1 in range(S):
#             if A[start][start1]==2:
#                 Miro(start,A[start].index(2))
#                 print(f'#{n+1} {result}')
#                 break

# # 계산기
# for n in range(10):
#     N=input()
#     C=input()
#     calc=[]
#     stack=[]
#     top=-1
#     R=[]
#     for i in C:
#         if i.isdigit():
#             calc.append(i)
#         elif i==')':
#             while stack[top]!='(':
#                 calc.append(stack.pop())
#                 top-=1
#             stack.pop()
#             top-=1
#         else:
#             if i=='+':
#                 if stack[top]=='*':
#                     while stack[top]!='*':
#                         calc.append(stack.pop())
#                         top-=1
#             stack.append(i)
#             top+=1
#     for c in calc:
#         if c == '+':
#             R.append(R.pop()+R.pop())
#         elif c == '*':
#             R.append(R.pop()*R.pop())
#         else:
#             R.append(int(c))
#     print(f'#{n+1} {R[0]}')

