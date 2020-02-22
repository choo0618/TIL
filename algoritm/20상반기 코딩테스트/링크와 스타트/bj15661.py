import sys
sys.stdin = open('bj15661.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
V=[0]*N
R=10**9
