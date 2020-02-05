import sys
sys.stdin = open('bj1774.txt','r')

def MST():
    P=list(range(N+1))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    for m in Path:union(m[0],m[1])
    R=0
    for l in L:
        c,a,b=l
        if find(a)!=find(b):R+=c;union(a,b)
    return R
N,M=map(int,input().split())
A=[[float(x)for x in input().split()]for y in range(N)]
Path=[tuple(int(x)for x in input().split())for y in range(M)]
L=[]
for i in range(N):
    for j in range(i+1,N):
        dis=(abs(A[i][0]-A[j][0])**2+abs(A[i][1]-A[j][1])**2)**0.5
        L.append((dis,i+1,j+1))
L.sort()
print('%.2f'%MST())