import sys
sys.stdin = open('5648.txt','r')

dx=[0,0,-1,1]
dy=[1,-1,0,0]
for t in range(int(input())):
    N=int(input())
    A=[]
    for a in range(N):
        x,y,d,e=map(int,input().split())
        A.append([2*x,2*y,d,e])
    R=0
    while N:
        tmp,Set1,Set2=[],set(),set()
        for a in A:
            a[0]+=dx[a[2]];a[1]+=dy[a[2]]
            Len=len(Set1)
            Set1.add((a[0],a[1]))
            if Len==len(Set1):Set2.add((a[0],a[1]))
        for x,y,d,e in A:
            if (x,y) in Set2:R+=e;N-=1
            elif min(x,y)<-2000 or max(x,y)>2000:N-=1
            else:tmp.append([x,y,d,e])
        A=tmp
    print('#%d %d'%(t+1,R))