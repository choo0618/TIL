import sys
sys.stdin = open('bj1654.txt','r')

K,N=map(int,input().split())
L=[int(input())for x in range(K)]
l,r=1,max(L)
while l<=r:
    Mid=(l+r)//2
    c=0
    for n in L:c+=n//Mid
    if c>=N:l=Mid+1
    else:r=Mid-1
print(r)