import sys
sys.stdin = open('4111.txt','r')

for t in range(int(input())):
    N=int(input())
    K=int(input())
    A=[int(x) for x in input().split()]
    A.sort()
    R=0
    Map=[]
    for i in range(N-1):Map.append(A[i+1]-A[i])
    Map.sort()
    for r in range(N-K):R+=Map[r]
    print('#%d %d'%(t+1,R))