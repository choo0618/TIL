import sys
sys.stdin = open('bj5397.txt','r')

from collections import deque
T=int(input())
for t in range(T):
    L=deque()
    R=deque()
    for s in input():
        if s=='<':
            if L:R.appendleft(L.pop())
        elif s=='>':
            if R:L.append(R.popleft())
        elif s=='-':
            if L:L.pop()
        else:
            L.append(s)
    L.extend(R)
    print(''.join(L))