import sys
sys.stdin = open('bj15684.txt','r')

def Chk():
    for j in range(1,N):
        n=j
        for i in range(H):n+=A[i][n]
        if n!=j:return 0
    return 1
def DFS(idx,t):
    global R
    if t==r:
        if Chk():R=t
        return
    for i in range(idx,c):
        y,x=l[i]
        if A[y][x] or A[y][x+1]:continue
        A[y][x],A[y][x+1]=1,-1
        DFS(i+1,t+1)
        A[y][x],A[y][x+1]=0,0
N,M,H=map(int,input().split())
A=[[0]*(N+2)for _ in range(H)]
for _ in range(M):
    a,b=map(int,input().split())
    A[a-1][b],A[a-1][b+1]=1,-1
c,l=0,[]
for i in range(H):
    for j in range(1,N):
        if A[i][j]==A[i][j+1]==0:l.append((i,j));c+=1
R,r=-1,0
while R==-1 and r!=4:DFS(0,0);r+=1
print(R)