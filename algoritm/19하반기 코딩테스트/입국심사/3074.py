import sys
sys.stdin = open('3074.txt','r')

T = int(input())
for t in range(T):
    N ,M = map(int, input().split())
    L = [int(input())for x in range(N)]
    Left = 0
    Right = max(L) * M
    answer = Right
    while Left <= Right:
        Mid = (Left + Right) // 2
        People = 0
        for p in L:
            People += Mid // p
        if People == M:
            answer = Mid
            Right = Mid - 1
        elif People < M:
            Left = Mid +1
        else:
            Right = Mid - 1
    if answer == max(L) * M:
        answer = Right + 1
    print('#%d %d'%(t+1, answer))