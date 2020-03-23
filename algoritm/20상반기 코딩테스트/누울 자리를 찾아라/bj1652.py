import sys
sys.stdin = open('bj1652.txt','r')

N=int(input())
A=[input()+'X'for _ in range(N)]+['X'*(N+1)]
r,c=0,0
for i in range(N):
    for j in range(N-1):
        r+=A[i][j]=='.' and A[i][j+1]=='.' and A[i][j+2]=='X'
        c+=A[j][i]=='.' and A[j+1][i]=='.' and A[j+2][i]=='X'
print(r,c)