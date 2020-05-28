import sys
sys.stdin = open('bj14500.txt','r')

N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
R=0
for t in range(4):
    A,N,M=list(map(list,zip(*A[::-1]))),M,N
    for i in range(N-2):
        for j in range(M-1):
            R=max(R,max(A[i+2][j]+A[i+2][j+1],A[i+1][j+1]+A[i+2][j+1])+A[i][j]+A[i+1][j],max(A[i+2][j]+A[i+2][j+1],A[i+1][j]+A[i+2][j],A[i+1][j]+A[i+2][j+1])+A[i][j+1]+A[i+1][j+1])
    if t>1:continue
    for i in range(N):
        for j in range(M-3):
            R=max(R,sum(A[i][j:j+4]))
    if t>0:continue
    for i in range(N-1):
        for j in range(M-1):
            R=max(R,A[i][j]+A[i][j+1]+A[i+1][j]+A[i+1][j+1])
print(R)