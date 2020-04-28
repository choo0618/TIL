import sys
sys.stdin = open('bj14226.txt','r')

from collections import deque
S=int(input())
Q=deque([(1,0,0)])
Map=[[0]*(S+1) for _ in range(S+1)]
while Q:
    b,c,t=Q.popleft()
    if b==S:print(t);break
    for B,C in (b,b),(b+c,c),(b-1,c):
        if 0<=B<=S and not Map[B][C]:Map[B][C]=1;Q.append((B,C,t+1))

    # if b!=c and not Map[b][b]:Map[b][b]=1;Q.append((b,b,t+1))
    # if c and b+c<=S and not Map[b+c][c]:Map[b+c][c]=1;Q.append((b+c,c,t+1))
    # if b and not Map[b-1][c]:Map[b-1][c]=1;Q.append((b-1,c,t+1))
