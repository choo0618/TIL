# import sys
# sys.stdin = open('5653.txt','r')
#
# for t in range(int(input())):
#     N,M,K=map(int,input().split())
#     A=[[int(x)for x in input().split()]for y in range(N)]
#     Set,Q=set(),[]
#     for i in range(N):
#         for j in range(M):
#             if A[i][j]:Set.add((i,j)),Q.append([2*A[i][j],A[i][j],i,j])
#     while K:
#         Q.sort()
#         # Q.reverse()
#         Len=len(Q)
#         for q in range(Len):
#             if not Q[q][0]:continue
#             Q[q][0]-=1
#             l,s,y,x=tuple(Q[q])
#             if l+1==s:
#                 for d in [(0,1),(1,0),(0,-1),(-1,0)]:
#                     SL=len(Set)
#                     Set.add((y+d[0],x+d[1]))
#                     if SL!=len(Set):
#                         Q.append([2*s,s,y+d[0],x+d[1]])
#         K-=1
#     # print(len(Q))
#     print('#%d %d'%(t+1,sum(1 for q in Q if q[0])))


import sys
sys.stdin = open('5653.txt','r')

for t in range(int(input())):
    N,M,K=map(int,input().split())
    Set,Q=set(),[]
    for i in range(N):
        for j,n in enumerate(map(int,input().split())):
            if n:Set.add((i,j));Q.append((2*n,n,i,j))
    for k in range(K):
        Q.sort()
        q=[]
        while Q:
            l,s,y,x=Q.pop()
            tmp=l-1
            if tmp:q.append((tmp,s,y,x))
            if tmp+1==s:
                for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
                    SL=len(Set)
                    Set.add((Y,X))
                    if SL!=len(Set):q.append((2*s,s,Y,X))
        Q=q
    print('#%d %d'%(t+1,len(Q)))