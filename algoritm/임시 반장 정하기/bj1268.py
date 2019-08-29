import sys
sys.stdin = open('bj1268.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
M,R=1,0
for y in range(N):
    r=set()
    for c in range(5):
        mc=A[y][c]
        for m in range(N):
            if m==y:continue
            elif A[m][c]==mc:r.add(m)
    if len(r)>R:R=len(r);M=y+1
print(M)
