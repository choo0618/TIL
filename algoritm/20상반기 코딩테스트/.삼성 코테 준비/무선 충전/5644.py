import sys
sys.stdin = open('5644.txt','r')

dx=[0,0,1,0,-1]
dy=[0,-1,0,1,0]
def Score(a,b):
    if len(a)>len(b):a,b=b,a
    sa,ia=a.pop()
    sb,ib=b.pop()
    r=sa+sb
    if ia==ib:
        if a and b:r=max(sa+b[-1][0],sb+a[-1][0])
        elif a:r=sb+a[-1][0]
        elif b:r=sa+b[-1][0]
        else:r//=2
    return r
for t in range(int(input())):
    M,BC=map(int,input().split())
    A=[0]+[int(x)for x in input().split()]
    B=[0]+[int(x)for x in input().split()]
    bc=[[int(x)for x in input().split()]for y in range(BC)]
    R,ax,ay,bx,by=0,1,1,10,10
    for d in range(M+1):
        ax+=dx[A[d]];ay+=dy[A[d]]
        bx+=dx[B[d]];by+=dy[B[d]]
        a,b=[],[]
        for i,(x,y,c,p) in enumerate(bc):
            ad=abs(ax-x)+abs(ay-y)
            bd=abs(bx-x)+abs(by-y)
            if ad<=c:a.append((p,i))
            if bd<=c:b.append((p,i))
        a.sort();b.sort()
        if a and b:R+=Score(a,b)
        elif a:R+=a[-1][0]
        elif b:R+=b[-1][0]
    print('#%d %d'%(t+1,R))
