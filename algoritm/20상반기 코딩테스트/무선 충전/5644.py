import sys
sys.stdin = open('5644.txt','r')

dx=[0,0,1,0,-1]
dy=[0,-1,0,1,0]
def Score(a,b):
    r,ai=0,-1
    if a:
        p,i=a.pop()
        ai=i
        r+=p
    if b:
        p,i=b.pop()
        if i==ai:
            if a and b:
                if a[-1][0]>b[-1][0]:r+=a[-1][0]
                else:r+=b[-1][0]
            elif not a and b:r+=b[-1][0]
            elif a and not b:r+=a[-1][0]
        else:r+=p
    return r
for t in range(int(input())):
    M,bc=map(int,input().split())
    A=[int(x)for x in input().split()]
    B=[int(x)for x in input().split()]
    BC=[[int(x)for x in input().split()]for y in range(bc)]
    ax,ay,bx,by=1,1,10,10
    R=0
    for T in range(M+1):
        a,b=[],[]
        for i,(x,y,c,p) in enumerate(BC):
            xd=abs(x-ax)+abs(y-ay)
            yd=abs(x-bx)+abs(y-by)
            if xd<=c:a.append((p,i))
            if yd<=c:b.append((p,i))
        a.sort()
        b.sort()
        R+=Score(a,b)
        if T<M:ax,ay,bx,by=ax+dx[A[T]],ay+dy[A[T]],bx+dx[B[T]],by+dy[B[T]]
    print('#%d %d'%(t+1,R))


