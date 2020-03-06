import sys
sys.stdin = open('bj2798.txt','r')

def DFS(idx,r,c):
    global R
    if r>M:return
    if c==3:
        R=max(R,r)
        return
    for i in range(idx,N):
        DFS(i+1,r+L[i],c+1)
N,M=map(int,input().split())
L=[int(x)for x in input().split()]
R=0
DFS(0,0,0)
print(R)

import bisect
N,M=map(int,input().split())
L=[int(x)for x in input().split()]
L.sort()
R=0
for i in range(N):
 for j in range(i+1,N):
  r=L[i]+L[j]
  k=bisect.bisect(L,M-r)-1
  if j>=k:break
  R=max(R,r+L[k])
print(R)