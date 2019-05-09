import sys
sys.stdin = open('bj14503.txt','r')

def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]:return True
    return False
def C(y,x):
    if A[y+1][x] and A[y-1][x] and A[y][x+1] and A[y][x-1]:return False
    return True
dy=[-1,0,1,0]
dx=[0,1,0,-1]
L=[int(x)for x in input().split()]
R=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
RS=0
Q=[]
Q.append([R[0],R[1],R[2]])
while Q:
    tmp=Q.pop(0)
    hY=tmp[0]
    hX=tmp[1]
    hD=tmp[2]
    if A[hY][hX]==0:A[hY][hX]=3;RS+=1
    nD=(tmp[2]+3)%4
    nY=tmp[0]+dy[nD]
    nX=tmp[1]+dx[nD]
    if IS(nY,nX):
        if C(hY,hX):
            if not A[nY][nX]:
                Q.append([nY,nX,nD])
            elif A[nY][nX]==3 or A[nY][nX]:
                Q.append([hY,hX,nD])
        else:
            hY+=dy[hD]*(-1)
            hX+=dx[hD]*(-1)
            if A[hY][hX]==1:break
            Q.append([hY,hX,hD])
print(RS)