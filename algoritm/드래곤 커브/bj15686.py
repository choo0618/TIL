import sys
sys.stdin = open('bj15686.txt','r')

dx=[1,0]
dy=[0,1]
N=int(input())
A=[[int(x)for x in input().split]for y in range(N)]