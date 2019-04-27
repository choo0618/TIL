import sys
sys.stdin = open('bj17144.txt','r')

dy=[-1,0,1,0]
dx=[0,1,0,-1]
def IS(y,x):
    if -1<y<L[0] and -1<x<L[1]:return True
    return False
def Dust(y,x):
    tmp=A[y][x]//5
    for dir in range(4):
        nY=y+dy[dir]
        nX=x+dx[dir]
        if IS(nY,nX) and A[nY][nX]!=-1:
            M[nY][nX]+=tmp
            A[y][x]-=tmp
    M[y][x]+=A[y][x]
def AIR(y,x,a):
    if M[y][x]==-1:return
    for dir in range(4):
        nY=y+dy[dir]
        nX=x+dx[dir]
        if IS(nY,nX) and not V[nY][nX] and M[nY][nX]!=-1:
            tmp=M[nY][nX]
            M[nY][nX]=a
            V[y][x]=1
            AIR(nY,nX,tmp)
            return
# def AIR(y,x,a):
#     Q=[]
#     Q.append([y,x,a])
#     Q.append([y+1,x,M[y+1][x]])
#     while Q:
#         tmp=Q.pop(0)
#         hY=tmp[0]
#         hX=tmp[1]
#         d=tmp[2]
#         V[hY][hX]=1
#         for dir in range(4):
#             nY=hY+dy[dir]
#             nX=hX+dx[dir]
#             if IS(nY,nX) and not V[nY][nX] and M[nY][nX]!=-1:
#                 Q.append((nY,nX,M[nY][nX]))
#                 M[nY][nX]=d
#                 break
L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]
for a in range(L[0]):
    if A[a][0]==-1:air=a;break
while L[2]:
    M=[[0]*L[1]for _ in range(L[0])]
    M[air][0]=M[air+1][0]=-1
    for i in range(L[0]):
        for j in range(L[1]):
            if A[i][j]>0:
                Dust(i,j)
    V=[[0]*L[1]for _ in range(L[0])]
    for vy in range(L[0]):
        if vy==0 or vy==L[0]-1 or vy==air or vy==air+1:continue
        for vx in range(L[1]):
            if vx==0 or vx==L[1]-1:continue
            V[vy][vx]=1
    AIR(air,1,M[air][1])
    M[air][1]=M[air+1][1]=0
    A=M
    L[2]-=1
R=2
for ry in range(L[0]):
    for rx in range(L[1]):
        R+=A[ry][rx]
print(R)