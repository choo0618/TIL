import sys
sys.stdin = open('5658.txt','r')

H=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
T=int(input())
for n in range(T):
    L=[int(x)for x in input().split()]
    S=input()
    N=L[0]//4
    R=[]
    for c in range(N):
        p=L[0]-1
        r=0
        for s in S:
            r+=H.index(s)*(16**(p%N))
            if not p%N and not r in R:
                R.append(r)
                r=0
            p-=1
        S=S[-1]+S[0:-1]
    R.sort()
    R.reverse()
    print('#%d %d'%(n+1,R[L[1]-1]))