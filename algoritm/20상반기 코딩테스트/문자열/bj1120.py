import sys
sys.stdin = open('bj1120.txt','r')

A,B = map(str,input().split())
R=987654321
for c in range(0,len(B)-len(A)+1):
    r=0
    for a in range(len(A)):
        if A[a]!=B[a+c]:
            r+=1
    if r<R:R=r
print(R)