import sys
sys.stdin = open('bj9517.txt','r')

K,N = int(input()),int(input())
A=[[x for x in input().split()]for y in range(N)]
T = 210
for a in A:
    T-=int(a[0])
    if T<=0:break
    if a[1]=='T':
        K+=1
        if K==9:K=1
print(K)