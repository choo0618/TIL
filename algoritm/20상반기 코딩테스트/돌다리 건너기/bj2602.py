import sys
sys.stdin = open('bj2602.txt','r')

def DFS(y,x,i):
    if DP[y][x]:return DP[y][x]
    if i==l:DP[y][x]=1;return 1
    Y=(y+1)%2
    for j in range(x+1,Len):
        if A[Y][j]==S[i]:DP[y][x]+=DFS(Y,j,i+1)
    return DP[y][x]
S=input()
R,l=0,len(S)
A=[input()for _ in range(2)]
Len=len(A[0])
DP=[[0]*Len for _ in range(2)]
for j in range(Len):
    if A[0][j]==S[0]:R+=DFS(0,j,1)
    if A[1][j]==S[0]:R+=DFS(1,j,1)
print(R)