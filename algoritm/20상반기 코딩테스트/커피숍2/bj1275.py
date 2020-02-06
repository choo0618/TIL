import sys
sys.stdin = open('bj1275.txt','r')

N,Q=map(int,input().split())
L=[int(x)for x in input().split()]
while Q:
    x,y,a,b=map(int,input().split())
    if x>y:x,y=y,x
    print(sum(L[x-1:y]))
    L[a-1]=b
    Q-=1