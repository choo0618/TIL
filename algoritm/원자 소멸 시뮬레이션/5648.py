import sys
sys.stdin = open('5648.txt','r')

dx=[0,0,-1,1]
dy=[1,-1,0,0]
T=int(input())
for n in range(T):
    N=int(input())
    A=[[int(x)for x in input().split()]for y in range(N)]
    for p in A:
        p[0]*=2
        p[1]*=2
    R,t=0,0
    while t<4000:
        S,l,ll=[],[],[]
        for a in A:
            a[0]+=dx[a[2]]
            a[1]+=dy[a[2]]
            if not [a[0],a[1]]in l:l.append([a[0],a[1]])
            else:ll.append([a[0],a[1]])
        if ll:
            for s in A:
                if [s[0],s[1]] in ll:S.append(s)
        for rr in S:
            R+=rr[3]
            A.pop(A.index(rr))
        t+=1
    print('#%d %d'%(n+1,R))