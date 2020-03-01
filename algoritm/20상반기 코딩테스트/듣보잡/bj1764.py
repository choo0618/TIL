import sys
sys.stdin = open('bj1764.txt','r')

N,M=map(int,input().split())
L=[input()for _ in range(N+M)]
L.sort()
Set=set(L)
print(N+M-len(Set))
for i in range(N+M-1):
    if L[i]==L[i+1]:print(L[i])