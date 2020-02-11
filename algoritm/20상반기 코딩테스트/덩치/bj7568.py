import sys
sys.stdin = open('bj7568.txt','r')

N=int(input())
A=[[int(x)for x in input().split()]for y in range(N)]
Map=[1]*N
for idx,n in enumerate(A):
    for n1 in A:
        if n[0]<n1[0] and n[1]<n1[1]:Map[idx]+=1
print(' '.join(map(str,Map)))
