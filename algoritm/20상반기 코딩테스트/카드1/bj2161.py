import sys
sys.stdin = open('bj2161.txt','r')

from collections import deque

N=int(input())
C = deque([int(x+1)for x in range(N)])
G=[]
while len(C)!=1:
    G.append(C.popleft())
    C.rotate(-1)
G.append(C[0])
for g in G:print(g, end = ' ')