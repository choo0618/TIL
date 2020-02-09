import sys
sys.stdin=open('bj1051.txt','r')

N,M=map(int,input().split())
A=[input()for _ in range(N)]
R=1
for i in range(N):
    for j in range(M):
        for s in range(min(N-i,M-j)):
            if A[i][j]==A[i+s][j]==A[i][j+s]==A[i+s][j+s]:R=max(R,s+1)
print(R*R)
