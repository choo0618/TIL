import sys
sys.stdin = open('2112.txt','r')

# def Check():
#     for j in range(W):
#         c=1
#         for i in range(0,D-K+1):
#             S=sum(A[x][j]for x in range(i,i+K))
#             if not S or S==K:c=0;break
#         if c:return 0
#     return 1
# def DFS(idx,t):
#     global R
#     if t==r:
#         if Check():R=r
#         return
#     for i in range(idx,D):
#         l=A[i][:]
#         for n in range(2):
#             A[i]=[n]*W
#             DFS(i+1,t+1)
#             if R==r:return
#         A[i]=l
# for t in range(int(input())):
#     D,W,K=map(int,input().split())
#     A=[[int(x)for x in input().split()]for y in range(D)]
#     R=K
#     for r in range(K):
#         DFS(0,0)
#         if R==r:break
#     print('#%d %d'%(t+1,R))

# def Check():
#     for j in range(W):
#         c=1
#         for i in range(0,D-K+1):
#             S=sum(M[x][j]for x in range(i,i+K))
#             if not S or S==K:c=0;break
#         if c:return 0
#     return 1
# def DFS(idx,t):
#     global R
#     if t==r:
#         if Check():R=r
#         return
#     for i in range(idx,D):
#         for n in range(2):
#             M[i]=[n]*W
#             DFS(i+1,t+1)
#             if R==r:return
#         M[i]=A[i]
# for t in range(int(input())):
#     D,W,K=map(int,input().split())
#     A=[[int(x)for x in input().split()]for y in range(D)]
#     M,R=A[:],K
#     for r in range(K):
#         DFS(0,0)
#         if R==r:break
#     print('#%d %d'%(t+1,R))


import itertools
def Check():
    for j in range(W):
        c=1
        for i in range(0,D-K+1):
            S=sum(M[x][j]for x in range(i,i+K))
            if not S or S==K:c=0;break
        if c:return 0
    return 1
def DFS(idx):
    global R
    if idx==r:
        if Check():R=r
        return
    for n in range(2):
        M[c[idx]]=[n]*W
        DFS(idx+1)
        if R==r:return
    M[c[idx]]=A[c[idx]]
for t in range(int(input())):
    D,W,K=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(D)]
    M,R=A[:],K
    for r in range(K):
        for c in itertools.combinations(range(D),r):DFS(0)
        if R==r:break
    print('#%d %d'%(t+1,R))