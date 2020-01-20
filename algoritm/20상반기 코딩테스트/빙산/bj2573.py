import sys
sys.stdin = open('bj2573.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M

def Check():
    global check
    Map=[[0]*M for _ in range(N)]
    Sum=0
    tmp=0
    for y in range(1,N-1):
        Sum+=sum(A[y])
        for x in range(M):
            if A[y][x] and not Map[y][x]:
                if tmp==1:return False
                tmp+=1
                Map[y][x]=tmp
                Que = [[y,x]]
                while Que:
                    Q=[]
                    for q in Que:
                        for d in range(4):
                            nY=q[0]+dy[d]
                            nX=q[1]+dx[d]
                            if IS(nY,nX) and A[nY][nX] and not Map[nY][nX]:
                                Map[nY][nX]=tmp
                                Q.append([nY,nX])
                    Que=Q
    if not Sum:check=1;return False
    return True
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Y,I,check=0,[],0
for i in range(1,N-1):
    for j in range(M):
        if A[i][j]:I.append((i,j,A[i][j]))
while Check():
    Mi=[]
    Map=[[0]*M for _ in range(N)]
    i=[]
    for m in I:
        c=0
        for d in range(4):
            if IS(m[0]+dy[d],m[1]+dx[d]) and not A[m[0]+dy[d]][m[1]+dx[d]]:c+=1
        r=m[2]-c
        if r<=0:r=0
        else:i.append((m[0],m[1],r))
        Map[m[0]][m[1]]=r
    I=i
    A=Map
    Y+=1
if check:Y=0
print(Y)