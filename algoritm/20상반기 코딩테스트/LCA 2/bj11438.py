import sys
sys.stdin = open('bj11438.txt','r')

def find(x):
    if P[x]!=x:P[x]=find(P[x])
    return P[x]
def union(a,b):
    P[find(a)]=find(b)
N=int(input())
A=[[int(x)for x in input().split()]for y in range(N-1)]
P=list(range(N+1))
for l in A:union(l[0],l[1])
print(P)
print(find(11))
print(find(6))