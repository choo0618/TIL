import sys
sys.stdin = open('bj2718.txt','r')

for t in range(int(input())):
    N=int(input())
    DP=[1,1,5,11]+[0]*(N-3)
    for i in range(4,N+1):
        tmp=DP[i-2]*4+DP[i-1]
        for j in range(3,i+1):
            if j&1:tmp+=DP[i-j]*2
            else:tmp+=DP[i-j]*3
        DP[i]=tmp
    print(DP[N])

def DFS(n,b):
    if n<0:return 0
    if n<1:return b==0
    if DP[n][b]:return DP[n][b]
    r=0
    if not b:
        r+=DFS(n-1,0)
        r+=DFS(n-1,3)
        r+=DFS(n-1,9)
        r+=DFS(n-1,12)
        r+=DFS(n-2,0)
    elif b==3:
        r+=DFS(n-1,0)
        r+=DFS(n-1,12)
    elif b==6:
        r+=DFS(n-1,9)
    elif b==9:
        r+=DFS(n-1,0)
        r+=DFS(n-1,6)
    elif b==12:
        r+=DFS(n-1,0)
        r+=DFS(n-1,3)
    DP[n][b]=r
    return r
for t in range(int(input())):
    N=int(input())
    DP=[[0]*13 for _ in range(N+1)]
    print(DFS(N,0))
