import sys
sys.stdin = open('bj13335.txt','r')

from collections import deque
N,W,L=map(int,input().split())
T=deque([int(x)for x in input().split()])
B=deque([0]*W)
R=0
while T:
    B[W-1]=0
    B.rotate()
    if sum(B)+T[0]<=L:B[0]=T.popleft()
    R+=1
print(R+W)