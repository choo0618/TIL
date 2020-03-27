import sys
sys.stdin = open('test.txt','r')

for t in range(int(input())):
    A,B=map(int,input().split())
    L=A*B
    while B:A,B=B,A%B
    print(L//A)

import pprint
L=[[1,2,3],[4,5,6],[7,8,9]]
pprint.pprint(L)
L=list(map(list,zip(*L[::1])))
pprint.pprint(L)

