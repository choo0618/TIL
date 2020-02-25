import sys
sys.stdin = open('bj1026.txt','r')

N=int(input())
A=[int(x)for x in input().split()]
B=[int(x)for x in input().split()]
A.sort()
B.sort()
print(sum(A[x]*B[N-x-1]for x in range(N)))


R=0
A.sort()
B.sort()
for i in range(N):
    R+=A[i]*B[N-i-1]
print(R)