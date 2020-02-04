import sys
sys.stdin = open('bj2887.txt','r')

def MST():
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(b)]=find(a)
    R=0
    k=0
    for i in L:
        if k==N-1:break
        c,a,b=i
        if find(a)!=find(b):R+=c;union(a,b);k+=1
    return R
N=int(input())
A=[]
for i in range(N):A+=[[int(x)for x in input().split()]+[i]]
L=[]
A.sort()
for i in range(N-1):L.append((abs(A[i][0]-A[i+1][0]),A[i][3],A[i+1][3]))
A.sort(key=lambda x:x[1])
for i in range(N-1):L.append((abs(A[i][1]-A[i+1][1]),A[i][3],A[i+1][3]))
A.sort(key=lambda x:x[2])
for i in range(N-1):L.append((abs(A[i][2]-A[i+1][2]),A[i][3],A[i+1][3]))
L.sort()
print(MST())
