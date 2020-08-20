import sys
sys.stdin = open('10204.txt','r')

for t in range(int(input())):
    N=int(input())
    A,B,C=[],[],[0]*N
    for _ in range(N):
        a,b=map(int,input().split())
        A.append((a,_))
        B.append((b,_))
    A.sort();B.sort()
    a,b,R=0,0,0
    tmp=1
    while N:
        if tmp:
            while C[A[a][1]]:a+=1
            C[A[a][1]]=1
            R+=A[a][0]
        else:
            while C[B[b][1]]:b+=1
            C[B[b][1]]=1
            R-=B[b][0]
        N-=1
        tmp=(tmp+1)%2
    print('#%d %d'%(t+1,R))
