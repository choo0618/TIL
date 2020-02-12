import sys
sys.stdin = open('7508.txt','r')

for t in range(int(input())):
    N=int(input())
    L=[int(x)for x in input().split()]
    Sum=sum(L)
    V=[1]+[0]*Sum
    for i in range(N):
        for j in range(Sum,-1,-1):
            if V[j]:V[j+L[i]]=1
    print('#%d %d'%(t+1,sum(V)))