import sys
sys.stdin = open('bj2493.txt','r')

N=int(input())
S,R=[],[]
for i,n in enumerate(map(int,input().split())):
    while S:
        if S[-1][1]>n:R.append(S[-1][0]);break
        S.pop()
    if not S:R.append(0)
    S.append((i+1,n))
print(*R)