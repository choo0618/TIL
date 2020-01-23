import sys
sys.stdin=open('bj1726.txt','r')

dir={1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}
lotate={1:[3,4],2:[4,3],3:[2,1],4:[1,2]}
def IS(y,x):
    return -1<y<M and -1<x<N

M,N=map(int,input().split())
Arr=[[int(x)for x in input().split()]for y in range(M)]
Map=[[[0,0,0,0,0]for x in range(N)] for y in range(M)]
sY,sX,sD=map(int,input().split())
eY,eX,eD=map(int,input().split())
Que=[(sY-1,sX-1,sD,0)]
R=0
while Que and not R:
    Q=[]
    for q in Que:
        if (q[0],q[1],q[2])==(eY-1,eX-1,eD):R=q[3];break
        for k in range(1,4):
            nY=q[0]+k*dir[q[2]][0]
            nX=q[1]+k*dir[q[2]][1]
            if IS(nY,nX) and not Map[nY][nX][q[2]]:
                if Arr[nY][nX]==1:break
                Map[nY][nX][q[2]]=1
                Q.append((nY,nX,q[2],q[3]+1))
        for d in range(2):
            if not Map[q[0]][q[1]][lotate[q[2]][d]]:
                Map[q[0]][q[1]][lotate[q[2]][d]]=1
                Q.append((q[0],q[1],lotate[q[2]][d],q[3]+1))
    Que=Q
print(R)


