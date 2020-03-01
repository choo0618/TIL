import sys
sys.stdin = open('bj2839.txt','r')

N,R=int(input()),0
while N%5 and N>0:
    N-=3
    R+=1
print(R+N//5 if N>=0 else -1)
