import sys
sys.stdin = open('4613.txt','r')

import itertools

T = int(input())
for t in range(T):
    N, M = map(int,input().split())
    A = [input()for y in range(N)]
    Result = 987654321
    WBR = [0,0,0]
    Map = []
    for Line in A:
        Color = [0, 0, 0]
        for color in Line:
            if color == 'W':
                Color[0] += 1
            elif color == 'B':
                Color[1] += 1
            else:
                Color[2] += 1
        r, g, b = sum(Color[1:3]), Color[0]+Color[2] , sum(Color[0:2])
        Map += [[r, g, b]]
    Comb = list(itertools.combinations_with_replacement([int(_)for _ in range(1,N-1)],2))
    for comb in Comb:
        result = 0
        for idx, m in enumerate(Map):
            if idx < comb[0]:
                result += m[0]
            elif idx > comb[1]:
                result += m[2]
            else:
                result += m[1]
        if result < Result:
            Result = result
    print('#%d %d'%(t+1,Result))

