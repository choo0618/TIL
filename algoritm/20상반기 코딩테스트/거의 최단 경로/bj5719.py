import sys
sys.stdin = open('bj5719.txt')

import heapq

Heap=[8,5,2,4,7,1]
heapq.heapify(Heap)
print(Heap)
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)



# from collections import deque
# import heapq
# def Dijkstra(S,D):
#     for i in range(N):L[i]=987654321
#     Que=[]
#     heapq.heappush(Que,(S,0))
#     L[S]=0
#     while Que:
#         now,Dis=heapq.heappop(Que)
#         for nxt,nxtd in Map[now]:
#             nxtd+=Dis
#             if L[nxt]>nxtd and not V[now][nxt]:
#                 L[nxt]=nxtd
#                 heapq.heappush(Que,(nxt,nxtd))
#     return L[D]
# def BFS(S,D):
#     Que=deque()
#     Que.append(D)
#     while Que:
#         now=Que.popleft()
#         if now==S:continue
#         for p,pd in Rev[now]:
#             if L[now]==L[p]+pd:
#                 V[p][now]=1
#                 Que.append((p))
#
# while True:
#     N,M=map(int,input().split())
#     if not N+M:break
#     S,D=map(int,input().split())
#     Map=[[] for _ in range(N)]
#     Rev=[[] for _ in range(N)]
#     for i in range(M):
#         s,e,d=map(int,input().split())
#         Map[s].append((e,d))
#         Rev[e].append((s,d))
#     V=[[0]*N for _ in range(N)]
#     L=[0]*N
#     R=Dijkstra(S,D)
#     BFS(S,D)
#     R=Dijkstra(S,D)
#     if R==987654321:R=-1
#     print(R)
