import sys
sys.stdin = open('bj9372.txt','r')

T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    for i in range(M):map(int,input().split())
    print(N-1)