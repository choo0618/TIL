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
    R=0
    while N:
        Q,l,ll=[],set(),set()
        for a in A:
            a[0]+=dx[a[2]]
            a[1]+=dy[a[2]]
            le=len(l)
            l.add((a[0],a[1]))
            if le==len(l):ll.add((a[0],a[1]))
        for s in A:
            if ll and (s[0],s[1]) in ll:
                R+=s[3]
                N-=1
            elif max(s)>2000 or min(s)<-2000:N-=1
            else:
                Q.append(s)
        A=Q
    print('#%d %d'%(n+1,R))