import sys
sys.stdin = open('3459.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    x = 1
    while True:
        tmp = 2 * x + 1
        tmp1 = 2 * tmp
        if tmp1 < N:
            x = tmp1
        elif tmp <= N or tmp1 <= N:
            print('#%d Alice' % (t + 1))
            break
        else:
            print('#%d Bob' % (t + 1))
            break
