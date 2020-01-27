import sys
sys.stdin=open('input.txt','r')

# # 1
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

# # 2
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

# # 3
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

# # 4
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

# # 5
# def DFS(idx,cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     for i in range(N):
#         if Map[i]:continue
#         Map[i]=1
#         List.append(L[i])
#         DFS(i+1,cnt+1,List)
#         Map[i]=0
#         List.pop()
#
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# Map=[0]*N
# DFS(0,0,[])

# # 6
# def DFS(idx,cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#     for i in range(idx,N):
#         List.append(L[i])
#         DFS(i+1,cnt+1,List)
#         List.pop()
#
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# DFS(0,0,[])

# # 7
# def DFS(cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     for i in range(N):
#         List.append(L[i])
#         DFS(cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# DFS(0,[])

# # 8
# def DFS(idx,cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     for i in range(idx,N):
#         List.append(L[i])
#         DFS(i,cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# DFS(0,0,[])

# # 9
# def DFS(cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     Map=[0]*(max(L)+1)
#     for i in range(N):
#         if Map[L[i]]or Map1[i]:continue
#         List.append(L[i])
#         Map[L[i]]=1
#         Map1[i]=1
#         DFS(cnt+1,List)
#         List.pop()
#         Map1[i]=0
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# Map1=[0]*N
# DFS(0,[])

# # 10
# def DFS(idx,cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     Map=[0]*(max(L)+1)
#     for i in range(idx,N):
#         if Map[L[i]]:continue
#         List.append(L[i])
#         Map[L[i]]=1
#         DFS(i+1,cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# DFS(0,0,[])

# # 11
# def DFS(cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     Map=[0]*(max(L)+1)
#     for i in range(N):
#         if Map[L[i]]:continue
#         List.append(L[i])
#         Map[L[i]]=1
#         DFS(cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# DFS(0,[])

# # 12
# def DFS(idx,cnt,List):
#     if cnt==M:
#         print(' '.join(map(str,List)))
#         return
#     Map=[0]*(max(L)+1)
#     for i in range(idx,N):
#         if Map[L[i]]:continue
#         List.append(L[i])
#         Map[L[i]]=1
#         DFS(i,cnt+1,List)
#         List.pop()
# N,M=map(int,input().split())
# L=[int(x)for x in input().split()]
# L.sort()
# DFS(0,0,[])


