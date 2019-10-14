import sys
sys.stdin = open('4050.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    L.reverse()
    Result = 0
    for idx in range(N):
        if idx%3 == 2:continue
        Result += L[idx]
    print('#%d %d'%(t+1, Result))