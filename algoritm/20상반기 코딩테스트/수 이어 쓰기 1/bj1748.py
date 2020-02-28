import sys
sys.stdin = open('bj1748.txt','r')

N=int(input())
R,i=0,9
while i<=N:
    R+=N
    i*=10
print(R)