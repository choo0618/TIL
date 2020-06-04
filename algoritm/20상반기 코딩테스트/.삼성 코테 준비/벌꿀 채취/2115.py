import sys
sys.stdin = open('2115.txt','r')

def DFS(x,Len,r,rr):
    global n
    n=max(n,rr)
    for i in range(x,Len):
        if r+l[i]<=C:DFS(i+1,Len,r+l[i],rr+l[i]**2)
def Sol(y,x,r):
    global R
    while y<N:
        while x<N-M+1:
            R=max(R,r+A[y][x])
            x+=1
        y+=1
        x=0
for t in range(int(input())):
    N,M,C=map(int,input().split())
    A=[]
    for i in range(N):
        a,l=[0]*(N-M+1),[int(x)for x in input().split()]
        for j in range(N-M+1):
            n=0
            DFS(j,j+M,0,0)
            a[j]=n
        A.append(a)
    R=0
    for i in range(N):
        for j in range(N-M+1):Sol(i,j+M,A[i][j])
    print('#%d %d'%(t+1,R))
