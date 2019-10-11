import sys
sys.stdin = open('4408.txt','r')

T = int(input())
for t in range(T):
    N = int(input())
    A = [[int(x)for x in input().split()]for y in range(N)]
    Map = [0] * 201
    for idx in range(N):
        A[idx].sort()
        for c in range(2):
            if A[idx][c] % 2: A[idx][c] = (A[idx][c] // 2) + 1
            else:A[idx][c] = (A[idx][c] // 2)
        for go in range(A[idx][0], A[idx][1]+1):
            Map[go] += 1
    print('#%d %d'%(t+1,max(Map)))

