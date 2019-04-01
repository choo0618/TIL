import sys
sys.stdin=open('input.txt','r')

연산
# def YEONSAN(y,x,c):
#     global R
#     if x==y:
#         if c<R:R=c;r.append(y);return
#     if c>R:return
#     if y in r:return
#     if not y%2 and y>x:YEONSAN(y//2,x,c+1)
#     YEONSAN(y+1,x,c+1)
#     YEONSAN(y+10,x,c+1)
#     YEONSAN(y-1,x,c+1)
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     r=[]
#     R=987654321
#     YEONSAN(L[1],L[0],0)
#     print('#%d %d'%((n+1),R))

# # 그룹나누기(디스조인트)
# def Find_Set(x):
#     if x == P[x]:return x
#     else:return Find_Set(P[x])
# def Union(x, y):
#     P[Find_Set(y)]=Find_Set(x)
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     L1=[int(x)for x in input().split()]
#     P=[0]+[0]*(L[0])
#     for j in range(L[0]+1):
#         P[j]=j
#     for i in range(0,len(L1),2):
#         Union(L1[i],L1[i+1])
#     cnt=[]
#     for c in range(len(P)):
#         if Find_Set(c) not in cnt:cnt.append(Find_Set(c))
#     print('#%d %d'%((n+1),len(cnt)-1))

# # 그룹나누기(플로이드 워셜)
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     L1=[int(x)for x in input().split()]
#     M=[[0]*(L[0]+1)for _ in range(L[0]+1)]
#     for i in range(0,2*L[1],2):
#         M[L1[i]][L1[i+1]]=1
#         M[L1[i+1]][L1[i]]=1
#     for via in range(1,L[0]+1):
#         for start in range(1,L[0]+1):
#             for end in range(1,L[0]+1):
#                 M[start][end]=M[start][end] or (M[start][via] and M[via][end])
#     cnt=0
#     C=[]
#     for c in range(1,L[0]+1):
#         if not sum(M[c]):cnt+=1
#         else:
#             if M[c] not in C:C.append(M[c])
#     print('#%d %d'%((n+1),cnt+len(C)))

# # 최소 신장트리
# def Find(x):
#     if x == P[x]:return x
#     else:return Find(P[x])
# def Union(x, y):
#     P[Find(y)]=Find(x)
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(L[1])]
#     A.sort(key=lambda x: x[2])
#     P=[]
#     for j in range(L[0]+1):
#         P.append(j)
#     R=0
#     for i in range(len(A)):
#         if Find(A[i][0])!=Find(A[i][1]):
#             R+=A[i][2]
#             Union(A[i][0],A[i][1])
#     print('#%d %d'%((n+1),R))

# # 최소비용
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# def IsSafe(y,x):
#     if -1<y<N and -1<x<N:return True
#     else: return False
# def BFS(y,x):
#     Q.append([y,x])
#     while Q:
#         tmp=Q.pop(0)
#         hereY=tmp[0]
#         hereX=tmp[1]
#         for dir in range(4):
#             newY=hereY+dy[dir]
#             newX=hereX+dx[dir]
#             if IsSafe(newY,newX):
#                 if A[hereY][hereX]<A[newY][newX]:
#                     if (newX or newY) and M[hereY][hereX]+1+(A[newY][newX]-A[hereY][hereX])<M[newY][newX]:
#                         M[newY][newX]=M[hereY][hereX]+1+(A[newY][newX]-A[hereY][hereX])
#                         Q.append([newY,newX])
#                 else:
#                     if (newX or newY) and M[hereY][hereX]+1<M[newY][newX]:
#                         M[newY][newX] = M[hereY][hereX] + 1
#                         Q.append([newY, newX])
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     M=[[987654321]*(N)for _ in range(N)]
#     M[0][0]=0
#     Q=[]
#     BFS(0,0)
#     print('#%d %d'%((n+1),(M[N-1][N-1])))

# # 최소 이동 거리
# T=int(input())
# for n in range(T):
#     L=[int(x)for x in input().split()]
#     A=[[int(x)for x in input().split()]for y in range(L[1])]
#     M=[[987654321]*(L[0]+1) for _ in range(L[0]+1)]
#     for _ in range(L[0]+1):
#         M[_][_]=0
#     for x in range(len(A)):
#         M[A[x][0]][A[x][1]]=A[x][2]
#     U=[0]
#     T=[]
#     for t in range(L[0]+1):
#         T.append(t)
#     D=M[0]
#     while len(U)!=L[0]:
#         w=D.index(min(D[T[1]:T[-1]]))
#         U.append(w)
#         T.pop(1)
#         for i in T:
#             D[i]=min(D[i],D[w]+M[w][i])
#     print(D)
#     print('#%d %d'%((n+1),D[L[0]]))

# # 전기버스 2
def DFS(which,battery,c):
    global R
    if which>=L[0]:
        if c<R:R=c;return
    if c>=R:
        return
    for i in range(battery,-1,-1):
        if which+i<=L[0]:
            DFS(which+i,L[which+i],c+1)
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    L.append(0)
    R=987654321
    DFS(1,L[1],0)
    print('#%d %d'%((n+1),(R-1)))

# # 보급로(BFS)
# dy=[0,1,0,-1]
# dx=[1,0,-1,0]
# def IsSafe(y,x):
#     if -1<y<N and -1<x<N:return True
#     else: return False
# def BFS(y,x):
#     Q.append([y,x])
#     while Q:
#         tmp=Q.pop(0)
#         hereY=tmp[0]
#         hereX=tmp[1]
#         for dir in range(4):
#             newY=hereY+dy[dir]
#             newX=hereX+dx[dir]
#             if IsSafe(newY,newX):
#                 if (newX or newY) and M[hereY][hereX]+A[newY][newX]<M[newY][newX]:
#                     M[newY][newX]=M[hereY][hereX]+A[newY][newX]
#                     Q.append([newY,newX])
# T=int(input())
# for n in range(T):
#     N=int(input())
#     A=[list(map(int,input()))for y in range(N)]
#     M=[[987654321]*(N)for _ in range(N)]
#     M[0][0]=0
#     Q=[]
#     BFS(0,0)
#     print('#%d %d'%((n+1),(M[N-1][N-1])))