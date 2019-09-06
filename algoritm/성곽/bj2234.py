import sys
sys.stdin = open('bj2234.txt','r')

from collections import deque
dx=[0,1,0,-1]
dy=[1,0,-1,0]
def IS(y,x):
    if -1<y<L[1] and -1<x<L[0]:return True
    return False
def Bi(x):
    B=[]
    while x:
        b=x%2
        B.insert(0,b)
        x//=2
    z=[0]*(4-len(B))
    B=z+B
    return B
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[1])]
M=[[0]*L[0]for _ in range(L[1])]
R,n,r=0,1,[0,0]
for i in range(L[1]):
    for j in range(L[0]):
        if not M[i][j]:
            r[n]+=1
            r.append(0)
            M[i][j]=n
            Q=[[i,j]]
            # Q.append([y,x])
            while Q:
                hY,hX=Q.pop(0)
                B=Bi(A[hY][hX])
                for dir in range(4):
                    if not B[dir]:
                        nY=hY+dy[dir]
                        nX=hX+dx[dir]
                        if IS(nY,nX) and not M[nY][nX]:
                            M[nY][nX]=n
                            r[n]+=1
                            Q.append([nY,nX])
        else:continue
        n+=1
for t in range(2):
    M=list(map(list,zip(*M[::-1])))
    for i in range(len(M)):
        for j in range(0,len(M[0])-1):
            if M[i][j]!=M[i][j+1]:
                s=r[M[i][j]]+r[M[i][j+1]]
                if s>R:R=s
print(len(r)-2)
print(max(r))
print(R)
