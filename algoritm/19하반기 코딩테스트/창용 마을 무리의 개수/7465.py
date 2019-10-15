import sys
sys.stdin = open('7465.txt', 'r')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    if not M:
        print('#%d %d' % (t + 1, N))
        continue
    Arr = [[int(z)for z in input().split()]for _ in range(M)]
    Map = [1]+[0]*N
    n = 1
    for m in Arr:
        if not Map[m[0]]:
            Map[m[0]] = n
            Que = [m[0],m[1]]
            while Que:
                que = []
                for q in Que:
                    Map[q] = n
                    for x in Arr:
                        if x[0] == q and not Map[x[1]]:
                            que.append(x[1])
                        if x[1] == q and not Map[x[0]]:
                            que.append(x[0])
                Que = que
            n += 1
    print('#%d %d'%(t+1, max(Map) + Map.count(0)))