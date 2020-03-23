import sys
sys.stdin = open('bj1931.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for _ in range(N)]
A.sort(key=lambda x:(x[1],x[0]))
print(A)
R,end=0,0
for s,e in A:
    if s>=end:
        end=e
        R+=1
print(R)