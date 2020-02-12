import sys
sys.stdin = open('4008.txt','r')

def Cal(a,b,t):
    if not t:return a+b
    elif t==1:return a-b
    elif t==2:return a*b
    else:return abs(a)//abs(b) if a>=0 else -(abs(a)//abs(b))
def DFS(x,idx):
    global Min,Max
    if idx==N-1:
        Min=min(x,Min)
        Max=max(x,Max)
        return
    for i in range(4):
        if not M[i]:continue
        M[i]-=1
        DFS(Cal(x,L[idx+1],i),idx+1)
        M[i]+=1
for t in range(int(input())):
    N=int(input())
    M=[int(x)for x in input().split()]
    L=[int(x)for x in input().split()]
    Min,Max=10**9,-10**9
    DFS(L[0],0)
    print('#%d %d'%(t+1,Max-Min))