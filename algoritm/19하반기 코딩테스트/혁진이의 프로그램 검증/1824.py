import sys
sys.stdin = open('1824.txt', 'r')

dx = [1,0,-1,0]
dy = [0,1,0,-1]

T = int(input())
for t in range(T):
    L = [int(x)for x in input().split()]
    A = [list(map(str,input()))for _ in range(L[0])]
    Map = [[[0, 0, 0, 0, [0]*16]for m in range(L[1])] for _ in range(L[0])]
    Result = 'NO'
    # y, x, 방향, Memory
    Que = [[0,0,0,0]]
    while Que:
        Check = 0
        Q = []
        for q in Que:
            if Map[q[0]][q[1]][q[2]] and Map[q[0]][q[1]][4][q[3]]:
                continue
            tmp = A[q[0]][q[1]]
            Map[q[0]][q[1]][q[2]] = 1
            Map[q[0]][q[1]][4][q[3]] = 1
            d_check = 0
            if tmp.isdigit():
                q[3] = int(A[q[0]][q[1]])
            elif tmp == '<':
                q[2] = 2
            elif tmp == '>':
                q[2] = 0
            elif tmp == '^':
                q[2] = 3
            elif tmp == 'v':
                q[2] = 1
            elif tmp == '_':
                if not q[3]: q[2] = 0
                else: q[2] = 2
            elif tmp == '|':
                if not q[3]: q[2] = 1
                else: q[2] = 3
            elif tmp == '?':
                d_check = 1
            elif tmp == '.':
                pass
            elif tmp == '@':
                Result = 'YES'
            elif tmp == '+':
                q[3] += 1
                if q[3] == 16:
                    q[3] = 0
            elif tmp == '-':
                q[3] -= 1
                if q[3] == -1:
                    q[3] = 15
            if d_check:
                for d in range(4):
                    nY = q[0] + dy[d]
                    nX = q[1] + dx[d]
                    if nY == -1:nY = L[0] - 1
                    elif nY == L[0]:nY = 0
                    if nX == -1:nX = L[1] - 1
                    elif nX == L[1]:nX = 0
                    Q.append([nY, nX, d, q[3]])
            else:
                nY = q[0] + dy[q[2]]
                nX = q[1] + dx[q[2]]
                if nY == -1:nY = L[0] - 1
                elif nY == L[0]:nY = 0
                if nX == -1:nX = L[1] - 1
                elif nX == L[1]:nX = 0
                Q.append([nY, nX, q[2], q[3]])
        if Result == 'YES':break
        Que = Q
    print('#%d %s'%(t+1, Result))

