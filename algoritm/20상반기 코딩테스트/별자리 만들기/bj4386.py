import sys
sys.stdin = open('bj4386.txt','r')

def MST():
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[find(a)]=find(b)
    R=0
    for l in L:
        d,a,b=l
        if find(a)!=find(b):R+=d;union(a,b)
    return R

N=int(input())
A=[[float(x)for x in input().split()]for y in range(N)]
L=[]
for i in range(N):
    for j in range(i+1,N):
        dis=(abs(A[i][0]-A[j][0])**2+abs(A[i][1]-A[j][1])**2)**0.5
        L.append((dis,i,j))
L.sort()
print('%.2f'%MST())

