import sys
sys.stdin = open('4111.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    K = int(input())
    L = list(set(map(int, input().split())))
    if N > K:
        Map = [0] * (len(L) - 1)
        for m in range(len(Map)):
            Map[m] = L[m+1] - L[m]
        Map.sort()
        del Map[len(Map)-K+1:]
        Result = sum(Map)
        print('#%d %d'%(t+1, Result))
    else:
        print('#%d %d'%(t+1, 0))