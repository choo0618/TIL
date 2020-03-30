import sys
sys.stdin = open('bj5052.txt','r')

def solution():
    check=L[0]
    for n in L[1:]:
        if check in n:return 'NO'
        else:check=n
    return 'YES'
for t in range(int(input())):
    N=int(input())
    L=[input() for _ in range(N)]
    L.sort()
    print(solution())