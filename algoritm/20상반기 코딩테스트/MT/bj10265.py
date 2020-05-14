import sys
sys.stdin = open('bj10265.txt','r')

def DFS(x):
    global c,r
    if DP[x]:return DP[x]
    if V[x]:
        cnt,tmp,C[x]=1,L[x],1
        while x!=tmp:
            cnt+=1
            C[tmp]=1
            tmp=L[tmp]
        if cnt<=K:r.append(cnt)
        return cnt
    V[x]=1
    tmp=DFS(L[x])
    if not C[x]:tmp+=1
    DP[x]+=tmp
    # if DP[x]<=K:r.append(DP[x])
    return DP[x]
N,K=map(int,input().split())
L=[0]+[int(x)for x in input().split()]
c=1
C=[0]*(N+1)
V=[0]*(N+1)
DP=[0]*(N+1)
r=[]
for i in range(1,N+1):
    if not DP[i]:DFS(i)
    if C[i]==0 and DP[i]<=K:r.append(DP[i])
print(DP)
r.sort()
print(r)
R=sum(r)
if R>K:
    for n in r:
        R-=n
        if R<=K:break
print(R)
