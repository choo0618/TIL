import sys
sys.stdin = open('bj16953.txt','r')

A,B=map(int,input().split())
R=1
while B>A:
    if B%10==1:B//=10
    elif not B%2:B//=2
    else:break
    R+=1
print(-1 if A!=B else R)