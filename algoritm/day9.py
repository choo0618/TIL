import sys
sys.stdin = open("input.txt", "r")

# # 토너먼트 카드게임 - runtime
# def VS(a,b):
#     if a-b==1 or a-b==-2 or a==b:
#         return a
#     else:
#         return b
# def T(start,end):
#     if end==start:
#         return start
#     c=(start+end)//2
#     return VS(T(start, c), T(c+1, end))
# TC=int(input())
# for num in range(TC):
#     N=int(input())
#     L=[int(x) for x in input().split()]
#     # stack=[]
#     # for i in range(N):
#     #     stack.append([i+1,L[i]])
#     # while stack:
#     #     T((N-1)//2+1,N)
#     #     T(0,(N-1)//2+1)
#     #     if len(stack) == 1:
#     #         break
#     #     N=N//2+1
#     print(f'#{num+1} {T(1,N)}')


# # Magnetic
# for n in range(10):
#     N=int(input())
#     A=[[int(x) for x in input().split()]for y in range(N)]
#     cnt=0
#     for y in range(N):
#         M=0
#         for x in range(N):
#             if A[x][y]==1:
#                 M=1
#             if A[x][y]==2 and M:
#                 cnt+=1
#                 M=0
#     print(f'#{n+1} {cnt}')
#
# # Queue
# Queue=[0]*10
# front = -1
# rear = -1
#
# rear+=1;Queue[rear]=1
# rear+=1;Queue[rear]=2
# rear+=1;Queue[rear]=3
#
# while front!=rear:
#     front+=1
#     print(Queue[front])
# print(Queue)


# # 원형큐
# Queue=[0]*1000
# front=-1
# rear=-1
# n = 41
# for i in range(n):
#     rear+=1;Queue[rear]=i+1
# while Queue:
#     if front>=41:
#         front-=41
#     while front<=rear:
#         Queue[front+3]=0
#         front+=3
# print(front)
# print(Queue)

# # 연습문제 3 BFS
# def BFS(here):
#     global front, rear
#     rear+=1
#     Queue[rear]=here
#     visited[here] = True
#     parents[here]+=1
#     distance[here]+=1
#
#     while front!=rear:
#         front+=1
#         here=Queue[front]
#         print(here)
#         for next in range(8):
#             if MyMap[here][next] and not visited[next]:
#                 visited[next]=True
#                 distance[next]=distance[here]+1
#                 parents[next] = here
#                 rear+=1
#                 Queue[rear]=next
#
# N=7
# L=[int(x) for x in input().split()]
# Queue=[0]*100
# front=-1
# rear=-1
# visited=[0]*(N+1)
# parents=[-1]*(N+1)
# distance=[-1]*(N+1)
# MyMap = [[0]*8 for i in range((N+1))]
# howmany = int(len(L)/2)
# for i in range(howmany):
#     Start=L[i*2]
#     Stop=L[i*2+1]
#     MyMap[Start][Stop]=1
#     MyMap[Stop][Start]=1
# BFS(1)
# print(visited,parents,distance)

# # 회전
# TC=int(input())
# for n in range(TC):
#     N=[int(x) for x in input().split()]
#     L=[int(x) for x in input().split()]
#     for i in range(N[1]):
#         L.append(L.pop(0))
#     print(f'#{n+1} {L[0]}')

# # 미로의 거리
# dy = [0, 0, -1, 1]
# dx = [-1, 1, 0, 0]
# def IsPossible(y, x):
#     if -1 < y < N and -1 < x < N and not visited[y][x] and A[y][x]!=1:
#         return True
#     else:
#         return False
#
# def BFS(y,x):
#     global front, rear
#     visited[y][x] = True
#     rear+=1
#     while A[y][x]!=3 and not visited[y][x]:
#         if IsPossible(new_y,new_x):
#             Que.append([new_y,new_x])
#
#
# N=int(input())
# A=[[int(x) for x in input().split()]for y in range(N)]
# Que=[]
# front=0
# rear=0
# visited=[[0]*N]*N
# for start in range(N):
#     for start1 in range(N):
#         if A[start][start1] == 2:
#             BFS(start, A[start].index(2))
#             print(f'#{n+1} {result}')
#             break



# # 피자 굽기
# TC=int(input())
# for n in range(TC):
#     L=[int(x) for x in input().split()]
#     P=[int(x) for x in input().split()]
#     Que=[]
#     front=0
#     index=[]
#     for i in range(len(P)):
#         index.append([i+1,P[i]])
#     for i in range(L[0]):
#         Que.append(index.pop(0))
#     while sum(Que[x][1] for x in range(L[0]))!=1:
#         Que[0][1]=Que[0][1]//2
#         if not Que[front][1] and index:
#             Que[front]=index.pop(0)
#         Que.append(Que.pop(0))
#
#     while not Que[front][1]:
#         front+=1
#     print(f'#{n+1} {Que[front][0]}')


# # 노드의 거리
# def BFS(here):
#     global front, rear
#     rear+=1
#     Queue[rear]=here
#     visited[here] = True
#     distance[here]+=1
#
#     while front!=rear:
#         front+=1
#         here=Queue[front]
#         for next in range(L[0]+1):
#             if MyMap[here][next] and not visited[next]:
#                 visited[next]=True
#                 distance[next]=distance[here]+1
#                 rear+=1
#                 Queue[rear]=next
# TC=int(input())
# for n in range(TC):
#     L=[int(x) for x in input().split()]
#     A=[[int(x) for x in input().split()]for y in range(L[1])]
#     B=[int(x) for x in input().split()]
#     Queue=[0]*100
#     front=-1
#     rear=-1
#     visited=[0]*(L[0]+1)
#     distance=[-1]*(L[0]+1)
#     MyMap = [[0]*(L[0]+1) for i in range((L[0]+1))]
#
#     for i in range(len(A)):
#         MyMap[A[i][0]][A[i][1]]=1
#         MyMap[A[i][1]][A[i][0]]=1
#     BFS(B[0])
#     if distance[B[1]]<0:
#         distance[B[1]]=0
#     print(f'#{n+1} {distance[B[1]]}')


