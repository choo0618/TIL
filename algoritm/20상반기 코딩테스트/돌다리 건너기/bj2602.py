import sys
sys.stdin = open('bj2602.txt','r')

def DFS(y,x,i):
    if i==l:return 1
    if DP[y][x][i]!=-1:return DP[y][x][i]
    DP[y][x][i]=0
    for j in range(x+1,Len-l+i+1):
        if A[(y+1)%2][j]==S[i]:DP[y][x][i]+=DFS((y+1)%2,j,i+1)
    return DP[y][x][i]
S=input()
A=['.'+input()for _ in range(2)]
R,l,Len=0,len(S),len(A[0])
DP=[[[-1]*l for _ in range(Len)] for __ in range(2)]
R+=DFS(0,0,0)
R+=DFS(1,0,0)
print(R)