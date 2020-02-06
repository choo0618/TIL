import sys
sys.stdin=open('bj10866.txt','r')

from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
Q=deque()
for t in range(N):
    L=list(input().split())
    if L[0]=='push_front':Q.appendleft(L[1])
    elif L[0]=='push_back':Q.append(L[1])
    elif L[0]=='pop_front':print(Q.popleft() if Q else -1)
    elif L[0]=='pop_back':print(Q.pop() if Q else -1)
    elif L[0]=='size':print(len(Q))
    elif L[0]=='empty':print(0 if Q else 1)
    elif L[0]=='front':print(Q[0] if Q else -1)
    else:print(Q[-1] if Q else -1)


