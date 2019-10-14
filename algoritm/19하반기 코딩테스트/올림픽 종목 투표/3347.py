import sys
sys.stdin = open('3347.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Result = [0] * N
    for b in B:
        for idx, a in enumerate(A):
            if a <= b:
                Result[idx] += 1
                break
    print('#%d %d'%(t+1, Result.index(max(Result))+1))