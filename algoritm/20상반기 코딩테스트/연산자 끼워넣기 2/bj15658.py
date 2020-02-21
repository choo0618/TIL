import sys
sys.stdin = open('bj15658.txt','r')

def Cal(a,b,c):
    if not c:return a+b
    elif c==1:return a-b
    elif c==2:return a*b
    else:
        if a<0:return -1*(abs(a)//abs(b))
        return a//b
def DFS(r,i):
    global Min,Max
    if i==N:
        Min=min(Min,r)
        Max=max(Max,r)
        return
    for c in range(4):
        if not L[c] or (c==3 and not Num[i]):continue
        L[c]-=1
        DFS(Cal(r,Num[i],c),i+1)
        L[c]+=1
N=int(input())
Num=[int(x)for x in input().split()]
L=[int(x)for x in input().split()]
Min,Max=10**10,-10**10
DFS(Num[0],1)
print(Max)
print(Min)