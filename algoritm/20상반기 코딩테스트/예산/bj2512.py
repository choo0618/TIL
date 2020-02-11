import sys
sys.stdin = open('bj2512.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
Max=int(input())
l,r=0,Max
while l<=r:
    Mid=(l+r)//2
    c=0
    for n in L:
        c+=n if n<=Mid else Mid
    if c<=Max:l=Mid+1
    else:r=Mid-1
print(min(r,max(L)))