import sys
sys.stdin=open('bj12886.txt','r')

from collections import deque
A,B,C=map(int,input().split())
Sum=A+B+C
T=1
if Sum%3:T=0
Map=[[0]*(Sum+1) for _ in range(Sum+1)]
Map[min(A,B,C)][max(A,B,C)]=1
Q=deque([(A,B,C)])
R=0
while Q and T:
    a,b,c=Q.popleft()
    if a==b==c:R=1;break
    for x,y in [(a,b),(a,c),(b,c)]:
        if x<y:x,y=y,x
        x,y=x-y,2*y
        z=Sum-x-y
        Min,Max=min(x,y,z),max(x,y,z)
        if not Map[Min][Max]:
            Map[Min][Max]=1
            Q.append((x,y,z))
print(R)
