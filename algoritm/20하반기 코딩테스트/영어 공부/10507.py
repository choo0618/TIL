import sys
sys.stdin = open('10507.txt','r')

def DFS(i,s,p):
    global R
    if i==Len+1:
        R=max(R,s+p)
        return
    if p==0:
        if S[I[i]-2]:R=max(R,s)
        else:R=max(R,s+S[I[i]-1])
        return
    idx=I[i]
    tmp=min(p,S[idx])
    r=s+S[idx-1]+tmp
    S[idx]-=tmp
    DFS(i+1,r,p-tmp)
    S[idx]+=tmp
    if s==0:DFS(i+1,s,p)
for t in range(int(input())):
    N,P=map(int,input().split())
    L=[int(x)for x in input().split()]
    S,I,Len=[1],[],0
    R=0
    for i in range(1,N):
        if L[i]-L[i-1]==1:S[-1]+=1
        else:S.append(L[i]-L[i-1]-1);I.append(len(S)-1);S.append(1);Len+=1
    I.append(len(S)),S.append(0)
    DFS(0,0,P)
    print('#%d %d'%(t+1,R))