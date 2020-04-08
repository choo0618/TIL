import sys
sys.stdin = open('bj18869.txt','r')

N,M=map(int,input().split())
R,A=0,[]
for n in range(N):
    c=''.join(map(str,[s for n,s in sorted([(x,i)for i,x in enumerate(input().split())])]))
    for a in A:R+=a==c
    A.append(c)
print(R)

def Check():
    for x in range(M):
        for y in range(x+1,M):
            if (A[i][x]>A[i][y] and A[j][x]<=A[j][y]) or (A[i][x]<A[i][y] and A[j][x]>=A[j][y]) or (A[i][x]==A[i][y] and A[j][x]!=A[j][y]):return 0
    return 1
N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for i in range(N):
    for j in range(i+1,N):
        if Check():R+=1
print(R)