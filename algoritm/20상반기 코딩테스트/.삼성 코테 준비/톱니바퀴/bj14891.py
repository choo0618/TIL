import sys
sys.stdin = open('bj14891.txt','r')

from collections import deque
A=[deque(list(map(int,input())))for y in range(4)]
for t in range(int(input())):
    i,t=map(int,input().split())
    i-=1
    ro=[0]*4
    ro[i]=t
    for r in range(i,3):
        if A[r][2]!=A[r+1][6]:ro[r+1]=-ro[r]
        else:break
    for l in range(i,0,-1):
        if A[l][6]!=A[l-1][2]:ro[l-1]=-ro[l]
        else:break
    for r in range(4):
        if ro[r]:A[r].rotate(ro[r])
print(A[0][0]+2*A[1][0]+4*A[2][0]+8*A[3][0])
