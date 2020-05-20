import sys
sys.stdin=open('bj14391.txt','r')

N,M=map(int,input().split())
A=[list(map(int,input()))for y in range(N)]
R=0
for t in range(1<<N*M):
    Sum=0
    for i in range(N):
        Sumi=0
        for j in range(M):
            k=i*M+j
            if (1<<k)&t:
                Sum+=Sumi
                Sumi=0
            else:Sumi=10*Sumi+A[i][j]
        Sum+=Sumi
    for j in range(M):
        Sumj=0
        for i in range(N):
            k=i*M+j
            if (1<<k)&t:Sumj=10*Sumj+A[i][j]
            else:
                Sum+=Sumj
                Sumj=0
        Sum+=Sumj
    R=max(R,Sum)
print(R)