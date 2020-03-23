import sys
sys.stdin = open('bj11047.txt','r')

N,K=map(int,input().split())
L=[int(input())for x in range(N)]
R=0
for i in range(N-1,-1,-1):
    R+=K//L[i]
    K%=L[i]
print(R)
