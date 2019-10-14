import sys
sys.stdin = open('6206.txt', 'r')

import itertools
T = int(input())
for t in range(T):
    M, N = map(int, input().split())
    Result = M**N
    tmp = M-1
    while tmp:
        up = 1
        down = 1
        for u in range(1,M+1):
            up*=u
        for d in range(1,tmp+1):
            down*=d
        Result -= (up//down)
        tmp -= 1
    # comb = 0
    # if M == 1:
    #     Result = 1
    # else:
    #     Result = (M**N) % 1000000007

    print('#%d %d'%(t+1, Result))
