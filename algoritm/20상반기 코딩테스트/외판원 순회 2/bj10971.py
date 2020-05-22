import sys
sys.stdin = open('bj10971.txt','r')

# def DFS(s,n,r,c):
#     global R
#     if r>=R:return
#     if c==N-1:
#         if A[n][s]:R=min(R,r+A[n][s])
#         return
#     for i,t in enumerate(A[n]):
#         if V[i] or s==i or t==0:continue
#         V[i]=1
#         DFS(s,i,r+t,c+1)
#         V[i]=0
# N=int(input())
# A=[[int(x)for x in input().split()]for y in range(N)]
# V=[0]*N
# R=10**9
# for i in range(N):DFS(i,i,0,0)
# print(R)

def DFS(s,n,r,c):
    global R
    if r>=R:return
    if c==N-1:
        if A[n][s]:R=min(R,r+A[n][s])
        return
    for i,t in enumerate(A[n]):
        if V[i] or s==i or t==0:continue
        V[i]=1
        DFS(s,i,r+t,c+1)
        V[i]=0
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[0]*N
R=10**9
for i in range(N):DFS(i,i,0,0)
print(R)

