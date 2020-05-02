import sys
sys.stdin = open('bj2644.txt','r')

N=int(input())
L=[int(x)for x in input().split()]
P=int(input())
A=[[int(x)for x in input().split()]for y in range(P)]
M=[0]*(N+1)
M[L[0]]=1
Q=[[L[0],1]]
R=-1
while Q:
    q,a=[],[]
    for qq in Q:
        for z in A:
            if qq[0] in z:s=sum(z)-qq[0];M[s]=qq[1]+1;q.append([s,qq[1]+1])
            else:a.append(z)
    if M[L[1]]:break
    A,Q=a,q
print(M[L[1]]-1)