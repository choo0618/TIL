import sys
sys.stdin = open('bj1516.txt','r')

# from collections import deque
# N=int(input())
# A=[[]for _ in range(N)]
# T=[0]*N
# R=[0]*N
# D=[0]*N
# Q=deque()
# for _ in range(N):
#     T[_],*l=map(int,input().split())
#     for n in l:
#         if n==-1:break
#         A[n-1].append(_)
#         D[_]+=1
# for d in range(N):
#     if not D[d]:Q.append(d);R[d]=T[d]
# while Q:
#     now=Q.popleft()
#     for next in A[now]:
#         D[next]-=1
#         R[next]=max(R[next],R[now]+T[next])
#         if not D[next]:
#             Q.append(next)
# for p in R:print(p)


def DFS(x):
    D[x]-=1
    T[x]+=R[x]
    for i in A[x]:
        D[i]-=1
        R[i]=max(R[i],T[x])
        if not D[i]:DFS(i)
N=int(input())
A=[[]for _ in range(N)]
T=[0]*N
R=[0]*N
D=[0]*N
for _ in range(N):
    T[_],*l=map(int,input().split())
    for n in l[:-1]:
        A[n-1].append(_)
        D[_]+=1
for n in range(N):
    if not D[n]:DFS(n)
print('\n'.join(map(str,T)))