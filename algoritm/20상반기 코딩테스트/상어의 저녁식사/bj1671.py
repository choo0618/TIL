import sys
sys.stdin = open('bj1671.txt','r')

def DFS(x):
    V[x]=1
    for idx,i in enumerate(A):
        if idx==x or (A[x][0]==i[0]and A[x][1]==i[1] and A[x][2]==i[2] and x<idx):continue
        if (A[x][0]>=i[0]and A[x][1]>=i[1] and A[x][2]>=i[2]) and(s2[idx]==-1 or (not V[s2[idx]] and DFS(s2[idx]))):
            s2[idx]=x
            s1[x]=idx
            return 1
    return 0
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
A.sort()
s1=[-1]*N
s2=[-1]*N
R=N
for i in range(N):
    for t in range(2):
        V=[0]*N
        if DFS(i):R-=1
print(R)