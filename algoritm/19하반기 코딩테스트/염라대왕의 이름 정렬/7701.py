import sys
sys.stdin = open('7701.txt', 'r')

T = int(input())
for t in range(T):
    print('#%d' % (t + 1))
    N = int(input())
    Arr = [input().strip('\r') for y in range(N)]
    Arr = list(set(Arr))
    Arr = sorted(Arr, key=lambda x : (len(x), x))
    for c in Arr:print(c)