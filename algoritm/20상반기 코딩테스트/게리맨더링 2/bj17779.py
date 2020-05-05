import sys
sys.stdin = open('bj17779.txt','r')

def Solution(y1,x1,d1,d2):
    y2,x2,y3,x3,y4,x4=y1+d1,x1-d1,y1+d2,x1+d2,y1+d1+d2,x1-d1+d2
    G=[0]*5
    tmp1=x1+1
    for i in range(y2):
        if i>=y1:tmp1-=1
        G[0]+=sum(A[i][:tmp1])
    tmp2=x1+1
    for i in range(y3+1):
        if i>=y1+1:tmp2+=1
        G[1]+=sum(A[i][tmp2:])
    tmp3=x2-1
    for i in range(y2,N):
        if i<=y4:tmp3+=1
        G[2]+=sum(A[i][:tmp3])
    tmp4=x3+1
    for i in range(y3+1,N):
        if i<=y4+1:tmp4-=1
        G[3]+=sum(A[i][tmp4:])
    G[4]=T-sum(G)
    return max(G)-min(G)

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
T,R=sum(sum(l)for l in A),10**9
for y1 in range(0,N-2):
    for x1 in range(1,N-1):
        for d1 in range(1,x1+1):
            for d2 in range(1,N-x1):
                if y1+d1+d2>=6:break
                R=min(R,Solution(y1,x1,d1,d2))
print(R)