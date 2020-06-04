import sys
sys.stdin = open('4008.txt','r')

def Cal(a,b,c):
    if c==0:return a+b
    elif c==1:return a-b
    elif c==2:return a*b
    else:return a//b if a>=0 else -(abs(a)//abs(b))
def DFS(idx,r):
    global Min,Max
    if idx==N:
        Min=min(Min,r)
        Max=max(Max,r)
        return
    for c in range(4):
        if C[c]==0:continue
        C[c]-=1
        DFS(idx+1,Cal(r,Num[idx],c))
        C[c]+=1
for t in range(int(input())):
    N=int(input())
    C=[int(x)for x in input().split()]
    Num=[int(x)for x in input().split()]
    Max,Min=-10**9,10**9
    DFS(1,Num[0])
    print('#%d %d'%(t+1,Max-Min))