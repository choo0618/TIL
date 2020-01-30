import sys
sys.stdin=open('bj1175.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<N and -1<x<M
N,M=map(int,input().split())
Arr=[list(map(str,input()))for _ in range(N)]
S,C,t=0,2,0
for i in range(N):
    for j in range(M):
        if Arr[i][j]=='S':S=(i,j,-1,0,0)
        elif Arr[i][j]=='C':Arr[i][j]=t;t+=1
Map=[[[[0]*4 for _ in range(M)]for __ in range(N)]for ___ in range(1<<2)]
Que=[S]
Map[0][S[0]][S[1]]=[1]*4
Check,tmp=0,0
while Que and not Check:
    Q=[]
    for q in Que:
        if q[4]==C:Check=1;break
        for d in range(4):
            if q[2]==d:continue
            Y,X,c,cnt=q[0]+dy[d],q[1]+dx[d],q[3],q[4]
            if IS(Y,X)and Arr[Y][X]!='#' and not Map[c][Y][X][d]:
                if Arr[Y][X]==1 or not Arr[Y][X]:
                    if (c&1<<Arr[Y][X])!=1<<Arr[Y][X]:
                        cnt+=1
                    c=(c|1<<Arr[Y][X])
                Map[c][Y][X][d]=1
                Q.append((Y,X,d,c,cnt))
    tmp+=1
    Que=Q
if Check:print(tmp-1)
else:print(-1)
