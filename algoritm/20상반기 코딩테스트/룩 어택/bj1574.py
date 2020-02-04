import sys
sys.stdin = open('bj1574.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if b[i]==-1 or (not V[b[i]] and DFS(b[i])):
            a[x]=i
            b[i]=x
            return 1
    return 0
R,C,N=map(int,input().split())
A=[[1]*C for _ in range(R)]
for i in range(N):
    y,x=map(int,input().split())
    A[y-1][x-1]=0
RA=[[0]*C for _ in range(R)]
CA=[[0]*C for _ in range(R)]
Rn,Cn=1,1
for i in range(R):
    for j in range(C):
        if A[i][j]:RA[i][j]=Rn
    Rn+=1
for i in range(C):
    for j in range(R):
        if A[j][i]:CA[j][i]=Cn
    Cn+=1
Map=[[]for _ in range(Rn)]
a=[-1]*Rn
b=[-1]*Cn
r=0
for i in range(R):
    for j in range(C):
        if RA[i][j]:Map[RA[i][j]].append(CA[i][j])
for i in range(1,Rn):
    V=[0]*Rn
    if DFS(i):r+=1
print(r)