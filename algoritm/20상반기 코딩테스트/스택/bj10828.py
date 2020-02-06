import sys
sys.stdin=open('bj10828.txt','r')

import sys
input=sys.stdin.readline
N=int(input())
Que=[]
size=0
while N:
    L=list(input().split())
    if L[0]=='push':Que.append(L[1]);size+=1
    elif L[0]=='pop':print(Que.pop() if Que else -1);size=max(size-1,0)
    elif L[0]=='size':print(size)
    elif L[0]=='empty':print(0 if size else 1)
    else:print(Que[-1] if size else -1)
    N-=1