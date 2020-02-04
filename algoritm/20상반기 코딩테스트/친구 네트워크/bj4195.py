import sys
sys.stdin = open('bj4195.txt','r')

def find(x):
    if Net[x]!=x:Net[x]=find(Net[x])
    return Net[x]
def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        Net[a]=b
        Cnt[b]+=Cnt[a]
        Cnt[a]=1
    return Cnt[b]
for t in range(int(input())):
    N=int(input())
    P={}
    Net=list(range(2*N))
    Cnt=[1]*(2*N)
    idx=0
    for n in range(N):
        a,b=map(str,input().split())
        if not a in P:P[a]=idx;idx+=1
        if not b in P:P[b]=idx;idx+=1
        print(union(P[a],P[b]))
