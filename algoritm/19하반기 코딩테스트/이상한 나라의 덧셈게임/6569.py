import sys
sys.stdin = open('6569.txt', 'r')

T = int(input())
for t in range(T):
    N = input()
    cnt = 0
    while int(N)//10:
        tmp = int(N[0])+int(N[1])
        N = str(tmp) + N[2:]
        cnt += 1
    if cnt%2:print('#%d A'%(t+1))
    else:print('#%d B'%(t+1))
