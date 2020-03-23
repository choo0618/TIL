import sys
sys.stdin = open('bj11729.txt','r')

def Hanoi(n,a,b,c):
    if n==1:print(a,c)
    else:
        Hanoi(n-1,a,c,b)
        print(a,c)
        Hanoi(n-1,b,a,c)
N=int(input())
print(2**N-1)
Hanoi(N,1,2,3)
