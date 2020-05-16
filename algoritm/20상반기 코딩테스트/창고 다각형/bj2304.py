import sys
sys.stdin = open('bj2304.txt','r')

def Sum(a,b,c):
    r=0
    S=[]
    for i in range(a,b,c):
        x,n=A[i]
        if not S:S.append((x,n));continue
        if n>=S[-1][1]:
            r+=S[-1][1]*(abs(x-S[-1][0]))
            S.append((x,n))
    return r
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
A.sort()
Idx,R=0,0
for idx,(i,n) in enumerate(A):
    if n>R:I,Idx,R=idx,i,n
R+=Sum(0,I+1,1)
R+=Sum(N-1,I-1,-1)
print(R)