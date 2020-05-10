import sys
sys.stdin = open('bj4395.txt','r')

for t in range(int(input())):
    X,Y=map(int,input().split())
    Y-=X
    R=0
    while R*R<Y:R+=1
    if R*R-R<Y:R=2*R-1
    else:R=2*R-2
    print(max(0,R))

