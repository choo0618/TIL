import sys
sys.stdin = open('bj1547.txt','r')

M = int(input())
R=1
for s in range(M):
    N,M = map(int,input().split())
    if N==M:continue
    elif N==R:R=M
    elif M==R:R=N
print(R)