import sys
sys.stdin = open('bj17281.txt','r')

from itertools import permutations
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for p in permutations(range(1,9)):
    p=list(p);p.insert(3,0)
    S,idx=0,0
    for n in range(N):
        a,b,c,o=0,0,0,0
        while o!=3:
            tmp=A[n][p[idx]]
            if tmp==1:S+=c;a,b,c=1,a,b
            elif tmp==2:S+=b+c;a,b,c=0,1,a
            elif tmp==3:S+=a+b+c;a,b,c=0,0,1
            elif tmp==4:S+=a+b+c+1;a,b,c=0,0,0
            else:o+=1
            idx=(idx+1)%9
    R=max(R,S)
print(R)