import sys
sys.stdin = open('bj16235.txt','r')

dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,1,1,1,0,-1,-1,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[0]:return True
    return False
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
T=[[int(x)for x in input().split()]for y in range(L[1])]
G=[[5]*L[0]for _ in range(L[0])]
M=[[[]for x in range(L[0])]for y in range(L[0])]
R=0
for t in T:
    M[t[0]-1][t[1]-1]+=[t[2]]
while L[2]:
    Q=[]
    for i in range(L[0]):
        for j in range(L[0]):
            g=0
            l=M[i][j]
            if l:
                for k in range(len(l)):
                    if l[k]<=G[i][j]:
                        G[i][j]-=l[k]
                        l[k]+=1
                        if not l[k]%5:Q.append([i,j])
                    else:
                        g+=l[k]//2;l[k].pop()
            G[i][j]+=g+A[i][j]
            l.sort()
            while l and not l[0]:
                l.pop(0)
    for q in Q:
        for dir in range(8):
            nY=q[0]+dy[dir]
            nX=q[1]+dx[dir]
            if IS(nY,nX):M[nY][nX].insert(0,1)
    L[2]-=1
for y in range(L[0]):
    for x in range(L[0]):
        R+=len(M[y][x])
print(R)