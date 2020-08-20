import sys
sys.stdin = open('10505.txt','r')

for t in range(int(input())):
    N=int(input())
    L=[int(x)for x in input().split()]
    R,Avg=0,sum(L)/N
    for n in L:
        if n<=Avg:R+=1
    print('#%d %d'%(t+1,R))