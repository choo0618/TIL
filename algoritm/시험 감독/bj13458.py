import sys
sys.stdin = open('bj13458.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
T=[int(x)for x in input().split()]
R=0
for l in L:
    l-=T[0]
    R+=1
    if l>0:
        if l%T[1]:R+=1
        R+=l//T[1]
print(R)