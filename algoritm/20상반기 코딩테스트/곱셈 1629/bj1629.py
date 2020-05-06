import sys
sys.stdin = open('bj1629.txt','r')

def POW(a,b,c):
    if b==1:return a
    tmp=POW(a,b//2,c)
    if b%2:return (tmp*tmp%c*a)%c
    return tmp*tmp%c

A,B,C=map(int,input().split())
print(POW(A%C,B,C))

print(pow(*map(int,input().split())))
