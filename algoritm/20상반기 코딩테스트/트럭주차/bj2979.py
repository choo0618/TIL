import sys
sys.stdin = open('bj2979.txt','r')

A,B,C = map(int,input().split())
Map,R = [],0
for i in range(3):
    S,E = map(int,input().split())
    Map +=[0]*(E-len(Map))
    for c in range(S,E):
        Map[c]+=1
for r in Map:
    if r==1:R+=A
    elif r==2:R+=2*B
    elif r==3:R+=3*C
print(R)