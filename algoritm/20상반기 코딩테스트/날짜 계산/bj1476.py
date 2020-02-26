import sys
sys.stdin = open('bj1476.txt','r')

E,S,M=map(int,input().split())
e,s,m,R=1,1,1,1
while (E,S,M)!=(e,s,m):
    e=e+1 if e+1<=15 else 1
    s=s+1 if s+1<=28 else 1
    m=m+1 if m+1<=19 else 1
    R+=1
print(R)