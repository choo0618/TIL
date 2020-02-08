import sys
sys.stdin = open('bj1525.txt')

from collections import deque
S=''.join(list(''.join(input().split())for y in range(3)))
Que=deque([(S,S.index('0'),0)])
Set=set()
Set.add(S)
R=-1
while Que:
    s,i,c=Que.popleft()
    if s=='123456780':R=c;break
    for d in [-1,1,-3,3]:
        if (not i%3 and d==-1) or (i%3==2 and d==1):continue
        if -1<i+d<9:
            a,b=min(i,i+d),max(i,i+d)
            nS=s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]
            Len=len(Set)
            Set.add(nS)
            if Len==len(Set):continue
            Que.append((nS,i+d,c+1))
print(R)