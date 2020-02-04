import sys
sys.stdin = open('bj2414.txt','r')

def DFS(x):
    V[x]=1
    for i in Map[x]:
        if B[i]==-1 or (not V[B[i]] and DFS(B[i])):
            A[x]=i
            B[i]=x
            return 1
    return 0
N,M=map(int,input().split())
Arr=[]
RA=[[0]*M for _ in range(N)]
CA=[[0]*M for _ in range(N)]
Rn,Cn=1,1
for i in range(N):
    I=input()
    Check=0
    for s in range(M):
        if I[s]=='*':
            RA[i][s]=Rn
            Check=1
            if s==M-1:Rn+=1
        else:
            if Check:Rn+=1
            Check=0
    Arr.append(I)
for j in range(M):
    Check=0
    for i in range(N):
        if Arr[i][j]=='*':
            CA[i][j]=Cn
            Check=1
            if i==N-1:Cn+=1
        else:
            if Check:Cn+=1
            Check=0
Map=[[]for _ in range(Cn)]
for i in range(N):
    for j in range(M):
        if CA[i][j]:Map[CA[i][j]].append(RA[i][j])
A=[-1]*Cn
B=[-1]*Rn
R=0
for i in range(1,Cn):
    V=[0]*Cn
    if DFS(i):R+=1
print(R)