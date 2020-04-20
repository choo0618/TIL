import sys
sys.stdin = open('5658.txt','r')

from collections import deque
for t in range(int(input())):
    N,K=map(int,input().split())
    L=deque(list(map(str,input())))
    Set=set()
    for r in range(N//4):
        l=''.join(L)
        for i in range(0,N,N//4):Set.add(int(l[i:i+N//4],16))
        L.rotate()
    print('#%d %d'%(t+1,sorted(Set,reverse=1)[K-1]))