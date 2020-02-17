import sys
sys.stdin = open('bj14395.txt','r')

from collections import deque
def Cal(n,x):
    if x=='+':return n+n
    elif x=='-':return n-n
    elif x=='*':return n*n
    else:return n//n
S,T=map(int,input().split())
Q=deque([(S,'')])
R=-1 if S!=T else 0
Set=set()
Set.add(S)
while Q and S!=T:
    n,s=Q.popleft()
    if n==T:R=s;break
    for c in '*+-/':
        if c=='/' and not n:continue
        next=Cal(n,c)
        if 0<=next<=10000000000 and not next in Set:
            Set.add(next)
            Q.append((next,s+c))
print(R)