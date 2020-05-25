import sys
sys.stdin = open('bj17779.txt','r')

def Soultion(y1,x1,d1,d2):
    y2,x2,y3,x3,y4,x4=y1+d1,x1-d1,y1+d2,x1+d2,y1+d1+d2,x1+d2-d1
    L=[0,0,0,0,0]
    tmp=x1+1
    for i in range(y2):
        if i>=y1:tmp-=1
        L[0]+=sum(A[i][:tmp])
    tmp=x1+1
    for i in range(y3+1):
        if i>y1:tmp+=1
        L[1]+=sum(A[i][tmp:])
    tmp=x2-1
    for i in range(y2,N):
        if i<=y4:tmp+=1
        L[2]+=sum(A[i][:tmp])
    tmp=x3+1
    for i in range(y3+1,N):
        if i<=y4+1:tmp-=1
        L[3]+=sum(A[i][tmp:])
    L[4]=Sum-sum(L[:4])
    return max(L)-min(L)
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Sum=sum(sum(x)for x in A)
R=Sum
for y1 in range(N-2):
    for x1 in range(1,N-1):
        for d1 in range(1,x1+1):
            for d2 in range(1,N-x1):
                if y1+d1+d2>=N:break
                R=min(R,Soultion(y1,x1,d1,d2))
print(R)