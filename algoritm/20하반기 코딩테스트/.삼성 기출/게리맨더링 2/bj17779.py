import sys
sys.stdin = open('bj17779.txt','r')

def Sol():
    y2,x2,y3,x3,y4,x4=y+d1,x-d1,y+d2,x+d2,y+d1+d2,x-d1+d2
    L=[0,0,0,0,Sum]
    tmp=x+1
    for i in range(y2):
        if i>=y:tmp-=1
        L[0]+=sum(A[i][:tmp])
    tmp=x+1
    for i in range(y3+1):
        if i>y:tmp+=1
        L[1]+=sum(A[i][tmp:])
    tmp=x2-1
    for i in range(y2,N):
        if i<=y4:tmp+=1
        L[2]+=sum(A[i][:tmp])
    tmp=x3+1
    for i in range(y3+1,N):
        if i<=y4+1:tmp-=1
        L[3]+=sum(A[i][tmp:])
    L[4]-=sum(L[:4])
    return max(L)-min(L)
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Sum=sum(sum(l)for l in A)
R=10**9
for y in range(N-2):
    for x in range(1,N-1):
        for d1 in range(1,x+1):
            for d2 in range(1,N-x):
                if y+d1+d2<N:R=min(R,Sol())
print(R)
