import sys
sys.stdin = open('bj2164.txt','r')

from collections import deque

N=int(input())
C=deque(int(x+1)for x in range(N))
while len(C)!=1:
    C.popleft()
    C.rotate(-1)
print(C[0])