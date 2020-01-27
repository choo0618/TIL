import sys
sys.stdin=open('input.txt','r')

# 1
# def DFS(cnt,List):
#     if cnt==M:
#         for p in List:
#             print(p,end=' ')
#         print()
#         return
#     for i in range(N):
#         if not Map[i]:
#             Map[i]=1
#             nL=List+[i+1]
#             DFS(cnt+1,nL)
#             Map[i]=0
# N,M=map(int,input().split())
# Map=[0]*N
# DFS(0,[])

# 2
# def DFS(idx,cnt,List):
#     if cnt==M:
#         for p in List:
#             print(p,end=' ')
#         print()
#         return
#     for i in range(idx,N):
#         if not Map[i]:
#             Map[i]=1
#             nL=List+[i+1]
#             DFS(i,cnt+1,nL)
#             Map[i]=0
#
# N,M=map(int,input().split())
# Map=[0]*N
# DFS(0,0,[])

# 3
# def DFS(cnt,List):
#     if cnt==M:
#         print(' '.join(map(str, List)))
#         return
#     for i in range(N):
#         List.append(i+1)
#         DFS(cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# DFS(0,[])

# 4
# def DFS(idx,cnt,List):
#     if cnt==M:
#         print(' '.join(map(str, List)))
#         return
#     for i in range(idx,N):
#         List.append(i+1)
#         DFS(i,cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# DFS(0,0,[])