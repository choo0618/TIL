import sys
sys.stdin = open('4008.txt','r')

def Cal(a,b,c):
    if not c:return a+b
    elif c==1:return a-b
    elif c==2:return a*b
    else:return a//b if a>=0 else -(abs(a)//abs(b))
def DFS(r,idx):
    global Min,Max
    if idx==N:
        Min=min(Min,r)
        Max=max(Max,r)
        return
    for i in range(4):
        if not C[i]:continue
        C[i]-=1
        c=Cal(r,L[idx],i)
        DFS(c,idx+1)
        C[i]+=1
for t in range(int(input())):
    N=int(input())
    C=list(map(int,input().split()))
    L=list(map(int,input().split()))
    Min=10**9
    Max=-10**9
    DFS(L[0],1)
    print('#%d %d'%(t+1,Max-Min))
