import sys
sys.stdin = open('bj4991.txt','r')

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def IS(y,x):
    return -1<y<H and -1<x<W
def DFS(idx,List,r):
    global R
    if sum(List)==Dust+1:
        if r<R:R=r
        return
    if r>R:return
    for i in range(Dust+1):
        if not List[i]:
            List[i]=1
            DFS(i,List,r+Map[idx][i])
            List[i]=0
while True:
    W,H=map(int,input().split())
    if W+H==0:break
    Arr=[list(map(str,input()))for y in range(H)]
    Que=[]
    Dust,R,tmp=0,987654321,1
    for i in range(H):
        for j in range(W):
            if Arr[i][j]=='o':Que.append((i,j,0));Arr[i][j]=0
            elif Arr[i][j]=='*':Dust+=1;Que.append((i,j,tmp));Arr[i][j]=tmp;tmp+=1
    Map=[[-1]*(Dust+1)for _ in range(Dust+1)]
    for q in Que:
        V=[[0]*W for v in range(H)]
        V[q[0]][q[1]]=1
        Q=[q]
        Map[q[2]][q[2]]=0
        r=0
        while Q:
            r+=1
            q=[]
            for q1 in Q:
                for d in range(4):
                    Y,X=q1[0]+dy[d],q1[1]+dx[d]
                    if IS(Y,X) and Arr[Y][X]!='x' and not V[Y][X]:
                        if type(Arr[Y][X])==int:
                            Map[q1[2]][Arr[Y][X]]=r
                            Map[Arr[Y][X]][q1[2]]=r
                        V[Y][X]=1
                        q.append((Y,X,q1[2]))
            Q=q
    if -1 in Map[0]:print(-1)
    else:DFS(0,[1]+[0]*Dust,0);print(R)

