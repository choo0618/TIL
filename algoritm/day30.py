import sys
sys.stdin=open('input.txt','r')

# # 리모컨
# def check(x):
#     for c in x:
#         if c in L:
#             return False
#     return True
# N=int(input())
# N1=int(input())
# if N1 and N1!=10:
#     L=[x for x in input().split()]
#     tmp=N
#     tmp1=N
#     cnt=0
#     while tmp>=0 or tmp1:
#         if check(str(tmp)):
#             print(min(cnt+len(str(tmp)),abs(N-100)))
#             break
#         if check(str(tmp1)):
#             print(min(cnt+len(str(tmp1)),abs(N-100)))
#             break
#         tmp-=1
#         if tmp<0:tmp=0
#         tmp1+=1
#         cnt+=1
# elif N1==10:
#     L=[x for x in input().split()]
#     print(abs(N-100))
# else:
#     print(min(abs(N-100),len(str(N))))

# # 탈주범 검거
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# Pipe=[[False,False,False,False],[True,True,True,True],[False,True,False,True],[True,False,True,False],[True,False,False,True],[True,True,False,False],[False,True,True,False],[False,False,True,True]]
# def IsSafe(y,x):
#     if -1<y<L[0] and -1<x<L[1] and not V[y][x]:return True
#     else: return False
# def BFS(y,x,c):
#     Q.append([y,x])
#     V[y][x]=c
#     while Q:
#         tmp=Q.pop(0)
#         hereY=tmp[0]
#         hereX=tmp[1]
#         here=A[hereY][hereX]
#         if not V[hereY][hereX]: break
#         for dir in range(4):
#             newY=hereY+dy[dir]
#             newX=hereX+dx[dir]
#             if IsSafe(newY,newX) and Pipe[here][dir] and Pipe[A[newY][newX]][dir-2]:
#                 Q.append([newY,newX])
#                 V[newY][newX]=V[hereY][hereX]-1
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(L[0])]
#     V=[[0]*L[1]for _ in range(L[0])]
#     Q=[]
#     cnt=0
#     BFS(L[2],L[3],L[4])
#     for y in range(L[0]):
#         for x in range(L[1]):
#             if V[y][x]:cnt+=1
#     print('#%d %d'%((n+1),cnt))

