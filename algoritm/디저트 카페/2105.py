import sys
sys.stdin = open('2105.txt','r')

import copy
dx=[1,0,-1,0]
dy=[0,1,0,-1]
di=[1,-1]
def IS(y,x):
    if 0<y<N-1 and 0<x<N-1:return True
    return False
T=int(input())
for t in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    R=-1
    for i in range(1,N-1):
        for j in range(1,N-1):
            print(i,j)
            d=set()
            for dir in range(4):
                d.add(A[i+dy[dir]][j+dx[dir]])
            if len(d)==4:
                for z in di:
                    dd,r,n=copy.deepcopy(d),4,1
                    while True:
                        if IS(i+n*z,j+n):
                            for ddir in range(4):dd.add(A[i+n*z+dy[ddir]][j+n+dx[ddir]])
                        else:break
                        if len(dd)!=r+2:break
                        else:r+=2
                        n+=1
                    if r>R:R=r
    print('#%d %d'%(t+1,R))