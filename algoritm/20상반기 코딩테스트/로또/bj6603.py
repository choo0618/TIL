import sys
sys.stdin = open('bj6603.txt','r')

import itertools

while True:
    L=[int(x)for x in input().split()]
    N=L.pop(0)
    if not N:break
    for i in list(itertools.combinations(L,6)):
        for p in i:print(p,end=' ')
        print()
    print()


