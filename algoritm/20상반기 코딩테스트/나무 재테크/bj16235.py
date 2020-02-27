import sys
sys.stdin = open('bj16235.txt','r')

dy=[-1,-1,0,1,1,1,0,-1]
dx=[0,1,1,1,0,-1,-1,-1]
def IS(y,x):
    if 0<y<L[0]+1 and 0<x<L[0]+1:return True
    return False
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
T=[[int(x)for x in input().split()]for y in range(L[1])]
M=[[5]*L[0]for _ in range(L[0])]
while L[2]:
    S,t,t1=[],[],[]
    for i in T:
        ty=i[0]-1
        tx=i[1]-1
        Y=i[2]
        if Y<=M[ty][tx]:
            M[ty][tx]-=Y
            i[2]+=1
            t+=[[ty+1,tx+1,Y+1]]
        else:S+=[[ty,tx,Y]];i[2]=0
        if i[2] and not i[2]%5:
            for dir in range(8):
                nY=i[0]+dy[dir]
                nX=i[1]+dx[dir]
                if IS(nY,nX):t1+=[[nY,nX,1]]
    T=t1+t
    for s in S:
        M[s[0]][s[1]]+=s[2]//2
    for k in range(L[0]):
        for l in range(L[0]):
            M[k][l]+=A[k][l]
    L[2]-=1
print(len(T))