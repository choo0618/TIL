import sys
sys.stdin=open('bj9205.txt','r')

T=int(input())
for t in range(T):
    N=int(input())
    HY,HX=map(int,input().split())
    Mart=[]
    Map=[0]*N
    for i in range(N):
        my,mx=map(int,input().split())
        Mart.append((my,mx))
    FY,FX=map(int,input().split())
    Check=1
    Que=[(HY,HX)]
    while Que and Check:
        Q=[]
        for q in Que:
            if abs(q[0]-FY)+abs(q[1]-FX)<=1000:Check=0;break
            for idx,m in enumerate(Mart):
                Len=abs(m[0]-q[0])+abs(m[1]-q[1])
                if not Map[idx] and Len<=1000:
                    Map[idx]=1
                    Q.append(m)
        Que=Q
    if Check:print('sad')
    else:print('happy')
