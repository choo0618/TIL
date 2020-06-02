import sys
sys.stdin = open('bj17086.txt','r')

N,M=map(int,input().split())
R,s,S,A=0,0,[],[]
for i in range(N):
    l=[int(x)for x in input().split()]
    for j in range(M):
        if l[j]:S.append((i,j));s+=1
    A.append(l)
for i in range(N):
    for j in range(M):
        if A[i][j]:continue
        r=10**9
        for y,x in S:r=min(r,max(abs(i-y),abs(j-x)))
        R=max(r,R)
print(R)