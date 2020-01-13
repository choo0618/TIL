import sys
sys.stdin = open('bj3985.txt','r')

L = int(input())
N = int(input())
Map = [0]*(L+1)
Man=[0]*(N+1)
R,M=0,0
for i in range(N):
    s,e = map(int,input().split())
    r = e-s
    if r>R:
        R=r
        M=i+1
    for m in range(s,e+1):
        if not Map[m]:
            Map[m]=i+1
            Man[i+1]+=1
print(M)
print(Man.index(max(Man)))
