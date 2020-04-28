import sys
sys.stdin = open('bj9613.txt','r')

def GCD(a,b):
    while b:
        tmp=a%b
        a=b
        b=tmp
    return a
for t in range(int(input())):
    N,*L=map(int,input().split())
    R=0
    for i in range(N):
        for j in range(i+1,N):
            R+=GCD(L[i],L[j])
    print(R)