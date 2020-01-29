import sys
sys.stdin = open('bj1507.txt','r')

def Floyd():
    global R
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if i==j or j==k or k==i:continue
                elif A[j][k]>A[j][i]+A[i][k]:R=-1;return
                elif A[j][k]==A[j][i]+A[i][k]:Map[j][k]=0
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[[1]*N for _ in range(N)]
R=0
Floyd()
if R!=-1:
    for i in range(N):
        for j in range(i,N):
            if Map[i][j]:R+=A[i][j]
            elif Map[i][j]==-1:R=-1
        if R==-1:break
print(Map)
print(R)