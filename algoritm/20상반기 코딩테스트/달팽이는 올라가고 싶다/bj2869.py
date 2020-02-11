import sys
sys.stdin = open('bj2869.txt','r')

A,B,V=map(int,input().split())
l,r=0,V//(A-B)
while l<=r:
    Mid=(l+r)//2
    if (Mid-1)*(A-B)+A>=V:r=Mid-1
    else:l=Mid+1
print(l)


