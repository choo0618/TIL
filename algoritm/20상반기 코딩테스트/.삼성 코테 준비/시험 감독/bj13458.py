import sys
sys.stdin = open('bj13458.txt','r')

N=int(input())
A=[int(x)for x in input().split()]
B,C=map(int,input().split())
for a in A:
    tmp=max(0,a-B)
    N+=tmp//C
    if tmp%C:N+=1
print(N)
