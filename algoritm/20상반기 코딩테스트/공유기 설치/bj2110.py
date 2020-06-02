import sys
sys.stdin = open('bj2110.txt','r')

N,C=map(int,input().split())
L=[int(input())for _ in range(N)]
L.sort()
l,r=L[0],L[-1]-L[0]
R=0
while l<=r:
    mid=(l+r)//2
    s,c=L[0],1
    for i in range(1,N):
        d=L[i]-s
        if d>=mid:
            s=L[i]
            c+=1
    if c>=C:
        R=mid
        l=mid+1
    else:r=mid-1
print(R)

