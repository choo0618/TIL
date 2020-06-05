import sys
sys.stdin = open('4013.txt','r')

from collections import deque
def Rotate(a,b,c,x,y):
    for i in range(a,b,c):
        if A[i][x]!=A[i+c][y]:M[i+c]=-M[i]
        else:return
for t in range(int(input())):
    K=int(input())
    A=[deque(int(x)for x in input().split())for y in range(4)]
    for k in range(K):
        M=[0]*4
        n,d=map(int,input().split())
        M[n-1]=d
        Rotate(n-1,3,1,2,6)
        Rotate(n-1,0,-1,6,2)
        for i in range(4):
            if M[i]:A[i].rotate(M[i])
    print('#%d %d'%(t+1,A[0][0]+2*A[1][0]+4*A[2][0]+8*A[3][0]))
