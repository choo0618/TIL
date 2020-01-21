import sys
sys.stdin=open('bj9019.txt','r')

T=int(input())
for t in range(T):
    N,M=map(int,input().split())
    Map,Check=[0]*10000,1
    Map[N]=[1,1,1,1]
    Que=[[N,'']]
    R=''
    while Check:
        Q=[]
        for q in Que:
            d1=q[0]//1000
            d2=q[0]//100-d1*10
            d3=q[0]//10-d1*100-d2*10
            d4=q[0]-d1*1000-d2*100-d3*10
            for idx,d in enumerate(['D','S','L','R']):
                if d=='D':n=2*q[0]%10000
                elif d=='S':
                    if q[0]:n=q[0]-1
                    else:n=9999
                elif d=='L':n=((d2*10+d3)*10+d4)*10+d1
                else:n=((d4*10+d1)*10+d2)*10+d3
                if n==M:R=q[1]+d;Check=0;break
                if not Map[n]:
                    Map[n]=1
                    Q.append([n,q[1]+d])
            if not Check:break
        Que=Q
    print(R)