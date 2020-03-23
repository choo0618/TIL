import sys
sys.stdin = open('bj11399.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
L.sort()
R=0
for i in range(N):R+=L[i]*(N-i)
print(R)