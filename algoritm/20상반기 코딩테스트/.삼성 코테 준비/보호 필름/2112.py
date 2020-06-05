import sys
sys.stdin = open('2112.txt','r')

def Check():
    for j in range(M):
        cnt=1
        for i in range(1,N):
            if A[i][j]==A[i-1][j]:
                cnt+=1
                if cnt==K:cnt=0;break
            else:cnt=1
        if cnt:return 0
    return 1
def DFS(idx,n,k):
    global R
    if n==k:
        if K==1 or Check():R=k
        return
    for i in range(idx,N):
        tmp=A[i][:]
        for ab in [[0]*M,[1]*M]:
            A[i]=ab
            DFS(i+1,n+1,k)
            if R!=K:return
        A[i]=tmp
for t in range(int(input())):
    N,M,K=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R=K
    for k in range(K):
        DFS(0,0,k)
        if R!=K:break
    if R==-1:R=K
    print('#%d %d'%(t+1,R))