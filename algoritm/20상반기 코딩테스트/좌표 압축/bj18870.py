import sys
sys.stdin = open('bj18870.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
I=sorted(set(L))
Dic={}
for n in range(len(I)):Dic[I[n]]=str(n)
for i in range(N):L[i]=Dic[L[i]]
print(' '.join(L))