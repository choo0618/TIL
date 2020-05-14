import sys
sys.stdin = open('bj10423.txt','r')

def MST():
    P=list(range(N))
    def find(x):
        if P[x]!=x:P[x]=find(P[x])
        return P[x]
    def union(a,b):
        P[b]=a
    def Check(l):
        for i in l:
            if not k[find(i)]:return 0
        return 1
    R,cnt=0,0
    for w,x,y in L:
        a,b=find(x),find(y)
        if k[a]==k[b]==1:continue
        if a!=b:
            if k[b]:a,b=b,a
            R+=w;union(a,b);cnt+=1
        if Check(P):return R
N,M,K=map(int,input().split())
k=[0]*N
for i in map(int,input().split()):k[i-1]=1
L=[]
for i in range(M):
    u,v,w=map(int,input().split())
    u-=1;v-=1
    if k[v]:u,v=v,u
    L.append((w,u,v))
L.sort()
print(MST())
