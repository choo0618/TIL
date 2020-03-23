import sys
sys.stdin = open('bj17608.txt','r')

N=int(input())
L=[int(input())for _ in range(N)]
r,tmp=0,0
for i in range(N-1,-1,-1):
    if L[i]>tmp:
        tmp=L[i]
        r+=1
print(r)
