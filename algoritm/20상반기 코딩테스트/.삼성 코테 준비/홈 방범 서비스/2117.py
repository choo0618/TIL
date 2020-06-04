import sys
sys.stdin = open('2117.txt','r')

def Sol(y,x):
    D=[]
    for i,j in H:D.append(abs(i-y)+abs(j-x))
    D.sort()
    r,k=0,1
    while k<=D[-1]+1:
        c=0
        for d in D:
            if d>=k:break
            c+=1
        if c*M>=k*k+(k-1)*(k-1):r=max(r,c)
        k+=1
    return r
for t in range(int(input())):
    N,M=map(int,input().split())
    A=[[int(x)for x in input().split()]for y in range(N)]
    H=[]
    for i in range(N):
        for j in range(N):
            if A[i][j]:H.append((i,j))
    R=0
    for i in range(N):
        for j in range(N):
            R=max(R,Sol(i,j))
    print('#%d %d'%(t+1,R))