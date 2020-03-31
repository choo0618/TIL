import sys
sys.stdin = open('bj14500.txt','r')

N,M=map(int,input().split())
A=[[int(x)for x in input().split()]for y in range(N)]
Max=0
for t in range(4):
    A,N,M=list(map(list,zip(*A[::-1]))),M,N
    for i in range(N-1):
        for j in range(M-2):
            Max=max(Max,max(A[i][j+1]+A[i][j+2],A[i+1][j+1]+A[i+1][j+2])+A[i][j]+A[i+1][j],max(A[i][j]+A[i+1][j+2],A[i][j+2]+A[i+1][j],A[i][j]+A[i][j+2],A[i+1][j]+A[i+1][j+2])+A[i][j+1]+A[i+1][j+1])
    if t==2 or t==3:continue
    for i in range(N):
        for j in range(M-3):
            Max=max(Max,sum(A[i][j:j+4]))
    if t==1:continue
    for i in range(N-1):
        for j in range(M-1):
            Max=max(Max,sum(A[i][j:j+2])+sum(A[i+1][j:j+2]))
print(Max)

