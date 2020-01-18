import sys
sys.stdin = open('bj3709.txt','r')

dx=[1,0,-1,0]
dy=[0,-1,0,1]
def IS(y,x):
    return 0<x<N+1 and 0<y<N+1
T=int(input())
for t in range(T):
    N,R=map(int,input().split())
    Map=[[0]*(N+1) for m in range(N+1)]
    for i in range(R):
        x,y=map(int,input().split())
        Map[x][y]=1
    X,Y=map(int,input().split())
    if X==0:d=0
    elif X==N+1:d=2
    elif Y==0:d=3
    else:d=1
    while True:
        X+=dx[d]
        Y+=dy[d]
        if not IS(Y,X):break
        if Map[X][Y]:
            d+=1
            d%=4
    print(X,Y)