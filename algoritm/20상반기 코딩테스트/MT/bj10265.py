import sys
sys.stdin = open('bj10265.txt','r')

def DFS(x,d):
    global r,c
    if DP[x]:
        if C[x]:r[C[x]-1][1]+=d
        return DP[x],C[x]
    if V[x]:
        cnt,tmp,C[x]=1,L[x],c
        while x!=tmp:
            cnt+=1
            C[tmp]=c
            tmp=L[tmp]
        r.append([cnt,d-cnt])
        c+=1
        return cnt,c-1
    V[x]=1
    tmp,tmp1=DFS(L[x],d+1)
    if not C[x]:tmp+=1
    DP[x]+=tmp
    C[x]=tmp1
    return DP[x],tmp1
N,K=map(int,input().split())
L=[0]+[int(x)for x in input().split()]
c=1
C=[0]*(N+1)
V=[0]*(N+1)
DP=[0]*(N+1)
r=[]
for i in range(1,N+1):
    if not DP[i]:DFS(i,0)
R,tmp=[0],0
for n,p in r:
    if n<=K:R.append((n,p));tmp+=1
KS=[[-1]*(K+1) for _ in range(tmp+1)]
for i in range(1,tmp+1):
    w,v=R[i]
    KS[i][w]=v
    for j in range(1,K+1):
        if j>w:
            if KS[i-1][j-w]!=-1:KS[i][j]=max(KS[i-1][j-w]+v,KS[i-1][j])
            else:KS[i][j]=max(KS[i][j],KS[i-1][j])
        else:KS[i][j]=max(KS[i][j],KS[i-1][j])
ans=0
for i in range(1,K+1):
    if KS[tmp][i]!=-1:ans=max(ans,i+KS[tmp][i])
print(min(ans,K))