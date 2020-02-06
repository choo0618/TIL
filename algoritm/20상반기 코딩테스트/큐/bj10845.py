import sys
sys.stdin=open('bj10845.txt','r')

import sys
input=sys.stdin.readline
N=int(input())
Q=[]
for t in range(N):
    L=list(input().split())
    if L[0]=='push':Q.append(L[1])
    elif L[0]=='pop':print(Q.pop(0) if Q else -1)
    elif L[0]=='size':print(len(Q))
    elif L[0]=='empty':print(0 if Q else 1)
    elif L[0]=='front':print(Q[0] if Q else -1)
    else:print(Q[-1] if Q else -1)

