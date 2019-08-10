import sys
sys.stdin = open('5644.txt','r')

dx=[0,0,1,0,-1]
dy=[0,-1,0,1,0]
def IS(y,x):
    if -1<y<10 and -1<x<10:return True
    return False
T=int(input())
for t in range(T):
    L=[int(x)for x in input().split()]
    a=[[0,0]]+[int(x)for x in input().split()]
    b=[[9,9]]+[int(x)for x in input().split()]
    B=[[int(x)for x in input().split()]for y in range(L[1])]
    M=[[[0]*(L[1]+1)for x in range(10)]for y in range(10)]
    i=0
    for C in B:
        Q=[[C[1]-1,C[0]-1,C[2]]]
        while Q:
            tmp=Q.pop(0)
            hY=tmp[0]
            hX=tmp[1]
            M[hY][hX][i]=C[3]
            for dir in range(1,5,1):
                nY=hY+dy[dir]
                nX=hX+dx[dir]
                d=tmp[2]-1
                if IS(nY,nX) and not M[nY][nX][i] and tmp[2]:
                    Q.append([nY,nX,d])
                    M[nY][nX][i]=C[3]
        i+=1
    for n in range(1,L[0]+1,1):
        ad,bd=a[n],b[n]
        a[n]=[a[n-1][0]+dy[ad],a[n-1][1]+dx[ad]]
        b[n]=[b[n-1][0]+dy[bd],b[n-1][1]+dx[bd]]
    for c in range(L[0]+1):
        a[c]=M[a[c][0]][a[c][1]]
        b[c]=M[b[c][0]][b[c][1]]
    R=0
    for h in range(L[0]+1):
        r=0
        for ac in range(L[1]+1):
            for bc in range(L[1]+1):
                if ac==bc:m=(a[h][ac]+b[h][bc])//2
                else:m=a[h][ac]+b[h][bc]
                if m>r:r=m
        R+=r
    print('#%d %d'%(t+1,R))