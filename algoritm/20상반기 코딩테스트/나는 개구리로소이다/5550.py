import sys
sys.stdin = open('5550.txt', 'r')

croak = ['c', 'r', 'o', 'a', 'k']
T = int(input())
for t in range(T):
    L = list(map(str,input()))
    for idx in range(len(L)):
        L[idx] = croak.index(L[idx])
    Result = [[0, 0, 0, 0, 0]]
    R = 0
    check = 1
    for frog in L:
        if not frog:
            for idx, f in enumerate(Result):
                if not sum(f):
                    Result[idx][0] = 1
                    break
                else:
                    if idx == len(Result)-1:
                        Result.append([0, 0, 0, 0, 0])
        else:
            for idx, f in enumerate(Result):
                if not Result[idx][frog] and Result[idx][frog-1]:
                    Result[idx][frog] = 1
                    check = 0
                    if frog == 4:
                        Result[idx] = [0, 0, 0, 0, 0]
                    break
            if check:break
    if check:
        print('#%d %d' %(t+1,-1))
    else:
        for r in Result:
            if any(r):
                R = -1
                break
            else: R += 1
        print('#%d %d' %(t+1,R))
