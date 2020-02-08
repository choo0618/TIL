import sys
sys.stdin = open('bj2352.txt','r')

N=int(input())
Map=[1]*(N+1)
L=[0]+[int(x)for x in input().split()]
for i in range(1,N+1):
    for j in range(i,0,-1):
        if L[i]>L[j] and Map[i]<=Map[j]:Map[i]=Map[j]+1
print(max(Map))


