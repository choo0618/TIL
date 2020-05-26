import sys
sys.stdin = open('bj17281.txt','r')

import itertools
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
S=0
for Per in itertools.permutations(range(1,9),8):
    Per=list(Per)
    Per.insert(3,0)
    s,i=0,0
    for j in range(N):
        a,b,c,o=0,0,0,0
        while o!=3:
            h=A[j][Per[i]]
            if h==1:s+=c;a,b,c=1,a,b
            elif h==2:s+=b+c;a,b,c=0,1,a
            elif h==3:s+=a+b+c;a,b,c=0,0,1
            elif h==4:s+=a+b+c+1;a,b,c=0,0,0
            else:o+=1
            i=(i+1)%9
    S=max(S,s)
print(S)