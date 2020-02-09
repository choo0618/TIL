import sys
sys.stdin=open('bj1038.txt','r')

from collections import deque
def Check():
    global idx
    while Q and idx<=N:
        n=Q.popleft()
        for i in range(n%10):
            Q.append(n*10+i)
            idx+=1
            Map[idx]=n*10+i
N=int(input())
Map=[0]*1000001
Q=deque()
idx=9
for i in range(9):
    Q.append(i+1)
    Map[i+1]=i+1
Check()
print(-1 if not Map[N] and N else Map[N])
