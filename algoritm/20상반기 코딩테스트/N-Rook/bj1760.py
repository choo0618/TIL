import sys
sys.stdin = open('bj1760.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if b[i]==-1 or (not V[b[i]] and DFS(b[i])):
            a[x]=i
            b[i]=x
            return 1
    return 0
M,N=map(int,input().split())
RA=[[0]*N for _ in range(M)]
CA=[[0]*N for _ in range(M)]
A=[]
Rn,Cn=1,1
for i in range(M):
    I=[int(x)for x in input().split()]
    Check=0
    for n in range(N):
        if I[n]!=2:
            RA[i][n]=Rn
            Check=1
            if n==N-1:Rn+=1
        else:
            if Check:Rn+=1
            Check=0
    A.append(I)
for j in range(N):
    Check=0
    for i in range(M):
        if A[i][j]!=2:
            CA[i][j]=Cn
            Check=1
            if i==M-1:Cn+=1
        else:
            if Check:Cn+=1
            Check=0
Map=[[]for _ in range(Rn)]
for i in range(M):
    for j in range(N):
        if not A[i][j]:Map[RA[i][j]].append(CA[i][j])
a=[-1]*Rn
b=[-1]*Cn
R=0
for i in range(1,Rn):
    V=[0]*Rn
    if DFS(i):R+=1
print(R)