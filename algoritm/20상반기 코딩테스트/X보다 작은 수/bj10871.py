import sys
sys.stdin = open('bj10871.txt','r')

N,X=map(int,input().split())
for p in map(int,input().split()):
    if p<X:print(p,end=' ')