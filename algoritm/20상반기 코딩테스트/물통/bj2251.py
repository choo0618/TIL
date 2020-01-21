import sys
sys.stdin = open('bj2251.txt','r')

A,B,C=map(int,input().split())
Que=[(0,0,C)]
Map,R=[[0]*(B+1) for b in range(A+1)],[]
while Que:
    Q=[]
    for q in Que:
        a,b,c=q
        if Map[a][b]:continue
        if not a:R.append(c)
        Map[a][b]=1
        Q.append((max(a+b-B,0),min(a+b,B),c))
        Q.append((max(a+c-C,0),b,min(a+c,C)))
        Q.append((min(a+b,A),max(a+b-A,0),c))
        Q.append((a,max(b+c-C,0),min(b+c,C)))
        Q.append((min(a+c,A),b,max(a+c-A,0)))
        Q.append((a,min(b+c,B),max(b+c-B,0)))
    Que=Q
R.sort()
for p in R:print(p,end=' ')
