import sys
sys.stdin = open('bj14888.txt','r')

def Cal(a,b,c):
    if c==0:return a+b
    elif c==1:return a-b
    elif c==2:return a*b
    else:
        if a*b<0:return -(abs(a)//abs(b))
        return a//b
def DFS(idx,r):
    global Min,Max
    if idx==N:
        Min,Max=min(Min,r),max(Max,r)
        return
    for c in range(4):
        if C[c]==0 or (c==3 and L[idx]==0):continue
        C[c]-=1
        DFS(idx+1,Cal(r,L[idx],c))
        C[c]+=1
N=int(input())
L=[int(x)for x in input().split()]
C=[int(x)for x in input().split()]
Min,Max=10**9,-10**9
DFS(1,L[0])
print(Max)
print(Min)