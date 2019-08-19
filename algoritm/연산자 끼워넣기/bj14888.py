import sys
sys.stdin = open('bj14888.txt','r')

def DFS(R,c):
    global Max,Min
    if c==r:
        if R>Max:Max=R
        if R<Min:Min=R
        return
    for f in range(4):
        if C[f]:
            C[f]-=1
            if not f:
                DFS(R+L[c+1],c+1)
            elif f==1:
                DFS(R-L[c+1],c+1)
            elif f==2:
                DFS(R*L[c+1],c+1)
            else:
                if R<0:R=-1*R//L[c+1]*-1
                else:R//=L[c+1]
                DFS(R,c+1)
            C[f]+=1
N=int(input())
L=[int(x)for x in input().split()]
C=[int(x)for x in input().split()]
r=sum(C)
Max=-1000000000
Min=1000000000
DFS(L[0],0)
print(Max)
print(Min)