import sys
sys.stdin = open('bj1333.txt','r')

N,L,D = map(int,input().split())
tmp=D
T=0
while N:
    T+=L
    while D<T:D+=tmp
    if T<=D<T+5:break
    T+=5
    N-=1
print(D)