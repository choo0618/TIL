import sys
sys.stdin = open('10507.txt','r')

def Sol(p):
    R,r,a,b=0,S[0],0,2
    while True:
        if S[b]==0:return max(R,r+p)
        if S[b-1]>p:
            R=max(R,r+p)
            r-=S[a]+S[a+1]
            p+=S[a+1]
            a+=2
            if a!=b:continue
        r+=S[b-1]+S[b]
        p-=S[b-1]
        b+=2
for t in range(int(input())):
    N,P=map(int,input().split())
    L=[int(x)for x in input().split()]
    S=[1]
    for i in range(1,N):
        if L[i]-L[i-1]==1:S[-1]+=1
        else:S.append(L[i]-L[i-1]-1);S.append(1)
    S+=[0,0]
    print('#%d %d'%(t+1,Sol(P)))
