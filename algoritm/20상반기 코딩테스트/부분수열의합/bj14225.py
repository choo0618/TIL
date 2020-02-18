import sys
sys.stdin=open('bj14225.txt','r')

def DFS(idx,r):
    Map[r]=1
    for i in range(idx,N):DFS(i+1,r+L[i])
N=int(input())
L=[int(x)for x in input().split()]
Sum=R=sum(L)+1
Map=[0]*Sum
DFS(0,0)
for m in range(Sum):
    if not Map[m]:R=m;break
print(R)
