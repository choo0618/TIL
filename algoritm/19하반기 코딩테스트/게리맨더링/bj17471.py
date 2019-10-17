import sys
sys.stdin = open('bj17471.txt', 'r')

import itertools
def BFS(list, v):
    Que = [list[0]]
    check[Que[0]] = v
    while Que:
        S = Que.pop(0)
        for idx, s in enumerate(Map[S]):
            if s and idx in list and not check[idx]:
                Que.append(idx)
                check[idx] = v
        # que = []
        # for q in Que:
        #     for idx, c in enumerate(Map[q]):
        #         if c and idx in list and not check[idx]:
        #             que.append(idx)
        #             check[idx] = v
        # Que = que
    P = 0
    for p in list:
        if check[p] != v:
            return -1
        else:P += People[p]
    return P

N = int(input())
People = list(map(int, input().split()))
Arr = [[int(x)for x in input().split()]for y in range(N)]
Map = [[0]*N for _ in range(N)]
Result = 987654321
for idx, C in enumerate(Arr):
    for iidx, c in enumerate(C):
        if not iidx:continue
        Map[idx][c-1] = 1
print(Map)
Comb = []
List = [x for x in range(N)]
for n in range(1, N//2+1):
    Comb.append(list(itertools.combinations(List, n)))
for comb in Comb:
    for a_list in comb:
        b_list = []
        for b in range(N):
            if not b in a_list:
                b_list.append(b)
        check = [0]*N
        A = BFS(a_list, 1)
        if A == -1:continue
        B = BFS(b_list, 2)
        if B == -1:continue
        result = abs(A-B)
        if result < Result:
            Result = result
if Result == 987654321:
    print(-1)
else:print(Result)

