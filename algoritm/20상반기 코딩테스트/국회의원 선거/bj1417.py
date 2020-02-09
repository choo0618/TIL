import sys
sys.stdin=open('bj1417.txt','r')

N=int(input())
L=[int(input())for _ in range(N)]
D=L[0]
L[0]=0
R=0
while D<=max(L):
    L.sort()
    L[-1]-=1
    D+=1
    R+=1
print(R)