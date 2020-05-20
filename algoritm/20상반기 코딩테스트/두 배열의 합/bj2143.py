import sys
sys.stdin = open('bj2143.txt','r')

from collections import defaultdict
T=int(input())
a=int(input())
A=[int(x)for x in input().split()]
b=int(input())
B=[int(x)for x in input().split()]
Dic=defaultdict(int)
R=0
for s in range(a):
    Sum=A[s]
    Dic[Sum]+=1
    for e in range(s+1,a):
        Sum+=A[e]
        Dic[Sum]+=1
for s in range(b):
    Sum=B[s]
    R+=Dic[T-Sum]
    for e in range(s+1,b):
        Sum+=B[e]
        R+=Dic[T-Sum]
print(R)