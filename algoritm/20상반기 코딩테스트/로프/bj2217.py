import sys
sys.stdin = open('bj2217.txt','r')

N=int(input())
L=[int(input())for _ in range(N)]
L.sort(reverse=1)
R=0
for i in range(N):R=max(R,L[i]*(i+1))
print(R)