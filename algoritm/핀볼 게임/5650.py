import sys
sys.stdin = open('5650.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]