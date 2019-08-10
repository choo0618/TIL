import sys
sys.stdin = open('bj5373.txt','r')

N=int(input())
L=[x for x in input().split()]
print(L)
M=[[[[0for z in range(3)]for i in range(3)] for x in range(3)]for y in range(4)]
print(M)
print(M[0][0][0][0])