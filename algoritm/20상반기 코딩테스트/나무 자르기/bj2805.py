import sys
sys.stdin = open('bj2805.txt','r')

N,M=map(int,input().split())
L=[int(x)for x in input().split()]
l,r=0,max(L)
while l<=r:
    Mid=(l+r)//2
    c=0
    for n in L:c+=n-Mid if n>=Mid else 0
    if c>=M:l=Mid+1
    else:r=Mid-1
print(r)