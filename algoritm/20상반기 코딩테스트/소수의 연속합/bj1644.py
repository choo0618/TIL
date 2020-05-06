import sys
sys.stdin = open('bj1644.txt','r')

N=int(input())
L,l=[],0
Map=[0,0]+[1]*(N-1)
for i in range(2,N+1):
    if not Map[i]:continue
    L.append(i)
    l+=1
    for j in range(i,N//i+1):Map[i*j]=0
R,s,j=0,0,0
for i in range(l):
    s+=L[i]
    while s>N:
        s-=L[j]
        j+=1
    if s==N:R+=1
print(R)
