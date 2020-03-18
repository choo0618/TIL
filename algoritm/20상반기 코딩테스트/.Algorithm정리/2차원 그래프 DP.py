# 내리막길 문제 참고
def IS(y,x):
    return -1<y<N and -1<x<N
def DFS(y,x):
    if DP[y][x]!=-1:
        return DP[y][x]
    DP[y][x]=0
    for Y,X in (y,x+1),(y+1,x),(y,x-1),(y-1,x):
        if IS(Y,X):
            DP[y][x]+=DFS(Y,X)
    return DP[y][x]

N=int(input())
A=[[],[]]
DP=[[],[]] # -1로 초기화 : Visit 역할
DP[N-1][N-1]=1