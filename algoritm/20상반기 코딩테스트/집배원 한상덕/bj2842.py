import sys
sys.stdin = open('bj2842.txt','r')

dx=[1,1,1,0,-1,-1,-1,0]
dy=[-1,0,1,1,1,0,-1,-1]
def IS(y,x):
    return -1<y<N and -1<x<N
N=int(input())
A=[list(map(str,input()))for y in range(N)]
H,L=[],[]
for h in range(N):
    I=[int(x)for x in input().split()]
    L+=I
    H.append(I)
L.sort()
Min,Max,P,K,R=0,0,0,0,987654321
for i in range(N):
    for j in range(N):
        if A[i][j]=='P':P=(i,j)
        elif A[i][j]=='K':K+=1
for i in range(N*N):
    if L[i]==H[P[0]][P[1]]:Max=i;tmp=i;break
while Min<=Max and Min!=tmp+1:
    Que,h=[P],0
    Map=[[0]*N for _ in range(N)]
    while Que:
        Q=[]
        for q in Que:
            for d in range(8):
                Y,X=q[0]+dy[d],q[1]+dx[d]
                if IS(Y,X) and L[Min]<=H[Y][X]<=L[Max] and not Map[Y][X]:
                    if A[Y][X]=='K':h+=1
                    Map[Y][X]=1
                    Q.append((Y,X))
        Que=Q
    if h==K:
        R=min(R,L[Max]-L[Min])
        Min+=1
    elif Max+1<N*N:Max+=1
    else:break
print(R)