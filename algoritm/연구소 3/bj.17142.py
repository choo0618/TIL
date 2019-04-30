import sys
sys.stdin = open('bj.17142.txt','r')

L=[int(x)for x in input().split()]
A=[[int(x)for x in input().split()]for y in range(L[0])]

print(L)
print(A)