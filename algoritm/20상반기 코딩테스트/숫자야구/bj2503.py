import sys
sys.stdin=open('bj2503.txt','r')

def Check():
    check=0
    for i in L:
        S,B=0,0
        for s in range(3):
            if I[s] in i[0]:
                if s==i[0].index(I[s]):S+=1
                else:B+=1
        if i[1]==str(S) and str(B)==i[2]:check+=1
    if check==N:return True
    return False
N=int(input())
L=[input().split()for y in range(N)]
R=0
for i in range(100,1000):
    I=str(i)
    if '0' in I or I[0]==I[1] or I[1]==I[2] or I[2]==I[0]:continue
    if Check():R+=1
print(R)

import itertools
N=int(input())
L=[input().split()for y in range(N)]
R=0
for p in itertools.permutations('123456789',3):
    check=0
    for l in L:
        s=b=0
        for i in range(3):
            if l[0][i]==p[i]:s+=1
            elif p[i] in l[0]:b+=1
        if str(s)==l[1] and str(b)==l[2]:check+=1
    if check==N:R+=1
print(R)