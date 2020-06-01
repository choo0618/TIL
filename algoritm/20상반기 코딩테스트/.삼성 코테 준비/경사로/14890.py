import sys
sys.stdin = open('bj14890.txt','r')

def Check(l):
    V=[0]*N
    for i in range(N-1):
        t=abs(l[i]-l[i+1])
        if t>1:return 0
        if t==0:continue
        if l[i]>l[i+1]:
            tmp=l[i+1]
            for j in range(i+1,i+L+1):
                if j==N or l[j]!=tmp:return 0
                V[j]=1
        else:
            tmp=l[i]
            for j in range(i-L+1,i+1):
                if j<0 or V[j] or l[j]!=tmp:return 0
                V[j]=1
    return 1
N,L=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for a in A+list(map(list,zip(*A[::-1]))):R+=Check(a)
print(R)