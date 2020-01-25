import sys
sys.stdin = open('bj6087.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<H and -1<x<W
W,H=map(int,input().split())
Arr=[list(map(str,input())) for y in range(H)]
Que=[]
Map=[[-1]*W for _ in range(H)]
R=987654321
for i in range(H):
    for j in range(W):
        if Arr[i][j]=='C':
            Arr[i][j]='*'
            for d in range(4):Que.append((i,j,d,0))
            break
    if Que:break
while Que:
    Q=[]
    for q in Que:
        if Arr[q[0]][q[1]]=='C':
            r=Map[q[0]][q[1]]
            if r<R:R=r
        for d in range(4):
            Y,X,nD,cnt=q[0]+dy[d],q[1]+dx[d],q[2],q[3]
            if d!=nD:cnt+=1
            if IS(Y,X) and Arr[Y][X]!='*' and (Map[Y][X]>=cnt or Map[Y][X]==-1):
                Map[Y][X]=cnt
                Q.append((Y,X,d,cnt))
    Que=Q
print(R)