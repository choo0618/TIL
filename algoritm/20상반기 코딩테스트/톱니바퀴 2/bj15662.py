import sys
sys.stdin= open('bj15662.txt','r')

from collections import deque
N=int(input())
A=[deque(list(map(int,input())))for _ in range(N)]
for _ in range(int(input())):
    a,b=map(int,input().split())
    T=[0]*N
    T[a-1]=b
    for l in range(a-1,N-1):
        if A[l][2]!=A[l+1][6]:T[l+1]=-T[l]
        else:break
    for r in range(a-1,0,-1):
        if A[r][6]!=A[r-1][2]:T[r-1]=-T[r]
        else:break
    for t in range(N):
        if T[t]:A[t].rotate(T[t])
print(sum(A[x][0]for x in range(N)))
